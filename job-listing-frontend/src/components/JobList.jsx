import React from 'react';
import './JobList.css';

const JobList = ({ jobs }) => {
  if (!Array.isArray(jobs) || jobs.length === 0) {
    return <p>No jobs available.</p>;
  }

  return (
    <div className="job-list">
      {jobs.map((job) => (
        <div key={job.id} className="job-card">
          <h3>{job.title !== 'N/A' ? job.title : 'Title Not Available'}</h3>
          <p><strong>Company:</strong> {job.company_name !== 'N/A' ? job.company_name : 'Company Not Available'}</p>
          <p><strong>Location:</strong> {job.location !== 'N/A' ? job.location : 'Location Not Available'}</p>
          <p><strong>Salary:</strong> {job.salary !== 'N/A' ? job.salary : 'Salary Not Available'}</p>
          <a href={job.details_url} target="_blank" rel="noopener noreferrer">
            View Job Details
          </a>
        </div>
      ))}
    </div>
  );
};

export default JobList;
