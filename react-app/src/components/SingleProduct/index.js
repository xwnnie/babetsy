import { useHistory, useParams } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import ReactTooltip from "react-tooltip";

import { addCartItem, updateCartItemQuantity} from "../../store/cart";

import ShowReviewsBtn from "../Reviews";
import FaveHeart from "../FaveHeart";

import "./index.css";

const SingleProduct = () => {
  const dispatch = useDispatch();
  const history = useHistory();
  const { productId } = useParams();
  const product = useSelector((state) => state.products[productId]);

  let reviews = useSelector((state) => state.reviews);
  reviews = Object.values(reviews);
  reviews = reviews.filter(review => review.product_id === parseInt(productId));

  let cartItem = useSelector((state) => state.cart[productId]);
  const sessionUser = useSelector((state) => state.session.user);
  const addToCart = () => {
    if (!sessionUser) {
      // alert("login to use this feature. redirecting... ");
      history.push("/login");
      return;
    }
    let payload;

    if (cartItem) {
      payload = {
        buyer_id: sessionUser.id,
        product_id: product.id,
        quantity: cartItem.quantity + 1,
      };
      return dispatch(updateCartItemQuantity(payload));
    }
    payload = {
      buyer_id: sessionUser.id,
      product_id: product.id,
      quantity: 1
    }
    dispatch(addCartItem(payload));
  };

  return (
    <div className="single-product-container">
      <img
        src={product?.image_url}
        alt={product?.name}
        className="single-product-img"
      />
      <div className="single-product-info">
        <FaveHeart productId={parseInt(productId)} />
        <div>{product?.name}</div>
        <div>${product?.price}</div>
        <div>{product?.quantity <= 0 ? "Out of Stock" : "In Stock"}</div>
        <button
          className={
            "add-to-bag-btn" + (cartItem?.quantity >= 5 || cartItem?.quantity >= product?.quantity ? " exceed-limit" : "")
          }
          onClick={cartItem?.quantity >= 5 || cartItem?.quantity >= product?.quantity ? null : addToCart}
          data-tip={
            !sessionUser
              ? "Log into your account to add items to your shopping bag"
              : cartItem?.quantity >= 5
              ? "Exceeds maximum quantity 5"
              : null
          }
        >
          <i className="fa-solid fa-bag-shopping" /> {" "}
          {cartItem?.quantity >= 5 ? "Limit 5 per purchase": cartItem?.quantity >= product?.quantity ? "Not enough inventory" : "Add to bag"}
        </button>
        <ReactTooltip place="bottom" effect="solid" />
        <ShowReviewsBtn reviewsCount={reviews?.length} reviews={reviews} />
        <div>{product?.description}</div>
      </div>
    </div>
  );
};

export default SingleProduct;
