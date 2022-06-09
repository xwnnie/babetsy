import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { addReview } from "../../store/reviews";

const SingleReview = ({ product, myReviews }) => {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);

  const [showForm, setShowForm] = useState(false);
  const [content, setContent] = useState("");

  const handleOnSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      content,
      product_id: product.id,
      author_id: sessionUser.id,
    };
    await dispatch(addReview(payload));
    setShowForm(false);
  };
  const reviewForm = (
    <form onSubmit={handleOnSubmit}>
      <textarea value={content} onChange={(e) => setContent(e.target.value)} />
      <button type="cancel" onClick={() => setShowForm(false)}>
        Cancel
      </button>
      <button type="submit">Add</button>
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
