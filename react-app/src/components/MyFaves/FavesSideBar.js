import React from "react";
import { NavLink, useHistory } from "react-router-dom";

import "./index.css";

const FavesSideBar = () => {
  const categories = [
    { id: 1, name: "Clothing" },
    { id: 7, name: "Accessories" },
    { id: 2, name: "Furniture" },
    { id: 3, name: "Bedding" },
    { id: 4, name: "Bath" },
    { id: 5, name: "Decor" },
    { id: 6, name: "Toys" },
  ];

  return (
    <div className="sidebar-container fave-sidebar">
      <div className="sidebar-menu main">
        <div className="sidebar-menu-item sidebar-header">Categories</div>
        <div className="sidebar-menu-item">
          <NavLink
            to={`/my-favorites`}
            exact={true}
            activeClassName="selected"
          >
            All favorites
          </NavLink>
        </div>
        {categories.map((category) => (
          <div className="sidebar-menu-item">
            <NavLink
              to={`/my-favorites/${category.name.toLowerCase()}`}
              exact={true}
              activeClassName="selected"
              key={category.id}
            >
              {category.name}
            </NavLink>
          </div>
        ))}
      </div>
    </div>
  );
};

export default FavesSideBar;
