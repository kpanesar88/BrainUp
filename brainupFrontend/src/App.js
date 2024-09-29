import logo from "./logo.svg";
import shortlogo from "./shortlogo.png";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import "./App.css";
import Form from "./form";
import Results from "./results";

function App() {
  return (
    <Router>
      <div className="App">
        <ul className="top-header">
          <li>
            <img src={shortlogo} className="Header-logo" alt="logo" />
          </li>
          <li className="slogan">
            <h1>Lets Fix Brainrot</h1>
          </li>
        </ul>
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
        </header>

        <Routes>
          <Route path="/" element={<Form />} />
          <Route path="/results" element={<Results />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
