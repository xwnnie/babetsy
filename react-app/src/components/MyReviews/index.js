import { useSelector } from "react-redux";
import { useState } from "react";

import AccountSideBar from "../AccountSideBar";
import SingleReview from "./SingleReview";

import "./index.css";

const MyReviews = () => {
  const sessionUser = useSelector((state) => state.session.user);
  let orders = useSelector((state) => state.orders);
  orders = Object.values(orders);

  let products = useSelector((state) => state.products);
  let reviews = useSelector((state) => state.reviews);

  let myReviews = new Object();
  for (const [key, value] of Object.entries(reviews)) {
    if (value?.author_id == sessionUser?.id) {
      myReviews[key] = value;
    }
  }
  //   console.log(myReviews)
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
          <div>Reviews on purchased items</div>
        </div>
        {purchasedProducts.map((product) => (
            <SingleReview product={product} myReviews={myReviews}/>
        //   <div className="my-review-container">
        //     <img src={product?.image_url} className="review-img" />
        //     <div>
        //       <div className="review-product-name">{product?.name}</div>
        //       <div>My review: </div>
        //       <div className="review-content">
        //         {product?.id in myReviews ? (
        //           myReviews[product.id].content
        //         ) : (
        //           <button onClick={() => setShowForm(true)}>Add Review</button>
        //         )}
        //         {showForm ? reviewForm() : null}
        //       </div>
        //     </div>
        //   </div>
        )
        )}
      </div>
    </div>
  );
};

export default MyReviews;
