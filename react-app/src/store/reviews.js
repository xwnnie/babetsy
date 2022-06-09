const SET_REVIEWS = "products/SET_REVIEWS";

export const setReviews = (reviews) => {
  return {
    type: SET_REVIEWS,
    reviews,
  };
};

export const loadReviews = () => async (dispatch) => {
  const response = await fetch(`/api/reviews`);

  if (response.ok) {
    const reviews = await response.json();
    dispatch(setReviews(reviews));
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ["An error occurred. Please try again."];
  }
};

const initialState = {};

const reviewReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_PRODUCTS:
      return { ...state, ...action.reviews };
    default:
      return state;
  }
};
export default reviewReducer;
