import { useSelector } from "react-redux";

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
          return (
            <div key={purchases[0].order_number} className="single-order-container">
              <div>{purchases[0].order_number}</div>
              <div>placed on: {purchases[0].created_at}</div>
              {new Date() - new Date(purchases[0].created_at) < 3600000 ? (
                <CancelOrderBtn orderNumber={purchases[0].order_number} />
              ) : null}
              {new Date() - new Date(purchases[0].created_at) < 3600000 ? (
                <EditAddressBtn />
              ) : null}
              <div>Items:</div>
              {purchases.map((item) => (
                <div key={item.product_id}>
                  <div>name: {products[item?.product_id]?.name}</div>
                  <div>product id: {item.product_id}</div>
                  <div>quantity: {item.quantity}</div>
                </div>
              ))}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default OrderHistory;
