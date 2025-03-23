import React, { useState } from "react";
import axios from "axios";

const UploadImage = ({ image }) => {
  const [result, setResult] = useState("");
  const [plateText, setPlateText] = useState("");

  const handleUpload = async () => {
    if (!image) return alert("Capture uma imagem primeiro!");

    const blob = await fetch(image).then(res => res.blob());
    const formData = new FormData();
    formData.append("image", blob, "placa.jpg");

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/upload/", formData);

      if (response.data.placa_texto) {
        setPlateText(`Texto detectado: ${response.data.placa_texto}`);
      } else {
        setResult("Nenhuma matrícula detectada.");
        setPlateText("");
      }

    } catch (error) {
      setResult("Erro ao processar a imagem.");
      setPlateText("");
    }
  };

  return (
    <div>
      <h2>Upload da Imagem</h2>
      <button onClick={handleUpload}>Enviar para Reconhecimento</button>
      {result && <h3>{result}</h3>}
      {plateText && <h3>{plateText}</h3>}
    </div>
  );
};

export default UploadImage;
