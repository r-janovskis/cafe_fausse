import { StrictMode } from "react";
import ReactDOM, { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.jsx";
import { BrowserRouter } from "react-router-dom";

// Import bootstrap library for styling
import "bootstrap/dist/css/bootstrap.min.css";
// Import bootstrap JS for interactivity
import "bootstrap/dist/js/bootstrap.bundle.min.js";

const root = createRoot(document.getElementById("root")).render(
  <StrictMode>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>
);
