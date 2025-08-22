import React from "react";
import { Link, NavLink } from "react-router-dom";

import "./Header.css";

function Header() {
  return (
    <header>
      <nav className="navbar bg-body-tertiary">
        <ul>
          <li>
            <NavLink to="/">Home</NavLink>
          </li>
          <li>
            <NavLink to="/menu">Menu</NavLink>
          </li>
          <li>
            <NavLink to="/reservation">Reservation</NavLink>
          </li>
          <li>
            <NavLink to="/gallery">Gallery</NavLink>
          </li>
          <li>
            <NavLink to="/about">About Us</NavLink>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;
