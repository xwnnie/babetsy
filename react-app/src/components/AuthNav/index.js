
import React from 'react';
import { NavLink } from 'react-router-dom';

const NavBar = () => {
  return (
    <nav>
          <NavLink to="/" exact={true} activeClassName="active">
            Home
          </NavLink>
          <NavLink to="/login" exact={true} activeClassName="active">
            Login
          </NavLink>
          <NavLink to="/sign-up" exact={true} activeClassName="active">
            Sign Up
          </NavLink>
    </nav>
  );
}

export default NavBar;
