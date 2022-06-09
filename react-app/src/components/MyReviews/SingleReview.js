import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { addReview } from "../../store/reviews";

const SingleReview = ({ product, myReviews }) => {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);

  const [showCreateForm, setShowCreateForm] = useState(false);
  const [content, setContent] = useState("");

  const handleOnSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      content,
      product_id: product.id,
      author_id: sessionUser.id,
    };
    await dispatch(addReview(payload));
    setShowCreateForm(false);
  };
  const reviewForm = (
    <form onSubmit={handleOnSubmit}>
      <textarea value={content} onChange={(e) => setContent(e.target.value)} />
      <button type="cancel" onClick={() => setShowCreateForm(false)}>
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
        {product?.id in myReviews ? (
          <div className="review-content">
            <div>My review: </div>
            <div>{myReviews[product.id].content}</div>
            <button>Edit Review</button>
            <button>Delete Review</button>
          </div>
        ) : !showCreateForm ? (
          <button onClick={() => setShowCreateForm(true)}>Add Review</button>
        ) : null}
        {showCreateForm ? reviewForm : null}
      </div>
    </div>
  );
};

export default SingleReview;
