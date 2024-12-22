import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { FaBriefcase, FaGlobe, FaPaperPlane } from 'react-icons/fa';
import './Home.css';

const Home = () => {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchJobs = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/jobs/');
        if (response.data.jobs && Array.isArray(response.data.jobs)) {
          setJobs(response.data.jobs);
        } else {
          setJobs([]);
          setError('Unexpected data format from server.');
        }
      } catch (err) {
        console.error('Error fetching jobs:', err);
        setError('Error fetching jobs. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchJobs();
  }, []);

  return (
    <div className="home-container">
      {/* Hero Section */}
      <section className="hero-section">
        <div className="hero-content">
          <h1>Find Your Dream Job</h1>
          <p>
            Discover top opportunities in remote, freelance, and full-time roles. Your next adventure begins here!
          </p>
          <button className="cta-button">Start Exploring</button>
        </div>
      </section>

      {/* Features Section */}
      <section className="features-section">
        <h2>Why Choose Us?</h2>
        <div className="features">
          <div className="feature-card">
            <FaBriefcase className="feature-icon" />
            <h3>Extensive Opportunities</h3>
            <p>Explore job opportunities in various domains tailored to your expertise.</p>
          </div>
          <div className="feature-card">
            <FaGlobe className="feature-icon" />
            <h3>Remote Work</h3>
            <p>Enjoy working from anywhere with our curated list of remote roles.</p>
          </div>
          <div className="feature-card">
            <FaPaperPlane className="feature-icon" />
            <h3>Easy Applications</h3>
            <p>Experience a seamless and user-friendly job application process.</p>
          </div>
        </div>
      </section>

      {/* Recent Jobs Section */}
      <section className="recent-jobs-section">
        <h2>Recent Job Listings</h2>
        <p className="recent-jobs-text">Carefully curated opportunities to help you land your next role.</p>

        {loading && <p className="loading">Loading...</p>}
        {error && <p className="error">{error}</p>}
        {!loading && !error && jobs.length === 0 && (
          <p className="no-jobs-message">No jobs are currently available. Please check back later!</p>
        )}

        {!loading && !error && jobs.length > 0 && (
          <div className="jobs-list">
            {jobs.map((job) => (
              <div key={job.id} className="job-card">
                <div className="job-header">
                  <h3 className="job-title">{job.title || 'Unknown Title'}</h3>
                  <p className="company-name">{job.company_name || 'Unknown Company'}</p>
                </div>
                <div className="job-info">
                  <p>
                    <strong>Location:</strong> {job.location || 'Not Provided'}
                  </p>
                  <p>
                    <strong>Salary:</strong> {job.salary || 'Not Disclosed'}
                  </p>
                </div>
                <a href={`/jobs/${job.id}`} className="job-details-link">
                  View Job Details
                </a>
              </div>
            ))}
          </div>
        )}
      </section>

      {/* Call to Action Section */}
      <section className="cta-section">
        <div className="cta-content">
          <h2>Land Your Dream Job Today</h2>
          <p>Take the first step towards your career growth with our platform.</p>
          <button className="cta-button-secondary">Join Us Now</button>
        </div>
      </section>
    </div>
  );
};

export default Home;
