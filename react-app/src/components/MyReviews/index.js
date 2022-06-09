import { useSelector } from "react-redux";

import AccountSideBar from "../AccountSideBar";

import "./index.css";

const MyReviews= () => {
  const sessionUser = useSelector((state) => state.session.user);
  let orders = useSelector((state) => state.orders);
  orders = Object.values(orders);
  console.log("***********", orders)
  let purchasedProducts = new Set();
  orders.forEach(order => {
    order.forEach(item => {
        purchasedProducts.add(item.product_id)
    })
  });
  console.log("!!!!!!!!!", purchasedProducts)

  return (
    <div>
      <AccountSideBar />
      <div className="account-container">
        <div>
          <div>Reviews on purchased items</div>
        </div>

        {/* <OrderHistory /> */}
      </div>
    </div>
  );
};

export default MyReviews;
