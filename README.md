# Job Listing Application

## Overview
The Job Listing Application is a comprehensive platform for posting, managing, and scraping job listings. It integrates a React.js frontend, a Django-based backend, and Scrapy for web scraping to offer a complete solution for job seekers and recruiters.

## Features
- **Frontend**: User-friendly interface for browsing and posting jobs.
- **Backend**: Robust API with Django for handling job data.
- **Web Scraping**: Automated job listing scraping using Scrapy.
- **Responsive Design**: Ensures optimal user experience across devices.

## Directory Structure
```
joblisting-main/
├── job-listing-frontend/          # React.js frontend
│   ├── src/                       # Frontend source files
│   │   ├── components/            # Reusable components
│   │   ├── pages/                 # Application pages
│   │   ├── App.js                 # Main React app component
│   │   └── index.js               # Entry point for React app
│   ├── public/                    # Public assets
│   ├── package.json               # Dependencies for React app
│   └── README.md                  # Frontend documentation
├── joblisting_project/            # Django backend
│   ├── jobs/                      # Django app for job handling
│   │   ├── models.py              # Job models
│   │   ├── serializers.py         # REST API serializers
│   │   ├── views.py               # View logic for job data
│   │   └── urls.py                # URL routing for jobs app
│   ├── joblisting_project/        # Main Django project files
│   │   ├── settings.py            # Django settings
│   │   ├── urls.py                # Project-wide URLs
│   │   └── wsgi.py                # WSGI application
│   ├── manage.py                  # Django management script
├── job_scraper/                   # Scrapy-based web scraper
│   ├── spiders/                   # Scrapy spiders for scraping
│   │   └── jobs_spider.py         # Spider for job scraping
│   ├── items.py                   # Scrapy items definitions
│   ├── settings.py                # Scrapy settings
│   └── scrapy.cfg                 # Scrapy configuration file
├── requirements.txt               # Backend dependencies
├── package.json                   # Frontend dependencies
└── read me.docx                   # Additional documentation
```

## Prerequisites
### Backend
- Python 3.8+
- Django 4.0+
- Scrapy 2.6+

### Frontend
- Node.js 16+
- npm 7+

## Installation

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd joblisting_project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd job-listing-frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

### Web Scraper Setup
1. Navigate to the scraper directory:
   ```bash
   cd job_scraper
   ```
2. Run the spider:
   ```bash
   scrapy crawl jobs_spider
   ```

## Usage
1. Open the frontend application at `http://localhost:3000`.
2. Use the interface to browse or post jobs.
3. Access backend APIs at `http://localhost:8000`.
4. Run the scraper to fetch job listings from external sources.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit changes and push:
   ```bash
   git commit -m "Description of changes"
   git push origin feature-name
   ```
4. Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, please contact ishaanvashista@gmail.com.

