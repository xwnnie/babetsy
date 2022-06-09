import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";

import { updateQuantity, removeItem } from "../../store/cart";

function CartItem({ item }) {
  const dispatch = useDispatch();
  const [quantity, setQuantity] = useState(item.quantity);

  useEffect(() => {
    setQuantity(item.quantity);
  }, [item.quantity]);

  return (
    <div className="cart-item">
      <img src={item.image_url} alt={item.name} className="cart-img" />
      <div>
        <div className="cart-item-header">{item.name}</div>
        <div className="cart-item-price">${item.price}</div>
        <div className="cart-item-menu">
          <input
            type="number"
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
            onBlur={() => dispatch(updateQuantity(item.id, Number(quantity)))}
          />
          <button
            className="cart-item-button"
            onClick={() => dispatch(updateQuantity(item.id, item.quantity - 1))}
          >
            <span class="material-symbols-outlined">remove</span>
          </button>
          <button
            className="cart-item-button"
            onClick={() => dispatch(updateQuantity(item.id, item.quantity + 1))}
          >
            <span class="material-symbols-outlined">add</span>
          </button>
          <button
            className="cart-item-button"
            onClick={() => dispatch(removeItem(item.id))}
          >
            <span class="material-symbols-outlined">delete</span>
          </button>
        </div>
      </div>
    </div>
  );
}

export default CartItem;
