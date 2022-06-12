import { useState } from "react";
import EditAddressForm from "./EditAddressForm";
import { Modal } from "../../context/Modal";

import "./index.css";

const EditAddressBtn = () => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button onClick={() => setShowModal(true)} className="edit-address-pen">
        <span className="material-symbols-outlined">edit</span>
      </button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <EditAddressForm setShowModal={setShowModal} />
        </Modal>
      )}
    </>
  );
};

export default EditAddressBtn;
