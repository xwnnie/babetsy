import { useState } from "react";

const SingleReview = ({ product, myReviews }) => {
  const [showForm, setShowForm] = useState(false);
  const reviewForm = (
    <form>
      <textarea />
      <button onClick={() => setShowForm(false)}>Cancel</button>
      <button onClick={() => setShowForm(false)}>Add</button>
    </form>
  );

  return (
    <div className="my-review-container">
      <img src={product?.image_url} className="review-img" />
      <div>
        <div className="review-product-name">{product?.name}</div>
        <div>My review: </div>
        <div className="review-content">
          {product?.id in myReviews ? (
            myReviews[product.id].content
          ) : !showForm ? (
            <button onClick={() => setShowForm(true)}>Add Review</button>
          ) : null}
          {showForm ? reviewForm : null}
        </div>
      </div>
    </div>
  );
};

export default SingleReview;
