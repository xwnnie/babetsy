import { useHistory, useParams } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";

import { addItem, updateQuantity } from "../../store/cart";

import ShowReviewsBtn from "../Reviews";

import "./index.css";

const SingleProduct = () => {
    const dispatch = useDispatch();
    const history = useHistory();
  const { productId } = useParams();
  const product = useSelector((state) => state.products[productId]);
  let reviews;
  if (product?.reviews) reviews = Object.values(product?.reviews);
  let cartItem = useSelector((state) => state.cart[productId]);
  const sessionUser = useSelector((state) => state.session.user);
  const addToCart = () => {
    if (!sessionUser) {
      alert("login to use this feature. redirecting... ");
      history.push("/login")
      return
    }
    if (cartItem) {
        return dispatch(updateQuantity(product.id, cartItem.quantity + 1));
    };
    dispatch(addItem(product.id));
  };

  return (
    <div className="single-product-container">
      <img
        src={product?.image_url}
        alt={product?.name}
        className="single-product-img"
      />
      <div className="single-product-info">
        <div>{product?.name}</div>
        <div>${product?.price}</div>
        <div className="fave-heart">
          <span class="material-symbols-outlined">favorite</span>
        </div>
        <button
          className={"plus-button" + (cartItem ? " selected" : "")}
          onClick={addToCart}
        >
          <i className="fa-solid fa-bag-shopping" /> Add to Bag
        </button>
        <ShowReviewsBtn reviewsCount={reviews?.length} reviews={reviews} />
        <div>{product?.description}</div>
      </div>
    </div>
  );
};

export default SingleProduct;
