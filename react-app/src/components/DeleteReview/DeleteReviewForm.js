import { useDispatch } from "react-redux";
import { deleteReview } from "../../store/reviews";
// import "./DeleteTaskForm.css";

const DeleteReviewForm = ({ setShowModal, reviewId}) => {
  const dispatch = useDispatch();
  const handleSubmit = async (e) => {
    e.preventDefault();
    await dispatch(deleteReview(reviewId));
    setShowModal(false);
  };
  return (
    <div className="">
      <p>Do you really want to delete this review?</p>
      <form onSubmit={handleSubmit}>
        <button type="cancel" className="">
          Cancel
        </button>
        <button type="submit" className="">
          Delete
        </button>
      </form>
    </div>
  );
};

export default DeleteReviewForm;
