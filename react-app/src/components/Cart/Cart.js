import { useSelector, useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { reset } from "../../store/cart";
import { addOrder } from "../../store/orders";

import CartItem from "./CartItem";
import "./Cart.css";

function Cart() {
  const dispatch = useDispatch();
  const history = useHistory();

  const products = useSelector((state) => state.products);
  const sessionUser = useSelector((state) => state.session.user);

  let cartItems = useSelector((state) => state.cart);
  cartItems = Object.values(cartItems);
  cartItems = cartItems.map((item) => ({
    ...item,
    price: products[item.id]?.price,
    name: products[item.id]?.name,
    image_url: products[item.id]?.image_url,
  }));
  //   console.log("******", cartItems);

  let value = cartItems.reduce(
    (accu, item) => accu + item.quantity * item.price,
    0
  );
  value = Math.round(value * 100) / 100;
  let shipping = value > 25 ? 0 : 9.99;

  // if (!cartItems || !cartItems.length)
  //   return (
  //     <div className="cart">
  //       No items in the cart. Start selecting items to purchase.
  //     </div>
  //   );

  // console.log("******", cartItems)

  const onSubmit = (e) => {
    e.preventDefault();
    window.alert(
      "Purchased the following:\n" +
        `${cartItems
          .map((item) => `${item.quantity} of ${item.name}`)
          .join("\n")}`
    );

    let orderNumber = Math.floor(
      Math.random(100000000000000, 999999999999999) * 1000000000000000
    );

    let createdAt = new Date();

    const payload = {
      buyer_id: sessionUser.id,
      products: cartItems,
      order_number: `ORDER_${orderNumber}`,
      created_at: createdAt.toString(),
    };
    console.log("********", payload);
    dispatch(reset());
    dispatch(addOrder(payload));
    history.push("/my-account");
  };

  return (
    <div className="cart">
      <div className="cart-header">Shopping Bag</div>
      <div className="cart-container">
        {!cartItems || !cartItems.length ? (
          <div className="cart">
            No items in the cart. Start selecting items to purchase.
          </div>
        ) : (
          <div className="cart-items-list">
            {cartItems.map((item) => (
              <CartItem key={item.id} item={item} />
            ))}
          </div>
        )}

        {/* <hr /> */}
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
            <span>{Math.round((value + shipping) * 100) / 100}</span>
          </div>
          <button onClick={onSubmit} className="checkout-btn">
            Continue to checkout
          </button>
        </div>
      </div>
    </div>
  );
}

export default Cart;
