import { useState } from "react";
import ReviewsList from "./ReviewsList";
import { Modal } from "../../context/Modal";
import "./index.css";

const ShowReviewsBtn = ({reviewsCount, reviews}) => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button onClick={() => setShowModal(true)}>Reviews({reviewsCount})</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <ReviewsList setShowModal={setShowModal} reviews={reviews}/>
        </Modal>
      )}
    </>
  );
};

export default ShowReviewsBtn;
