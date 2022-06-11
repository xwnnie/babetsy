import { useSelector } from "react-redux";
import { Link } from "react-router-dom";

import CancelOrderBtn from "./CancelOrderBtn";
import EditAddressBtn from "../EditAddress";
import AccountSideBar from "../AccountSideBar";

import "./index.css";

const OrderHistory = () => {
  let orders = useSelector((state) => state.orders);
  orders = Object.values(orders);
  let products = useSelector((state) => state.products);
  let purchases;

  orders.sort((a, b) => {
    const keyA = new Date(a[0]?.created_at);
    const keyB = new Date(b[0]?.created_at);
    return keyA > keyB ? -1 : 1;
  });

  return (
    <div>
      <AccountSideBar />
      <div className="account-container">
        <div id="note">
          Note: After placed, orders can be updated or
          canceled for the first one hour. Please contact customer service for any further questions.
        </div>
        {orders.map((order) => {
          purchases = Object.values(order);
          let date = new Date(purchases[0].created_at);
          return (
            <div
              key={purchases[0].order_number}
              className="single-order-container"
            >
              <div>{purchases[0].order_number}</div>
              <div className="order-placed-date">{date.toDateString()}</div>
              {new Date() - new Date(purchases[0].created_at) < 3600000 ? (
                <CancelOrderBtn orderNumber={purchases[0].order_number} />
              ) : null}
              {new Date() - new Date(purchases[0].created_at) < 3600000 ? (
                <EditAddressBtn />
              ) : null}
              {/* <div>Order detail:</div> */}

              <table className="order-table">
                <thead>
                  <tr className="order-table-header">
                    <th>ITEM</th>
                    <th>PRICE</th>
                    <th>QUANTITY</th>
                    <th></th>
                  </tr>
                </thead>
                <tbody>
                  {purchases.map((item) => (
                    <tr key={item.product_id} className="order-item-row">
                      <Link to={`/products/${item.product_id}`}>
                        <td>{products[item?.product_id]?.name}</td>
                      </Link>
                      <td>${products[item?.product_id]?.price}</td>
                      <td>{item.quantity}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
              <div>
                <div>Shipping Address</div>
                <div>{purchases[0].full_name}</div>
                <div>{purchases[0].phone}</div>
                <div>{purchases[0].address}</div>
              </div>
              {/* <hr /> */}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default OrderHistory;
