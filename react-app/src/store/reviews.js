const SET_REVIEWS = "products/SET_REVIEWS";
const CREATE_REVIEW = "projects/CREATE_REVIEW";

export const setReviews = (reviews) => {
  return {
    type: SET_REVIEWS,
    reviews,
  };
};

export const createReview = (review) => {
  return {
    type: CREATE_REVIEW,
    review,
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

export const addReview = (payload) => async (dispatch) => {
  const response = await fetch(`/api/reviews`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(createReview(data));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return "An error occurred. Please try again.";
  }
};

const initialState = {};

const reviewReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_REVIEWS:
      return { ...state, ...action.reviews };
    case CREATE_REVIEW:
      return {
        ...state,
        [action.review.id]: action.review,
      };
    default:
      return state;
  }
};
export default reviewReducer;
