import React from "react";
import { Link } from "react-router-dom";
import { useSelector } from "react-redux";

import LogoutButton from "../auth/LogoutButton";
import "./index.css";

const MyNav = () => {
  const cartItems = useSelector((state) => state.cart);
  let cartItemsQuantity = 0;

  for (let value of Object.values(cartItems)) {
    cartItemsQuantity += value.quantity;
  }

  return (
    <div className="my-nav-container">
      <Link to={`/my-account`} exact="true">
        My Account
      </Link>
      <Link to={`/favorites`} exact="true">
        Favorites
      </Link>
      <Link to={`/cart`} exact="true">
        Shopping bag({cartItemsQuantity})
      </Link>
      <LogoutButton />
    </div>
  );
};

export default MyNav;
