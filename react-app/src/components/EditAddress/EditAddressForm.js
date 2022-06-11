import { useState } from "react";
import { useSelector, useDispatch } from "react-redux";

import { editAddress } from "../../store/session";

const EditAddressForm = ({ setShowModal }) => {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [fullName, setFullName] = useState(sessionUser.full_name);
  const [phone, setPhone] = useState(sessionUser.phone);
  const [address, setAddress] = useState(sessionUser.address);
  

  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      address,
      full_name: fullName,
      phone
    };
    await dispatch(editAddress(payload, sessionUser.id));
    setShowModal(false);
  };
  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={fullName}
        onChange={(e) => setFullName(e.target.value)}
      />
      <input
        type="text"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
      />
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
