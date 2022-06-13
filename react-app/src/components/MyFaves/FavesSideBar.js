import React from "react";
import { NavLink, useHistory } from "react-router-dom";

import "./index.css";

const FavesSideBar = () => {
  const categories = [
    { id: 1, name: "Clothing" },
    { id: 2, name: "Furniture" },
    { id: 3, name: "Bedding" },
    { id: 4, name: "Bath" },
    { id: 5, name: "Decor" },
    { id: 6, name: "Toys" },
  ];

  return (
    <div className="sidebar-container">
      <div className="sidebar-menu main">
        <div className="sidebar-menu-item sidebar-header">Categories</div>
        <div className="sidebar-menu-item">
          {categories.map((category) => (
            <NavLink
              to={`/my-favorites/${category.name.toLowerCase()}`}
              exact={true}
              activeClassName="selected"
              key={category.id}
            >
              {category.name}
            </NavLink>
          ))}
        </div>
      </div>
    </div>
  );
};

export default FavesSideBar;
