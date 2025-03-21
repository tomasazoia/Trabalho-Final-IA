import React, { useState } from "react";
import axios from "axios";

const UploadImage = ({ image }) => {
  const [result, setResult] = useState("");

  const handleUpload = async () => {
    if (!image) return alert("Capture uma imagem primeiro!");

    const blob = await fetch(image).then(res => res.blob());
    const formData = new FormData();
    formData.append("image", blob, "placa.jpg");

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/upload/", formData);
      setResult(response.data.placa || "Placa não detectada");
    } catch (error) {
      setResult("Erro ao processar a imagem.");
    }
  };

  return (
    <div>
      <h2>Upload da Imagem</h2>
      <button onClick={handleUpload}>Enviar para Reconhecimento</button>
      {result && <h3>Resultado: {result}</h3>}
    </div>
  );
};

export default UploadImage;
