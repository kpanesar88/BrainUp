import React, { useState } from "react";
import { useDropzone } from "react-dropzone";
import ProgressBar from "./progressbar";
import { useNavigate } from "react-router-dom";
import "./form.css";

const FileUpload = () => {
  const [uploadedFiles, setUploadedFiles] = useState([]);
  const [text, setText] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [progress, setProgress] = useState(0);
  const [isFormVisible, setIsFormVisible] = useState(true);
  const navigate = useNavigate();

  const { getRootProps, getInputProps } = useDropzone({
    onDrop: (acceptedFiles) => {
      setUploadedFiles(acceptedFiles);
    },
  });

  const handleSubmit = (event) => {
    event.preventDefault();
    setIsLoading(true);
    setIsFormVisible(false);

    // send get request to server with text and uploaded files
    const formData = new FormData();
    formData.append("text", text);
    uploadedFiles.forEach((file) => {
      formData.append("files", file);
    });

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://localhost:4000/hobby_card", true);

    xhr.upload.onprogress = (progressEvent) => {
      const percentCompleted = Math.round(
        (progressEvent.loaded * 100) / progressEvent.total
      );
      setProgress(percentCompleted);
    };

    xhr.onload = () => {
      if (xhr.status === 200) {
        const response = JSON.parse(xhr.responseText);
        console.log(response);
        setIsLoading(false);
        navigate("/results", { state: { processedData: response } });
      } else {
        console.error("Error:", xhr.statusText);
        setIsLoading(false);
      }
    };

    xhr.onerror = () => {
      console.error("Error:", xhr.statusText);
      setIsLoading(false);
    };

    xhr.send(formData);

  };
  return (
    <div className="form-container">
      {isLoading && <ProgressBar progress={progress} />}
      {isFormVisible && (
        <form onSubmit={handleSubmit}>
          <div className="text-input">
            <input
              type="text"
              placeholder="Enter your city"
              name="locationInput"
            />
          </div>
          <div {...getRootProps()} className="file-upload">
            <input {...getInputProps()} />
            <p className="brainrot-msg">Upload your brainrot</p>
            <p>Choose a file or drop it here</p>
            <ul>
              {uploadedFiles.map((file) => (
                <li key={file.path}>{file.path}</li>
              ))}
            </ul>
          </div>
          <button type="submit" className="submit">
            Go
          </button>
        </form>
      )}
    </div>
  );
};

export default FileUpload;
