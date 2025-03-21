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
    <div>
      <h2>Capturar Imagem</h2>
      <Webcam ref={webcamRef} screenshotFormat="image/jpeg" />
      <button onClick={capture}>Capturar</button>
      {image && <img src={image} alt="Captura" style={{ width: "300px" }} />}
    </div>
  );
};

export default WebcamCapture;
