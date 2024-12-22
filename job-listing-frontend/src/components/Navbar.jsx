import React from 'react';
import { NavLink } from 'react-router-dom';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      {/* Logo */}
      <div className="navbar-logo">
        <NavLink to="/">Job Portal</NavLink>
      </div>

      {/* Links */}
      <ul className="navbar-links">
        <li>
          <NavLink to="/" activeClassName="active" exact>
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/post-job" activeClassName="active">
            Post a Job
          </NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
