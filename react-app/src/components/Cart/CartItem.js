import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";

import { updateCartItemQuantity, removeCartItem } from "../../store/cart";

function CartItem({ item }) {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [quantity, setQuantity] = useState(item.quantity);
  const product = useSelector((state) => state.products[item?.product_id]);
  // console.log("+++++++++++", product)

  let rangeQuantityValues;
  if (product?.quantity >= 0) {
    rangeQuantityValues = [...Array(Math.min(6, product?.quantity + 1)).keys()]
    rangeQuantityValues = rangeQuantityValues.slice(1);
  }
  
  // console.log("*******", rangeQuantityValues)


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
          <select
            value={quantity}
            onChange={(e) => {
              setQuantity(e.target.value);
              dispatch(
                updateCartItemQuantity({
                  buyer_id: sessionUser.id,
                  product_id: item.product_id,
                  quantity: Number(e.target.value),
                })
              );
            }}
          >
            {rangeQuantityValues?.map(value => (
              <option value={value} key={value}>{value}</option>
            ))}
            {/* <option value={1}>1</option>
            <option value={2}>2</option>
            <option value={3}>3</option>
            <option value={4}>4</option>
            <option value={5}>5</option> */}
          </select>
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
            className={
              "cart-item-button" + (item?.quantity >= 5 ? " exceed-limit" : "")
            }
            onClick={
              item?.quantity >= 5
                ? null
                : () =>
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
