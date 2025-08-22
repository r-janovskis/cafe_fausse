import React from "react";
import { Link, NavLink } from "react-router-dom";

import "./Header.css";

function Header() {
  return (
    <header>
      {/* <nav> is built using bootstrap navbar scaffoldings. All the included classes are meant to be make it responsive */}
      <nav className="navbar navbar-expand-md">
        <div className="container-fluid">
          <Link to="/" className="navbar-brand">
            <img src="./src/assets/cafe_fausse.jpg" alt="Café Fausse logo" />
          </Link>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNavAltMarkup"
            aria-controls="navbarNavAltMarkup"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div className="navbar-nav">
              <NavLink to="/" className="nav-link">
                Home
              </NavLink>

              <NavLink to="/menu" className="nav-link">
                Menu
              </NavLink>

              <NavLink to="/reservation" className="nav-link">
                Reservation
              </NavLink>

              <NavLink to="/gallery" className="nav-link">
                Gallery
              </NavLink>

              <NavLink to="/about" className="nav-link">
                About Us
              </NavLink>
            </div>
          </div>
        </div>
      </nav>
    </header>
  );
}

export default Header;
