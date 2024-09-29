import React from "react";
import { useLocation } from "react-router-dom";
import "./results.css";

const Results = () => {
  const location = useLocation();
  const { processedData } = location.state || { processedData: [] };

  return (
    <div className="page-container">
      <div className="results-container">
        <div className="results-text">
          <h1>Based off your reels, try this out</h1>
        </div>
        <div className="results-display">
          {processedData.map((data, index) => (
            <div className="result">
              <a href={data.url} className="class-link">{data.hobby}</a>
              <p className="class-name">{data.name}</p>
              <p className="class-desc">{data.description}</p>
              <img src={data.image} alt="Class" className="class-img"/>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Results;
