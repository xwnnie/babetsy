import { useSelector, useDispatch } from "react-redux";
import { Link } from "react-router-dom";

import { addOrder } from "../../store/orders";
import { clearCartItems } from "../../store/cart";

import EditAddressBtn from "../EditAddress";
import CheckOutBtn from "./CheckOutButton";

import "./index.css";

function CheckOut() {
  const dispatch = useDispatch();

  const products = useSelector((state) => state.products);
  const sessionUser = useSelector((state) => state.session.user);

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

  const onSubmit = () => {
    let orderNumber = Math.floor(
      Math.random(1000000000000000, 999999999999999) * 1000000000000000
    );

    let createdAt = new Date();

    const payload = {
      buyer_id: sessionUser.id,
      products: cartItems,
      order_number: `ORDER_${orderNumber}`,
      created_at: createdAt.toString(),
      full_name: sessionUser.full_name,
      phone: sessionUser.phone,
      address: sessionUser.address,
      total,
    };
    // console.log("********", payload);
    dispatch(clearCartItems(sessionUser.id));
    dispatch(addOrder(payload));
  };

  return (
    <div>
      <div className="cart-header">Check Out</div>
      <Link to="/cart" className="back-to-cart-link">
        <span className="material-symbols-outlined">keyboard_backspace</span>
        <span className="back-to-cart-link-text">Back to shopping bag</span>
      </Link>
      <div className="cart">
        <div className="cart-container checkout">
          <div className="order-detail-container">
            <div className="order-detail-items">
                <div className="order-detail-header">Order Review </div>
                <div className="cart-items-list checkout-items">
                {cartItems.map((item) => (
                    <Link to={`/products/${item.product_id}`}>
                    <div key={item.product_id}>
                        <img
                        src={item.image_url}
                        className="checkout-img"
                        alt={item.name}
                        />
                        <div className="order-detail-name">
                        ${item.price} x {item.quantity}
                        </div>
                    </div>
                    </Link>
                ))}
                </div>                
            </div>

            <div className="checkout-shipping-container">
              <div className="checkout-shipping-header">Shipping Address</div>
              <div className="checkout-shipping-address">
                <div>{sessionUser?.full_name}</div>
                <div>{sessionUser?.phone}</div>
                <div>{sessionUser?.address}</div>
              </div>
              <EditAddressBtn />
            </div>
          </div>

          <div className="order-review checkout">
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
            <CheckOutBtn cartItems={cartItems} onSubmit={onSubmit} />
          </div>
        </div>
      </div>
    </div>
  );
}

export default CheckOut;
