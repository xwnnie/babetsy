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
  const sessionUser = useSelector(state => state.session.user);

  let cartItems = useSelector((state) => state.cart);
  cartItems = Object.values(cartItems);
  cartItems = cartItems.map((item) => ({
    ...item,
    name: products[item.id]?.name,
  }));
  //   console.log("******", cartItems);

  if (!cartItems || !cartItems.length)
    return (
      <div className="cart">
        No items in the cart. Start selecting items to purchase.
      </div>
    );

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

    let createdAt = new Date()

    const payload = {
      buyer_id: sessionUser.id,
      products: cartItems,
      order_number: `ORDER_${orderNumber}`,
      created_at: createdAt.toString()
    }
    console.log("********", payload)
    dispatch(reset());
    dispatch(addOrder(payload))
    history.push("/my-account")
  };

  return (
    <div className="cart">
      <ul>
        {cartItems.map((item) => (
          <CartItem key={item.id} item={item} />
        ))}
      </ul>
      <hr />
      <form onSubmit={onSubmit}>
        <button type="submit">Purchase</button>
      </form>
    </div>
  );
}

export default Cart;
