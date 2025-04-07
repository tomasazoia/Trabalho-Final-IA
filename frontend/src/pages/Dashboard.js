import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./styles/Dashboard.css";
import Sidebar from "../components/Sidebar";
import MapComponent from "../components/mapComponent";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import "bootstrap/dist/css/bootstrap.min.css";

function Dashboard() {
  const navigate = useNavigate();
  const [pontoPartida, setPontoPartida] = useState("");
  const [pontoChegada, setPontoChegada] = useState("");
  const [metodo, setMetodo] = useState("");

  const handleCalcularRota = async () => {
    if (!pontoPartida || !pontoChegada || !metodo) {
      alert("Preencha todos os campos!");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/api/calcular_rota/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_id: parseInt(localStorage.getItem("userId")),
          partida: pontoPartida,
          chegada: pontoChegada,
          algoritmo: metodo,
        }),
      });

      const data = await response.json();
      if (response.ok) {
        console.log("Rota calculada:", data);
        alert(`Distância: ${data.distancia_total_km} km\nCaminho: ${data.caminho.join(" ➝ ")}`);
        // podes navegar ou passar os dados para outro componente aqui
      } else {
        alert(data.erro || "Erro ao calcular rota");
      }
    } catch (error) {
      console.error("Erro:", error);
      alert("Erro ao contactar o servidor.");
    }
  };

  return (
    <div className="dashboard-container">
      <Sidebar className="sidebar" />
      <div className="dashboard-content">
        <h1>Escolha o seu destino</h1>

        <div className="input-container">
          <input
            className="form-control"
            type="text"
            placeholder="Ponto de Partida"
            value={pontoPartida}
            onChange={(e) => setPontoPartida(e.target.value)}
          />

          <input
            className="form-control"
            type="text"
            placeholder="Ponto de Chegada"
            value={pontoChegada}
            onChange={(e) => setPontoChegada(e.target.value)}
          />
        </div>

        <div className="dropdown">
          <button
            className="btn btn-secondary dropdown-toggle"
            type="button"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            {metodo || "Escolha um método"}
          </button>
          <ul className="dropdown-menu">
            <li><button className="dropdown-item" onClick={() => setMetodo("custo_uniforme")}>Custo Uniforme</button></li>
            <li><button className="dropdown-item" onClick={() => setMetodo("aprofundamento")}>Aprofundamento Progressivo</button></li>
            <li><button className="dropdown-item" onClick={() => setMetodo("sofrega")}>Procura Sôfrega</button></li>
            <li><button className="dropdown-item" onClick={() => setMetodo("a_estrela")}>A*</button></li>
          </ul>
        </div>

        <button className="btn btn-primary mt-3" onClick={handleCalcularRota}>
          Calcular Rota
        </button>

        <MapComponent />
      </div>
    </div>
  );
}

export default Dashboard;
