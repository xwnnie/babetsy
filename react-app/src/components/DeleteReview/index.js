import { useState } from "react";
import DeleteReviewForm from "./DeleteReviewForm";
import { Modal } from "../../context/Modal";

const DeleteReviewBtn = ({ reviewId }) => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button
        className="table-delete-btn review-edit-btns"
        onClick={() => setShowModal(true)}
      >
        <span className="material-symbols-outlined">delete</span>
      </button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <DeleteReviewForm setShowModal={setShowModal} reviewId={reviewId} />
        </Modal>
      )}
    </>
  );
};

export default DeleteReviewBtn;
