import { useState } from "react";
import DeleteReviewForm from "./DeleteReviewForm";
import { Modal } from "../../context/Modal";

const DeleteReviewBtn = ({ reviewId }) => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button className="table-delete-btn" onClick={() => setShowModal(true)}>
        Delete Review
      </button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <DeleteReviewForm
            setShowModal={setShowModal}
            reviewId={reviewId}
          />
        </Modal>
      )}
    </>
  );
};

export default DeleteReviewBtn;
