import { useParams } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";

import { addItem, updateCount } from "../../store/cart";

import "./index.css";

const SingleProduct = () => {
    const dispatch = useDispatch();
  const { productId } = useParams();
  const product = useSelector((state) => state.products[productId]);
  const reviews = Object.values(product?.reviews);
  let cartItem = useSelector((state) => state.cart[productId]);
  const addToCart = () => {
    if (cartItem) {
        return dispatch(updateCount(product.id, cartItem.count + 1))
    };
    dispatch(addItem(product.id));
  };

  return (
    <div className="single-product-container">
      <img
        src={product.image_url}
        alt={product.name}
        className="single-product-img"
      />
      <div className="single-product-info">
        <div>${product.price}</div>
        <div>{product.name}</div>
        <div>{product.description}</div>
        <div>favorite heart</div>
        <button
          className={"plus-button" + (cartItem ? " selected" : "")}
          onClick={addToCart}
        >
          <i className="fa-solid fa-bag-shopping" /> Add to Bag
        </button>
        <div>
          Reviews({reviews.length})
          {reviews.map((review) => (
            <div key={review.id}>
              <div>{review.content}</div>
              <div>{review.author_name}</div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default SingleProduct;
