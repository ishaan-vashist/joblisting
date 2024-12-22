import React from 'react';
import { Link } from 'react-router-dom';
import './JobCard.css';

const JobCard = ({ job }) => {
  return (
    <div className="job-card">
      <h3>{job.title}</h3>
      <p><strong>Company:</strong> {job.company_name}</p>
      <p><strong>Location:</strong> {job.location}</p>
      <Link to={`/jobs/${job.id}`} className="details-button">
        View Details
      </Link>
    </div>
  );
};

export default JobCard;
