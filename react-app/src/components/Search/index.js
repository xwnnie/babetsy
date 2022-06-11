import React, { useState } from "react";
import { NavLink, useHistory } from "react-router-dom";
import { useSelector } from "react-redux";

import "./index.css";

const Search = () => {
  const history = useHistory();
  const [searchQuery, setSearchQuery] = useState("");
  const handleSubmit = async (e) => {
    e.preventDefault();
    history.push(`/search/${searchQuery}`);
    setSearchQuery("");
  };
  return (
    <form id="nav-search" onSubmit={handleSubmit}>
      <input
        type="text"
        value={searchQuery}
        onChange={(e) => setSearchQuery(e.target.value)}
        placeholder="Search products"
      />
      <button type="submit">
        <span class="material-symbols-outlined">search</span>
      </button>
    </form>
  );
};

export default Search;
