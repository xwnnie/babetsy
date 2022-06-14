import { useDispatch } from "react-redux";
import { deleteReview } from "../../store/reviews";

import "./index.css";

const DeleteReviewForm = ({ setShowModal, reviewId}) => {
  const dispatch = useDispatch();
  const handleSubmit = async (e) => {
    e.preventDefault();
    await dispatch(deleteReview(reviewId));
    setShowModal(false);
  };
  return (
    <div className="redirect-msg-container">
      <div className="edit-form-logo">BABETSY</div>
      <p className="redirect-msg">Do you really want to delete this review?</p>
      <form onSubmit={handleSubmit} className="cancel-order-form">
        <button className="cancel-order-cancel-btn" onClick={() => setShowModal(false)}>
          Cancel
        </button>
        <button type="submit" className="cancel-order-submit-btn">
          Delete
        </button>
      </form>
    </div>
  );
};

export default DeleteReviewForm;
