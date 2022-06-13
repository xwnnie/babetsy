import { useState } from "react";
import { useSelector, useDispatch } from "react-redux";

import { editAddress } from "../../store/session";

const EditAddressForm = ({ setShowModal }) => {
  const dispatch = useDispatch();
  const sessionUser = useSelector((state) => state.session.user);
  const [errors, setErrors] = useState([]);
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
      setErrors(data);
    } else {
      setShowModal(false);
    }
    // 
  };
  return (
    <form onSubmit={handleSubmit}>
      <div className="auth-error">
        {errors.map((error, ind) => (
          <div key={ind}>
            <span class="material-symbols-outlined">error</span> {error}
          </div>
        ))}
      </div>
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
