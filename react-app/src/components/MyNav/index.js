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
      <div className="dropdown">
        <Link to={`/my-account`} exact="true" className="dropbtn">
          My Account
        </Link>
        <div class="dropdown-content">
          <Link to={`/my-account`}>Settings</Link>
          <Link to={`/my-orders`}>Order History</Link>
          <Link to={`/my-reviews`}>Reviews</Link>
          {/* <Link to={`/my-reviews`}>
            <LogoutButton />
          </Link> */}
          <LogoutButton />
        </div>
      </div>
      <Link to={`/favorites`} exact="true">
        Favorites
      </Link>
      <Link to={`/cart`} exact="true">
        Shopping bag({cartItemsQuantity})
      </Link>
    </div>
  );
};

export default MyNav;
