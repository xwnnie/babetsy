import { useState } from "react";
import { useSelector, useDispatch } from "react-redux";

import { editAddress } from "../../store/session";
import ErrorMessage from "../ErrorMessage";

const EditAddressForm = ({ setShowModal }) => {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [errors, setErrors] = useState([]);
  const [errorMessages, setErrorMessages] = useState({});
  const [fullName, setFullName] = useState(sessionUser.full_name);
  const [phone, setPhone] = useState(sessionUser.phone);
  const [address, setAddress] = useState(sessionUser.address);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (typeof parseInt(phone) !== "number") {
      return setErrors([...errors, "Not a valid phone number"]);
    }
    const payload = {
      address,
      full_name: fullName,
      phone,
    };
    const data = await dispatch(editAddress(payload, sessionUser.id));
    if (data) {
      let errorsObj = {};
      data.forEach((error) => {
        const [label, message] = error.split(" : ");
        errorsObj[label] = message;
      });
      setErrorMessages(errorsObj);
    } else {
      setShowModal(false);
    }
    // 
  };
  return (
    <form onSubmit={handleSubmit} className="edit-address-form">
      <div className="edit-form-logo">BABETSY</div>
      <div className="edit-address-header">Edit Your Shipping Address</div>
      <div className="auth-error">
        {/* {errors.map((error, ind) => (
          <div key={ind}>
            <span class="material-symbols-outlined">error</span> {error}
          </div>
        ))} */}
      </div>
      <label>Full Name*</label>
      <input
        type="text"
        value={fullName}
        onChange={(e) => setFullName(e.target.value)}
      />
      <ErrorMessage message={errorMessages.full_name} />
      <label>Phone Number*</label>
      <input
        type="text"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
      />
      <ErrorMessage message={errorMessages.phone} />
      <label>Address*</label>
      <input
        type="text"
        value={address}
        onChange={(e) => setAddress(e.target.value)}
      />
      <ErrorMessage message={errorMessages.address} />
      <button className="" type="submit">
        Save
      </button>
    </form>
  );
};

export default EditAddressForm;
