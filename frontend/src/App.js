import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, useNavigate } from "react-router-dom";
import WebcamCapture from "./components/WebCapture";
import UploadImage from "./components/UploadImage";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Dashboard from "./pages/Dashboard";
import History from "./pages/History";

function Login() {
  const [username, setUsername] = useState("");
  const [capturedImage, setCapturedImage] = useState(null);
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!username || !capturedImage) {
      setMessage("Por favor, insira um nome e capture uma imagem.");
      return;
    }

    let imageFile = capturedImage;
    if (capturedImage.startsWith("data:image")) {
      const byteString = atob(capturedImage.split(",")[1]);
      const arrayBuffer = new ArrayBuffer(byteString.length);
      const uint8Array = new Uint8Array(arrayBuffer);
      for (let i = 0; i < byteString.length; i++) {
        uint8Array[i] = byteString.charCodeAt(i);
      }
      imageFile = new Blob([uint8Array], { type: "image/jpeg" });
    }

    const formData = new FormData();
    formData.append("nome", username);
    formData.append("image", imageFile, "captured.jpg");

    try {
      const response = await fetch("http://127.0.0.1:8000/api/salvar_usuario_matricula/", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (response.ok) {
        setMessage("Login bem-sucedido!");
        setTimeout(() => {
          navigate("/dashboard");
        }, 2000);
      } else {
        setMessage(data.message || "Erro ao processar a requisição.");
      }
    } catch (error) {
      console.error("Erro na requisição:", error);
      setMessage("Erro ao conectar ao servidor.");
    }
  };

  return (
    <div className="container mt-5">
      <div className="row justify-content-center">
        <div className="col-md-6">
          <div className="card shadow p-4">
            <h2 className="text-center mb-3">Login</h2>

            <form onSubmit={handleSubmit}>
              <div className="mb-3">
                <label htmlFor="username" className="form-label">Nome</label>
                <input
                  type="text"
                  id="username"
                  className="form-control"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  required
                />
              </div>

            </form>

            <hr />

            <h4 className="text-center mt-3">Reconhecimento de Matrícula</h4>

            <div className="d-flex flex-column align-items-center mt-3">
              <WebcamCapture onCapture={setCapturedImage} />
              <UploadImage image={capturedImage} />
            </div>

            {message && <div className="alert alert-info text-center mt-3">{message}</div>}
            <button type="submit" className="btn btn-primary w-100">Entrar</button>
            
          </div>
          
        </div>
        
      </div>
    </div>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/history" element={<History />} />
      </Routes>
    </Router>
  );
}

export default App;
