import React from "react";
import { Link } from "react-router-dom";

import LogoutButton from "../auth/LogoutButton";
// import "./index.css";

const MyNav = () => {
  return (
    <nav>
      <div>
        <Link to={`/my-account`} exact="true">
          My Account
        </Link>
        <Link to={`/favorites`} exact="true">
          Favorites
        </Link>
        <Link to={`/cart`} exact="true">
          Shopping bag
        </Link>
        <LogoutButton />
      </div>
    </nav>
  );
};

export default MyNav;
