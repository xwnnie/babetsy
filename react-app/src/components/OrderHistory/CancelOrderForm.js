import { useDispatch } from "react-redux";
import { cancelOrder } from "../../store/orders";

const CancelOrderForm = ({ orderNumber, setShowModal }) => {
  const dispatch = useDispatch();

  const handleOnClick = async (e) => {
    e.preventDefault();
    await dispatch(cancelOrder(orderNumber));
    setShowModal(false);
  };
  return (
    <div className="redirect-msg-container">
      <div className="edit-form-logo">BABETSY</div>
      <p className="redirect-msg">Do you really want to cancel this order?</p>
      <button onClick={handleOnClick}>Cancel Order</button>
    </div>
  );
};

export default CancelOrderForm;