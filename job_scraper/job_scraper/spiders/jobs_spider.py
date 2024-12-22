import scrapy
import requests
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

class JobsSpider(scrapy.Spider):
    name = "jobs_spider"
    allowed_domains = ["dice.com"]
    start_urls = [
        "https://www.dice.com/jobs?q=Software&radius=30&radiusUnit=mi&page=1&pageSize=20&filters.postedDate=ONE&filters.workplaceTypes=Remote&filters.employmentType=CONTRACTS&currencyCode=USD&language=en"
    ]

    def __init__(self):
        # Set Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--no-sandbox")

        # Path to the chromedriver
        chrome_driver_path = r"C:\\Users\\ishaa\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

    def parse(self, response):
        """
        Parse the job listings page and follow links to job details.
        """
        self.driver.get(response.url)

        try:
            # Wait for the job listings to load
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.card a'))
            )

            while True:
                # Extract job links
                job_links = self.driver.find_elements(By.CSS_SELECTOR, 'div.card a')
                job_urls = [a.get_attribute('href') for a in job_links if a.get_attribute('href')]

                if not job_urls:
                    self.logger.warning("No job links found on the page. Check the CSS selector.")
                    break

                self.logger.info(f"Found {len(job_urls)} job links.")

                for job_url in job_urls:
                    self.logger.info(f"Following job URL: {job_url}")
                    yield scrapy.Request(job_url, callback=self.parse_job_details)
                    time.sleep(1)  # Rate limiting to avoid being blocked

                # Handle pagination using the Next button
                try:
                    next_button = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Next"]')
                    actions = ActionChains(self.driver)
                    actions.move_to_element(next_button).perform()
                    next_button.click()

                    # Wait for the next page to load
                    WebDriverWait(self.driver, 30).until(
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.card a'))
                    )

                except (NoSuchElementException, ElementClickInterceptedException):
                    self.logger.info("No next button found or pagination completed.")
                    break

        except Exception as e:
            self.logger.error(f"Error while parsing job listings: {e}")

        finally:
            self.driver.quit()

    def parse_job_details(self, response):
        """
        Extract job details from the job page.
        """
        job_data = {
            "title": response.css('h1[data-cy="jobTitle"]::text').get(default="").strip(),
            "company_name": response.css('a[data-cy="companyNameLink"]::text').get(default="").strip(),
            "location": response.css('li[data-cy="location"]::text').get(default="").strip(),
            "posted_date": self.parse_posted_date(response.css('li[data-cy="postedDate"] span#timeAgo::text').get(default="").strip()),
            "description": " ".join(response.css('div[data-testid="jobDescriptionHtml"] *::text').getall()).strip(),
            "company_profile_url": response.css('a[data-cy="companyNameLink"]::attr(href)').get(default=""),
            "employment_details": response.css('div[data-cy="employmentDetails"] span::text').get(default="").strip(),
            "details_url": response.url,  # Add details URL
        }

        # Skip jobs with missing essential fields
        if not job_data["title"] or not job_data["company_name"] or not job_data["details_url"]:
            self.logger.warning(f"Skipping incomplete job data: {job_data}")
            return

        self.logger.info(f"Scraped job: {job_data}")
        self.send_to_backend(job_data)
        yield job_data

    def parse_posted_date(self, posted_date):
        """
        Convert the posted_date to YYYY-MM-DD format or return today's date if invalid.
        """
        if not posted_date:
            return datetime.now().strftime("%Y-%m-%d")

        try:
            # Handle formats like "Dec 21, 2024" or "1 day ago"
            if "day" in posted_date or "hour" in posted_date:
                return datetime.now().strftime("%Y-%m-%d")
            elif "," in posted_date:  # Example: "Dec 21, 2024"
                return datetime.strptime(posted_date, "%b %d, %Y").strftime("%Y-%m-%d")
        except ValueError:
            self.logger.error(f"Invalid date format: {posted_date}")
            return datetime.now().strftime("%Y-%m-%d")

    def send_to_backend(self, job_data):
        """
        Send the scraped job data to the Django backend API.
        """
        retries = 3
        for attempt in range(retries):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/api/jobs/create/",
                    json=job_data,
                    timeout=10
                )
                if response.status_code == 201:
                    self.logger.info(f"Successfully sent job: {job_data['title']}")
                    break
                else:
                    self.logger.error(f"Failed to send job (Attempt {attempt + 1}): {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                self.logger.error(f"Error sending job to backend (Attempt {attempt + 1}): {e}")

            if attempt < retries - 1:
                self.logger.info("Retrying...")
                time.sleep(2)
            else:
                self.logger.error("Max retries reached. Could not send job to backend.")
