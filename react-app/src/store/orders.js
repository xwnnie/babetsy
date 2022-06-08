const SET_ORDERS = "projects/SET_ORDERS";
const CREATE_ORDER = "projects/CREATE_ORDER";
const REMOVE_ORDER = "project/REMOVE_ORDER";

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


export const cancelOrder = (orderNumber) => async (dispatch) => {
  const response = await fetch(`/api/order/${orderNumber}`, {
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
    case CREATE_ORDER:
      return {
        ...state,
        [action.orderNumber]: action.order,
      };
    case REMOVE_ORDER:
      let newState = { ...state };
      delete newState[action.orderNumber];
      return newState;
    default:
      return state;
  }
};

export default orderReducer;
