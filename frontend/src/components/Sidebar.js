import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Home, History, LogOut } from "lucide-react"; // Ícones modernos

function Sidebar() {
  const [expanded, setExpanded] = useState(false);
  const navigate = useNavigate();

  const handleLogout = () => {
    navigate("/");
  };

  return (
    <div
      className="sidebar bg-primary text-white d-flex flex-column align-items-center p-3"
      style={{
        width: expanded ? "10%" : "4%",
        height: "100vh",
        position: "fixed",
        left: 0,
        top: 0,
        transition: "width 0.3s ease",
      }}
      onMouseEnter={() => setExpanded(true)}
      onMouseLeave={() => setExpanded(false)}
    >
      <div className="mt-3 text-center w-100" onClick={() => navigate("/dashboard")}>
        <Home size={30} className="mb-3 cursor-pointer" />
        {expanded && <p>Dashboard</p>}
      </div>
      <div className="mt-4 text-center w-100" onClick={() => navigate("/history")}>
        <History size={30} className="mb-3 cursor-pointer" />
        {expanded && <p>Histórico</p>}
      </div>
      <div className="mt-auto text-center w-100" onClick={handleLogout}>
        <LogOut size={30} className="mb-3 cursor-pointer text-danger" />
        {expanded && <p className="text-danger">Sair</p>}
      </div>
    </div>
  );
}

export default Sidebar;
