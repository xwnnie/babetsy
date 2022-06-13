import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";

import { addReview, updateReview } from "../../store/reviews";
import DeleteReviewBtn from "../DeleteReview";

const SingleReview = ({ product }) => {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  let reviews = useSelector((state) => state.reviews);
  reviews = Object.values(reviews);
  let currReview = reviews.filter(
    (review) =>
      review.author_id === sessionUser?.id && review?.product_id === product?.id
  );
  currReview = currReview[0];
  // console.log(currReview)

  const [errors, setErrors] = useState([]);
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
    const data = await dispatch(addReview(payload));
    if (data) {
      setErrors(data);
    } else {
      setShowCreateForm(false);
    }

    // setContent("")
  };

  const handleEditOnSubmit = async (e) => {
    e.preventDefault();
    let updatedAt = new Date();
    const payload = {
      content,
      updated_at: updatedAt.toString(),
    };
    const data = await dispatch(updateReview(payload, currReview.id));
    if (data) {
      setErrors(data);
    } else {
      setShowEditForm(false);
    }
    // setContent("");
  };

  const reviewForm = (
    <form onSubmit={handleCreateOnSubmit} className="review-form">
      <div className="auth-error">
        {errors.map((error, ind) => (
          <div key={ind}>
            <span class="material-symbols-outlined">error</span> {error}
          </div>
        ))}
      </div>
      <textarea
        className="review-textarea"
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
      <div className="review-form-btn-container">
        <button
          className="review-cancel-btn"
          type="cancel"
          onClick={() => {setShowCreateForm(false); setErrors([])}}
        >
          Cancel
        </button>
        <button className="review-submit-btn" type="submit">
          Add
        </button>
      </div>
    </form>
  );

  const editReviewForm = (
    <form onSubmit={handleEditOnSubmit} className="review-form edit">
      <div className="auth-error">
        {errors.map((error, ind) => (
          <div key={ind}>
            <span class="material-symbols-outlined">error</span> {error}
          </div>
        ))}
      </div>
      <textarea
        className="review-textarea"
        value={content}
        onChange={(e) => setContent(e.target.value)}
      />
      <div className="review-form-btn-container">
        <button
          type="cancel"
          className="review-cancel-btn"
          onClick={() => {setShowEditForm(false); setErrors([])}}
        >
          Cancel
        </button>
        <button type="submit" className="review-submit-btn">
          Update
        </button>
      </div>
    </form>
  );

  return (
    <div className="my-review-container">
      <Link to={`/products/${product?.id}`}>
        <img
          src={product?.image_url}
          className="review-img"
          alt={product?.name}
        />
      </Link>
      <div className="review-content-container">
        <Link to={`/products/${product?.id}`}>
          <div className="review-product-name">{product?.name}</div>
        </Link>
        {currReview ? (
          <div className="review-content">
            <div>{currReview.content}</div>
            {!showEditForm ? (
              <div className="edit-review-btns-container">
                <button
                  onClick={() => setShowEditForm(true)}
                  className="review-edit-btns"
                >
                  <span className="material-symbols-outlined">edit</span>
                </button>
                <DeleteReviewBtn reviewId={currReview?.id} />
              </div>
            ) : null}
          </div>
        ) : !showCreateForm ? (
          <button
            className="review-submit-btn"
            onClick={() => setShowCreateForm(true)}
          >
            Add Review
          </button>
        ) : null}
        {showCreateForm ? reviewForm : null}
        {showEditForm ? editReviewForm : null}
      </div>
    </div>
  );
};

export default SingleReview;
