import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";

const Redirect = ({setShowModal, onSubmit}) => {
  const history = useHistory();

  const [message, setMessage] =  useState("Confirming your payment....");

  useEffect(() => {
    const timer = setTimeout(() => {
        setMessage("Thank you. Your order has been placed!");
    }, 1500);
    return () => clearTimeout(timer);
  }, []);

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowModal(false);
      onSubmit();
      history.push("/my-orders");
    }, 2500);
    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="redirect-msg-container">
      <div className="edit-form-logo">BABETSY</div>
      <div className="redirect-msg">{message}</div>
    </div>
  );
};

export default Redirect;
