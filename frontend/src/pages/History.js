import React, { useState, useEffect } from "react";
import axios from "axios";
import "./styles/History.css";
import Sidebar from "../components/Sidebar";

function History() {
  const [viagens, setViagens] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchViagens = async () => {
      try {
        const userId = localStorage.getItem("userId");
        const response = await axios.get("http://127.0.0.1:8000/api/listar_viagens/", {
          params: { user_id: userId },
        });
        setViagens(response.data.viagens);
        setLoading(false);
      } catch (error) {
        console.error("Erro ao buscar as viagens:", error);
        setError("Erro ao carregar o histórico de viagens. Tente novamente mais tarde.");
        setLoading(false);
      }
    };

    fetchViagens();
  }, []);

  if (loading) {
    return <div className="loading">Carregando histórico de viagens...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div className="history-page">
      <Sidebar />
      <div className="history-content">
        <h1>Histórico de Viagens</h1>
        {viagens.length > 0 ? (
          <div className="viagens-list">
            {viagens.map((viagem) => (
              <div key={viagem.id} className="viagem-card">
                <h2>{viagem.partida} → {viagem.chegada}</h2>
                <p><strong>Data:</strong> {viagem.data_partida}</p>
                <p>
                  <strong>Método:</strong>{" "}
                  {viagem.metodo ? viagem.metodo.replace("_", " ").toUpperCase() : "Desconhecido"}
                </p>
                <p><strong>Distância:</strong> {viagem.distancia} km</p>
                <p><strong>Nós Explorados:</strong> {viagem.nos_expandidos}</p>
                <p>
                  <strong>Caminho:</strong>{" "}
                  {Array.isArray(viagem.caminho) ? viagem.caminho.join(" → ") : "Caminho não disponível"}
                </p>
              </div>
            ))}
          </div>
        ) : (
          <p className="no-viagens">Nenhuma viagem encontrada.</p>
        )}
      </div>
    </div>
  );
}

export default History;