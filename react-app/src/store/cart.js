const ADD_ITEM = "cart/ADD_ITEM";
const REMOVE_ITEM = "cart/REMOVE_ITEM";
const UPDATE_COUNT = "cart/UPDATE_COUNT";
const RESET = "cart/RESET";

/* ----- ACTIONS ------ */

export const addItem = (productId) => {
  return {
    type: ADD_ITEM,
    productId,
  };
};

export const updateCount = (productId, count) => {
  if (count < 1) return removeItem(productId);
  return {
    type: UPDATE_COUNT,
    productId,
    count,
  };
};

export const removeItem = (productId) => {
  return {
    type: REMOVE_ITEM,
    productId,
  };
};

export const reset = () => {
  return {
    type: RESET,
  };
};


const initialState = {};

export default function cartReducer(state = initialState, action) {
  switch (action.type) {
    case ADD_ITEM:
      return {
        ...state,
        [action.productId]: {
            id: action.productId,
            count: 1,
        }
      };
    case UPDATE_COUNT:
      return {
        ...state,
        [action.productId]: {
        ...state[action.productId],
        count: action.count,
        }
      };
    case REMOVE_ITEM:
      const newState = { ...state};
      delete newState[action.productId];
      return newState;
    case RESET:
      return initialState;
    default:
      return state;
  }
}