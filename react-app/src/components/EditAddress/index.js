import { useState } from "react";
import EditAddressForm from "./EditAddressForm";
import { Modal } from "../../context/Modal";

const EditAddressBtn = () => {
  const [showModal, setShowModal] = useState(false);

  return (
    <>
      <button onClick={() => setShowModal(true)}>Edit Address</button>
      {showModal && (
        <Modal onClose={() => setShowModal(false)}>
          <EditAddressForm
            setShowModal={setShowModal}
          />
        </Modal>
      )}
    </>
  );
};

export default EditAddressBtn;
