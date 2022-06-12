import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";

import { updateCartItemQuantity, removeCartItem } from "../../store/cart";

function CartItem({ item }) {
  const dispatch = useDispatch();
  const sessionUser = useSelector(state => state.session.user);
  const [quantity, setQuantity] = useState(item.quantity);


  useEffect(() => {
    setQuantity(item.quantity);
  }, [item.quantity]);

  return (
    <div className="cart-item">
      <Link to={`/products/${item.product_id}`}>
        <img src={item.image_url} alt={item.name} className="cart-img" />
      </Link>
      <div>
        <Link to={`/products/${item.product_id}`}>
          <div className="cart-item-header">{item.name}</div>
        </Link>
        <div className="cart-item-price">${item.price}</div>
        <div className="cart-item-menu">
          <input
            type="number"
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
            onBlur={() =>
              dispatch(
                updateCartItemQuantity({
                  buyer_id: sessionUser.id,
                  product_id: item.product_id,
                  quantity: Number(quantity),
                })
              )
            }
          />
          <button
            className="cart-item-button"
            onClick={() =>
              dispatch(
                updateCartItemQuantity({
                  buyer_id: sessionUser.id,
                  product_id: item.product_id,
                  quantity: item.quantity - 1,
                })
              )
            }
          >
            <span className="material-symbols-outlined">remove</span>
          </button>
          <button
            className="cart-item-button"
            onClick={() =>
              dispatch(
                updateCartItemQuantity({
                  buyer_id: sessionUser.id,
                  product_id: item.product_id,
                  quantity: item.quantity + 1,
                })
              )
            }
          >
            <span className="material-symbols-outlined">add</span>
          </button>
          <button
            className="cart-item-button"
            onClick={() =>
              dispatch(removeCartItem(sessionUser.id, item.product_id))
            }
          >
            <span className="material-symbols-outlined">delete</span>
          </button>
        </div>
      </div>
    </div>
  );
}

export default CartItem;
