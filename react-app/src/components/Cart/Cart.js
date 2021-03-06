import { useSelector} from "react-redux";
import { useHistory } from "react-router-dom";

import CartItem from "./CartItem";
import "./Cart.css";

function Cart() {
  const history = useHistory();

  const products = useSelector((state) => state.products);

  let cartItems = useSelector((state) => state.cart);
  cartItems = Object.values(cartItems);
  cartItems = cartItems.map((item) => ({
    ...item,
    price: products[item.product_id]?.price,
    name: products[item.product_id]?.name,
    image_url: products[item.product_id]?.image_url,
  }));

  let value = cartItems.reduce(
    (accu, item) => accu + item.quantity * item.price,
    0
  );
  value = Math.round(value * 100) / 100;
  let shipping = value > 25 ? 0 : 9.99;
  let total = Math.round((value + shipping) * 100) / 100;

  const onSubmit = (e) => {
    e.preventDefault();
    history.push("/checkout");
  };

  return (
    <div>
      <div className="cart-header">Shopping Bag</div>
      <div className="cart">
        <div className="cart-container">
          {!cartItems || !cartItems.length ? (
            <div className="cart-no-items-msg">Your shopping bag is empty!</div>
          ) : (
            <div className="cart-items-list">
              {cartItems.map((item) => (
                <CartItem key={item.product_id} item={item} />
              ))}
            </div>
          )}
          <div className="order-review">
            <div className="order-review-line">
              <span>Order Value:</span> <span>${value}</span>
            </div>
            <div className="order-review-line">
              <span>Shipping:</span>{" "}
              <span>{shipping === 0 ? "Free" : "$9.99"}</span>
            </div>
            <hr />
            <div className="order-review-line">
              <span>Total: </span>
              <span>${total}</span>
            </div>
            <button
              onClick={!cartItems || !cartItems.length ? null : onSubmit}
              className={`checkout-btn ${
                !cartItems || !cartItems.length ? "no-item" : null
              }`}
            >
              <span>Continue to checkout</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Cart;
