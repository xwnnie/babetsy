import { useState } from "react";
import Redirect from "./Redirect";
import { Modal } from "../../context/Modal";

import "./index.css";

const CheckOutBtn = ({cartItems, onSubmit}) => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button
        onClick={(e) => {setShowModal(true)}}
        className={`checkout-btn ${
          !cartItems || !cartItems.length ? "no-item" : null
        }`}
      >
        <span>Complete purchase</span>
      </button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <Redirect setShowModal={setShowModal} onSubmit={onSubmit}/>
        </Modal>
      )}
    </>
  );
};

export default CheckOutBtn;
