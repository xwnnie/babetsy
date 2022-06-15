import React, { useState } from "react";
import { useHistory } from "react-router-dom";

import ReactTooltip from "react-tooltip";

import "./index.css";

const Search = () => {
  const history = useHistory();
  const [searchQuery, setSearchQuery] = useState("");
  const [tipMsg, setTipMsg] = useState(true);
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (searchQuery && searchQuery.trim()) {
        setTipMsg(false);
        history.push(`/search/${searchQuery}`);
        setSearchQuery("");        
    }
  };
  return (
    <form id="nav-search" onSubmit={handleSubmit}>
      <input
        type="text"
        value={searchQuery}
        onChange={(e) => {setSearchQuery(e.target.value); setTipMsg(false)}}
        placeholder="Search products"
      />

      <button type="submit" data-tip={tipMsg ? "Search can't be empty" : null}>
        <span className="material-symbols-outlined">search</span>
      </button>
      <ReactTooltip place="bottom" type="light" effect="solid" />
    </form>
  );
};

export default Search;
