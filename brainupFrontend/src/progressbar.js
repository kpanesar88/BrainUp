import React from 'react';
import './progressbar.css';

const ProgressBar = ({progress}) => {
    return (
        <div className='progress'>
            <h4>Gathering Data...</h4>
            <div className="progress-container">
                <div className="progress-bar" style={{width: `${progress}%`}}></div>
            </div>'
        </div>
    );
}

export default ProgressBar;