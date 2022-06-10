import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";

// import { getFaves, addFave, removeFave } from "../../store/faves.js";

import "./FaveStar.css";

const FaveStar = ({ photoId }) => {
  const dispatch = useDispatch();

  const sessionUser = useSelector((state) => state.session.user);

  let faves = useSelector((state) => state.faves);
  let isFave = faves[photoId] ? true : false;
  //   const [fave, setFave] = useState(isFave);

  useEffect(() => {
    dispatch(getFaves(sessionUser.id));
  }, [dispatch]);

  const handleCheckboxChange = async (checked) => {
    if (checked) {
      //   setFave(true);
      dispatch(addFave(sessionUser.id, photoId));
    } else {
      //   setFave(false);
      dispatch(removeFave(sessionUser.id, photoId));
    }
  };

  return (
    <input
      className="star"
      id="faves-page-star"
      type="checkbox"
      name="addFave"
      checked={isFave}
      onChange={(e) => {
        handleCheckboxChange(e.target.checked);
      }}
    />
  );
};

export default FaveStar;
