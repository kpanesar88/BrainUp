import React from "react";
import { useLocation } from "react-router-dom";
import "./results.css";

const Results = () => {
  const location = useLocation();
  const { processedData } = location.state || { processedData: [] };

  return (
    <div className="page-container">
      {processedData.map((data, index) => (
        <div key={index} className={`bgimg${index + 1}`}>
            <img src={data.image} alt={`Background ${index + 1}`} />
        </div>
      ))}
      <div className="results-container">
        <div className="results-text">
          <h1>Based off your reels, try this out</h1>
        </div>
        <div className="results-display">
          {processedData.map((data, index) => (
            <div key={index} className="result">
              <h3>{data.title}</h3>
              <p>{data.contact}</p>
              <p>{data.description}</p>
              <img src={data.classImage} alt={`Class Image ${index + 1}`}/>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Results;
