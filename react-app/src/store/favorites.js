const SET_FAVORITES = "favorites/SET_FAVORITES";
const CREATE_FAVORITE = "favorites/CREATE_FAVORITE";
const REMOVE_FAVORITE = "favorites/REMOVE_FAVORITE";
const RESET_FAVORITES = "favorites/RESET_FAVORITES";

export const setFavorites = (productsArr) => ({
  type: SET_FAVORITES,
  productsArr,
});

const createFavorite = (productId) => ({
  type: CREATE_FAVORITE,
  productId,
});

const removeFavorite = (productId) => ({
  type: REMOVE_FAVORITE,
  productId,
});

export const resetFavorites = () => {
  return {
    type: RESET_FAVORITES,
  };
};


export const addFavorite = (userId, productId) => async (dispatch) => {
  const response = await fetch(
    `/api/users/${userId}/favorites/${productId}`,
    {
      method: "POST",
    }
  );

  if (response.ok) {
    const data = await response.json();
    dispatch(createFavorite(productId));
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return "An error occurred. Please try again.";
  }
};

export const unFavorite = (userId, productId) => async (dispatch) => {
  const response = await fetch(
    `/api/users/${userId}/favorites/${productId}`,
    {
      method: "DELETE",
    }
  );

  if (response.ok) {
    const data = await response.json();
    dispatch(removeFavorite(productId));
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data;
    }
  } else {
    return ["An error occurred. Please try again."];
  }
};

const initialState = [];

const favoriteReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_FAVORITES: 
        return [...state, ...action.productsArr]
    case CREATE_FAVORITE: 
        return [...state, action.productId]
    case REMOVE_FAVORITE: 
        return state.filter(productId => productId !== action.productId)
    case RESET_FAVORITES:
        return initialState
    default:
      return state;
  }
};
export default favoriteReducer;
