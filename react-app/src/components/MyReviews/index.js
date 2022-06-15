import { useSelector } from "react-redux";

import AccountSideBar from "../AccountSideBar";
import SingleReview from "./SingleReview";

import "./index.css";

const MyReviews = () => {
  let orders = useSelector((state) => state.orders);
  orders = Object.values(orders);

  let products = useSelector((state) => state.products);

  let purchasedProductIds = new Set();
  orders.forEach((order) => {
    order.forEach((item) => {
      purchasedProductIds.add(item.product_id);
    });
  });

  let purchasedProducts = Array.from(purchasedProductIds).map(
    (id) => products[id]
  );


  return (
    <div>
      <AccountSideBar />
      <div className="account-container">
        <div>
          <div className="my-reviews-header">Reviews on your purchased items: </div>
        </div>
        {purchasedProducts.map((product) => (
          <SingleReview product={product} key={product?.id} />
        ))}
      </div>
    </div>
  );
};

export default MyReviews;
