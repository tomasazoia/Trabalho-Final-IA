import React, { useState } from "react";
import WebcamCapture from "./components/WebCapture";
import UploadImage from "./components/UploadImage";
import "./App.css";

function App() {
  const [username, setUsername] = useState("");
  const [capturedImage, setCapturedImage] = useState(null);

  return (
    <div className="login-container">
      <div className="login-box">
        <h1>Login</h1>
        <form>
          <div className="form-group">
            <label htmlFor="username">Nome</label>
            <input
              type="text"
              id="username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="login-button">
            Entrar
          </button>
        </form>
        <h2>Reconhecimento de Matrícula</h2>
        <div className="webcam-container">
          <WebcamCapture onCapture={setCapturedImage} />
          <UploadImage image={capturedImage} />
        </div>
      </div>
    </div>
  );
}

export default App;
