import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";

import { addFavorite, unFavorite} from "../../store/favorites";

import "./index.css";

const FaveHeart = ({ productId }) => {
  const dispatch = useDispatch();

  const sessionUser = useSelector((state) => state.session.user);

  let favorites = useSelector((state) => state.favorites);
  let isFave = favorites.includes(productId) ? true : false;

  const handleCheckboxChange = async (checked) => {
    if (checked) {
      //   setFave(true);
      dispatch(addFavorite(sessionUser.id, productId));
    } else {
      //   setFave(false);
      dispatch(unFavorite(sessionUser.id, productId));
    }
  };

  return (
    <input
      className="heart"
      id="faves-page-heart"
      type="checkbox"
      name="addFave"
      checked={isFave}
      onChange={(e) => {
        handleCheckboxChange(e.target.checked);
      }}
    />
  );
};

export default FaveHeart;