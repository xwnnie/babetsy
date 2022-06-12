const SET_ITEMS = "cart/SET_ITEMS";
const ADD_ITEM = "cart/ADD_ITEM";
const REMOVE_ITEM = "cart/REMOVE_ITEM";
const UPDATE_QUANTITY = "cart/UPDATE_QUANTITY";
const RESET = "cart/RESET";

/* ----- ACTIONS ------ */

export const setCartItems = (items) => {
  return {
    type: SET_ITEMS,
    items,
  };
};

const addItem = (item) => {
  return {
    type: ADD_ITEM,
    item,
  };
};

const updateQuantity = (buyerId, productId, quantity) => {
  if (quantity < 1) return removeCartItem(buyerId, productId);
  return {
    type: UPDATE_QUANTITY,
    productId,
    quantity,
  };
};

const removeItem = (productId) => {
  return {
    type: REMOVE_ITEM,
    productId,
  };
};

const reset = () => {
  return {
    type: RESET,
  };
};


export const addCartItem = (payload) => async (dispatch) => {
  const response = await fetch(`/api/cart`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(addItem(data));
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

export const updateCartItemQuantity = (payload) => async (dispatch) => {
  const response = await fetch(`/api/cart/${payload.buyer_id}/${payload.product_id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(updateQuantity(data.buyer_id, data.product_id, data.quantity));
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

export const removeCartItem = (buyerId, productId) => async (dispatch) => {
  const response = await fetch(`/api/cart/${buyerId}/${productId}`, {
    method: "DELETE",
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(removeItem(productId));
    return data;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data;
    }
  } else {
    return ["An error occurred. Please try again."];
  }
};


export const clearCartItems = (buyerId) => async (dispatch) => {
  const response = await fetch(`/api/cart/${buyerId}/clear`, {
    method: "DELETE",
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(reset());
    return data;
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

export default function cartReducer(state = initialState, action) {
  switch (action.type) {
    case SET_ITEMS:
      return {
        ...state,
        ...action.items
      }
    case ADD_ITEM:
      return {
        ...state,
        [action.item.product_id]: action.item,
      };
    case UPDATE_QUANTITY:
      return {
        ...state,
        [action.productId]: {
          ...state[action.productId],
          quantity: action.quantity,
        },
      };
    case REMOVE_ITEM:
      const newState = { ...state };
      delete newState[action.productId];
      return newState;
    case RESET:
      return initialState;
    default:
      return state;
  }
}
