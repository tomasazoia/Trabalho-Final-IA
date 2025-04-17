import React, { useState } from "react";
import axios from "axios";
import "./styles/Dashboard.css";
import Sidebar from "../components/Sidebar";

function Dashboard() {
  const [inicio, setInicio] = useState("");
  const [destino, setDestino] = useState("");
  const [metodo, setMetodo] = useState("custo_uniforme");
  const [resultado, setResultado] = useState(null);

  const distritos = [
    "Aveiro", "Beja", "Braga", "Bragança", "Castelo Branco", "Coimbra", "Évora",
    "Faro", "Guarda", "Leiria", "Lisboa", "Portalegre", "Porto", "Santarém",
    "Setúbal", "Viana do Castelo", "Vila Real", "Viseu"
  ];

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!inicio || !destino) {
      alert("Por favor, selecione o ponto de partida e o destino.");
      return;
    }

    try {
      const userId = localStorage.getItem("userId"); // Recupera o ID do usuário logado

      const response = await axios.get("http://127.0.0.1:8000/api/calcular_caminho/", {
        params: { metodo, inicio, destino,  user_id: userId },
      });

      setResultado(response.data);
    } catch (error) {
      console.error("Erro ao calcular o caminho:", error);
      alert("Erro ao calcular o caminho. Verifique os dados e tente novamente.");
    }
  };

  return (
    <div className="dashboard-container">
      <Sidebar />
      <div className="dashboard-content">
        <h1>Calcular Rotas</h1>
        <form onSubmit={handleSubmit} className="form-container">
          <select
            value={inicio}
            onChange={(e) => setInicio(e.target.value)}
            required
          >
            <option value="" disabled>
              Selecione o Ponto de Partida
            </option>
            {distritos.map((distrito) => (
              <option key={distrito} value={distrito}>
                {distrito}
              </option>
            ))}
          </select>
          <select
            value={destino}
            onChange={(e) => setDestino(e.target.value)}
            required
          >
            <option value="" disabled>
              Selecione o Destino
            </option>
            {distritos.map((distrito) => (
              <option key={distrito} value={distrito}>
                {distrito}
              </option>
            ))}
          </select>
          <select value={metodo} onChange={(e) => setMetodo(e.target.value)}>
            <option value="custo_uniforme">Custo Uniforme</option>
            <option value="aprofundamento_progressivo">Aprofundamento Progressivo</option>
            <option value="procura_sofrega">Procura Sofrega</option>
            <option value="a_estrela">A*</option>
          </select>
          <button type="submit">Calcular</button>
        </form>

        {resultado && (
          <div className="resultado-container">
            <div className="resumo-box">
              {resultado && resultado.metodo && (
                <p><strong>Método:</strong> {resultado.metodo.replace("_", " ").toUpperCase()}</p>
              )}              
              <p><strong>Distância Total:</strong> {resultado.custo} km</p>
              <p><strong>Nós Explorados:</strong> {resultado.nos_explorados}</p>
            </div>

            <h3>Caminho Encontrado</h3>
            <div>
              {resultado.caminho.map((cidade, index) => (
                
                <div key={index} className="passo">
                  <div className="passo-numero">{index + 1}</div>
                  <div className="passo-info">
                    <strong>{cidade}</strong>
                    <div className="detalhes">
                      {index === 0 && "Cidade inicial"}
                      {index < resultado.caminho.length - 1 && (
                        <>
                          • Próxima cidade
                        </>
                      )}
                      {index === resultado.caminho.length - 1 && (
                        <>
                          • Cidade destino
                        </>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default Dashboard;