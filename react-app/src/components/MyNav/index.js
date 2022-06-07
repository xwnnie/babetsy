import React from "react";
import { Link } from "react-router-dom";
import { useSelector } from "react-redux";

import LogoutButton from "../auth/LogoutButton";
// import "./index.css";

const MyNav = () => {
  const cartItems = useSelector(state => state.cart);
  let cartItemsCount = 0;

  for (let value of Object.values(cartItems)) {
    cartItemsCount += value.count
  }

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
          Shopping bag({cartItemsCount})
        </Link>
        <LogoutButton />
      </div>
    </nav>
  );
};

export default MyNav;
