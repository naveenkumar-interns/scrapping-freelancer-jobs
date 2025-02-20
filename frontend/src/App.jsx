import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [query, setQuery] = useState('');
  const [jobs, setJobs] = useState([]);
  const [platform, setPlatform] = useState('freelancer.com');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(`http://localhost:8000/api/scrape_jobs?search_query=${query}&platform=${platform}`);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const data = await response.json();
      setJobs(data);
        setJobs(data);
      } catch (err) {
        setError('Failed to fetch jobs. Please try again.');
        console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <h1>Freelancer Job Search</h1>
      
      <form onSubmit={handleSearch} className="search-form">
        <div className="form-group">
          <label htmlFor="platform-select">Platform:</label>
          <select
            id="platform-select"
            value={platform}
            onChange={(e) => setPlatform(e.target.value)}
            className="platform-select"
          >
            <option value="freelancer.com">Freelancer.com</option>
            <option value="upwork.com">Upwork.com</option>
            <option value="fiverr.com">Fiverr.com</option>
          </select>
        </div>
        <div className="form-group">
          <label htmlFor="search-input">Job Keyword:</label>
          <input
            id="search-input"
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Enter job keyword..."
            className="search-input"
          />
        </div>
        <button type="submit" className="search-button" disabled={loading}>
          {loading ? 'Searching...' : 'Search'}
        </button>
      </form>

      {error && <div className="error-message">{error}</div>}

      <div className="jobs-container">
        {jobs.map((job, index) => (
          <div key={index} className="job-card">
            <h3>{job.title}</h3>
            <a href={job.link} target="_blank" rel="noopener noreferrer">
              View Job
            </a>
          </div>
        ))}
      </div>
    </div>
  );
};

export default App;