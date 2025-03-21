import React, { useState } from "react";
import WebcamCapture from "./components/WebCapture";
import UploadImage from "./components/UploadImage";

function App() {
  const [capturedImage, setCapturedImage] = useState(null);

  return (
    <div>
      <h1>Reconhecimento de Matrícula</h1>
      <WebcamCapture onCapture={setCapturedImage} />
      <UploadImage image={capturedImage} />
    </div>
  );
}

export default App;
