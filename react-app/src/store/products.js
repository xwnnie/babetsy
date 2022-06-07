const SET_PRODUCTS = "products/SET_PRODUCTS";

export const setProducts = (products) => {
  return {
    type: SET_PRODUCTS,
    products,
  };
};

export const loadProducts = () => async (dispatch) => {
    const response = await fetch(`/api/products`);

    if (response.ok) {
      const products = await response.json();
      dispatch(setProducts(products));
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

const productReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_PRODUCTS:
      return { ...state, ...action.products };
    default:
      return state;
  }
};
export default productReducer;
