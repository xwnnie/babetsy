import { useState } from "react";
import ReviewsList from "./ReviewsList";
import { Modal } from "../../context/Modal";
import "./index.css";

const ShowReviewsBtn = ({reviewsCount, reviews}) => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button className="show-review-btn" onClick={() => setShowModal(true)}>REVIEWS ({reviewsCount})</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <ReviewsList setShowModal={setShowModal} reviews={reviews}/>
        </Modal>
      )}
    </>
  );
};

export default ShowReviewsBtn;
