
import React from 'react';
import { NavLink } from 'react-router-dom';

const NavBar = () => {
  return (
    <div className="my-nav-container">
      <NavLink
        to="/"
        exact={true}
        activeClassName="active"
        className="nav-link-div"
      >
        Home
      </NavLink>
      <NavLink
        to="/login"
        exact={true}
        activeClassName="active"
        className="nav-link-div"
      >
        Login
      </NavLink>
      <NavLink
        to="/sign-up"
        exact={true}
        activeClassName="active"
        className="nav-link-div"
      >
        Sign Up
      </NavLink>
    </div>
  );
}

export default NavBar;
