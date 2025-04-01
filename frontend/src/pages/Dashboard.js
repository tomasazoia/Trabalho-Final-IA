import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./styles/Dashboard.css"; 
import Sidebar from "../components/Sidebar"; 
import MapComponent from "../components/mapComponent";

function Dashboard() {
  const navigate = useNavigate(); 
  const [pontoPartida, setPontoPartida] = useState("");
  const [pontoChegada, setPontoChegada] = useState("");
  const [algoritmos, setAlgoritmos] = useState({
    custoUniforme: false,
    aprofundamento: false,
    procuraSofrega: false,
    aEstrela: false
  });

  const handleCheckboxChange = (e) => {
    const { name, checked } = e.target;
    setAlgoritmos((prev) => ({ ...prev, [name]: checked }));
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

        <div className="checkbox-container">
          <label>
            <input 
              type="checkbox" 
              name="custoUniforme" 
              checked={algoritmos.custoUniforme} 
              onChange={handleCheckboxChange} 
            />
            Custo Uniforme
          </label>

          <label>
            <input 
              type="checkbox" 
              name="aprofundamento" 
              checked={algoritmos.aprofundamento} 
              onChange={handleCheckboxChange} 
            />
            Aprofundamento Progressivo
          </label>

          <label>
            <input 
              type="checkbox" 
              name="procuraSofrega" 
              checked={algoritmos.procuraSofrega} 
              onChange={handleCheckboxChange} 
            />
            Procura Sôfrega (Faro)
          </label>

          <label>
            <input 
              type="checkbox" 
              name="aEstrela" 
              checked={algoritmos.aEstrela} 
              onChange={handleCheckboxChange} 
            />
            A* (Faro)
          </label>
        </div>
        <MapComponent /> 
      </div>
    </div>
  );
}

export default Dashboard;
