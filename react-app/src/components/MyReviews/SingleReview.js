import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";

import { addReview, updateReview } from "../../store/reviews";
import DeleteReviewBtn from "../DeleteReview";

const SingleReview = ({ product }) => {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  let reviews = useSelector((state) => state.reviews);
  reviews = Object.values(reviews);
  let currReview = reviews.filter(
    (review) =>
      review.author_id === sessionUser?.id && review.product_id === product.id
  );
  currReview = currReview[0];
  // console.log(currReview)

  const [showCreateForm, setShowCreateForm] = useState(false);
  const [showEditForm, setShowEditForm] = useState(false);
  const [content, setContent] = useState("" || currReview?.content);

  const handleCreateOnSubmit = async (e) => {
      let createdAt = new Date();
    e.preventDefault();
    const payload = {
      content,
      product_id: product.id,
      author_id: sessionUser.id,
      created_at: createdAt.toString(),
      updated_at: createdAt.toString(),
    };
    await dispatch(addReview(payload));
    setShowCreateForm(false);
    // setContent("")
  };

  const handleEditOnSubmit = async (e) => {
    e.preventDefault();
    let updatedAt = new Date();
    const payload = {
      content,
      updated_at: updatedAt.toString()
    };
    await dispatch(updateReview(payload, currReview.id));
    setShowEditForm(false);
    // setContent("");
  };

  const reviewForm = (
    <form onSubmit={handleCreateOnSubmit}>
      <textarea value={content} onChange={(e) => setContent(e.target.value)} />
      <button type="cancel" onClick={() => setShowCreateForm(false)}>
        Cancel
      </button>
      <button type="submit">Add</button>
    </form>
  );

  const editReviewForm = (
    <form onSubmit={handleEditOnSubmit}>
      <textarea value={content} onChange={(e) => setContent(e.target.value)} />
      <button type="cancel" onClick={() => setShowCreateForm(false)}>
        Cancel
      </button>
      <button type="submit">Update</button>
    </form>
  );

  return (
    <div className="my-review-container">
      <img src={product?.image_url} className="review-img" />
      <div>
        <div className="review-product-name">{product?.name}</div>
        {currReview ? (
          <div className="review-content">
            <div>My review: </div>
            <div>{currReview.content}</div>
            {!showEditForm ? (
              <div>
                <button onClick={() => setShowEditForm(true)}>
                  Edit Review
                </button>
                <DeleteReviewBtn reviewId={currReview?.id} />
              </div>
            ) : null}
          </div>
        ) : !showCreateForm ? (
          <button onClick={() => setShowCreateForm(true)}>Add Review</button>
        ) : null}
        {showCreateForm ? reviewForm : null}
        {showEditForm ? editReviewForm : null}
      </div>
    </div>
  );
};

export default SingleReview;
