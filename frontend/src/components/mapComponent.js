import React from "react";
import { MapContainer, TileLayer, Marker } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";

// Ícone personalizado (corrige problema com ícones do Leaflet no React)
const customIcon = new L.Icon({
  iconUrl: "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41]
});

const MapComponent = () => {
  const position = [40.6575, -7.91428]; // Posição inicial (Lisboa)

  return (
    <MapContainer center={position} zoom={10} style={{ height: "60%", width: "80%", borderRadius: "12px", marginTop: "5%", marginLeft: "10%" }}>
      <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        <Marker position={position} icon={customIcon} />
    </MapContainer>
  );
};

export default MapComponent;
