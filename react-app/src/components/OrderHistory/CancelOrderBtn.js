import { useState } from "react";
import CancelOrderForm from "./CancelOrderForm";
import { Modal } from "../../context/Modal";

const CancelOrderBtn = ({ orderNumber }) => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button onClick={() => setShowModal(true)}>Cancel</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <CancelOrderForm setShowModal={setShowModal} orderNumber={orderNumber} />
        </Modal>
      )}
    </>
  );
};

export default CancelOrderBtn;
