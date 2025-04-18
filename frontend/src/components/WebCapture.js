import React, { useRef, useState } from "react";
import Webcam from "react-webcam";

const WebcamCapture = ({ onCapture }) => {
  const webcamRef = useRef(null);
  const [image, setImage] = useState(null);

  const capture = () => {
    const imageSrc = webcamRef.current.getScreenshot();
    setImage(imageSrc);
    onCapture(imageSrc);
  };

  return (
    <div style={{ textAlign: "center", padding: "10px" }}>
      <h2>Capturar Imagem</h2>
      <div>
        <Webcam
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          width={300}
          height={200}
          style={{ borderRadius: "10px", boxShadow: "0 4px 8px rgba(0,0,0,0.2)" }}
        />
      </div>
      <button onClick={capture} style={{ marginTop: "10px", padding: "8px 16px" }}>
        Capturar
      </button>
      {image && (
        <img
          src={image}
          alt="Captura"
          style={{ width: "200px", marginTop: "10px", borderRadius: "5px" }}
        />
      )}
    </div>
  );
};

export default WebcamCapture;
