const SET_REVIEWS = "products/SET_REVIEWS";
const CREATE_REVIEW = "products/CREATE_REVIEW";
const EDIT_REVIEW = "products/EDIT_REVIEW";
const REMOVE_REVIEW = "products/REMOVE_REVIEW";

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

export const editReview = (review) => {
  return {
    type: EDIT_REVIEW,
    review,
  };
};

export const removeReview = (reviewId) => {
  return {
    type: REMOVE_REVIEW,
    reviewId,
  };
};

export const loadReviews = () => async (dispatch) => {
  const response = await fetch(`/api/reviews`);

  if (response.ok) {
    const reviews = await response.json();
    dispatch(setReviews(reviews));
    return null
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

export const updateReview = (payload, reviewId) => async (dispatch) => {
  const response = await fetch(`/api/reviews/${reviewId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(editReview(data));
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ["An error occurred. Please try again."];
  }
};

export const deleteReview = (reviewId) => async (dispatch) => {
  const response = await fetch(`/api/reviews/${reviewId}`, {
    method: "DELETE",
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(removeReview(reviewId));
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
    case EDIT_REVIEW:
      return {
        ...state,
        [action.review.id]: action.review,
      };
    case REMOVE_REVIEW:
      let newState = { ...state };
      delete newState[action.reviewId];
      return newState;
    default:
      return state;
  }
};
export default reviewReducer;
