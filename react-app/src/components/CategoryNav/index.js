import React from "react";
import { NavLink, useHistory } from "react-router-dom";

import "./index.css";

const CategoryNav = () => {
  const categories = [
    { id: 1, name: "Clothing" },
    { id: 2, name: "Furniture" },
    { id: 3, name: "Bedding" },
    { id: 4, name: "Bath" },
    { id: 5, name: "Decor" },
    { id: 6, name: "Toys" },
  ];
  const history = useHistory();
  const handleOnClick = () => {
      history.push("/")
  }
  return (
    <nav className="logo-category-container">
      <div onClick={handleOnClick}>LOGO</div>
      <div className="category-nav">
        {categories.map((category) => (
            <NavLink
              to={`/${category.name.toLowerCase()}`}
              exact={true}
              activeClassName="active"
              key={category.id}
            >
              {category.name}
            </NavLink>
        ))}
      </div>
    </nav>
  );
};

export default CategoryNav;
