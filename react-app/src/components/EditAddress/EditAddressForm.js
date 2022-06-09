import { useState } from "react";
import { useSelector, useDispatch } from "react-redux";

import { editAddress } from "../../store/session";

const EditAddressForm = ({ setShowModal }) => {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [address, setAddress] = useState(sessionUser.address);
  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      address,
    };
    await dispatch(editAddress(payload, sessionUser.id));
    setShowModal(false);
  };
  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={address}
        onChange={(e) => setAddress(e.target.value)}
      />
      <button className="" type="submit">
        Save
      </button>
    </form>
  );
};

export default EditAddressForm;
