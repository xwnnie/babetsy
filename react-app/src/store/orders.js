import { loadProducts } from "./products";
const SET_ORDERS = "products/SET_ORDERS";
const CREATE_ORDER = "products/CREATE_ORDER";
const REMOVE_ORDER = "products/REMOVE_ORDER";
const RESET_ORDERS = "products/RESET_ORDERS";

export const setOrders = (orders) => {
  return {
    type: SET_ORDERS,
    orders,
  };
};

export const createOrder = (order) => {
  return {
    type: CREATE_ORDER,
    order,
  };
};

export const removeOrder = (orderNumber) => {
  return {
    type: REMOVE_ORDER,
    orderNumber,
  };
};

export const resetOrders = () => {
  return {
    type: RESET_ORDERS,
  };
};

export const addOrder = (payload) => async (dispatch) => {
  const response = await fetch(`/api/orders`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(createOrder(data));
    dispatch(loadProducts());
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


export const cancelOrder = (orderNumber) => async (dispatch) => {
  const response = await fetch(`/api/orders/${orderNumber}`, {
    method: "DELETE",
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(removeOrder(orderNumber));
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

const orderReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_ORDERS:
      return {
        ...state,
        ...action.orders,
      };
    case CREATE_ORDER:{
      let newState = {...state};
      newState = Object.assign(action.order, newState);
      return newState
    }
      // return {
      //   ...state,
      //   [action.order[0].order_number]: action.order,
      // };
    case REMOVE_ORDER:{
      let newState = { ...state };
      delete newState[action.orderNumber];
      return newState;
    }
    case RESET_ORDERS:
      return initialState
    default:
      return state;
  }
};

export default orderReducer;
