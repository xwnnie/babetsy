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
    <div>
      <p>Do you really want to cancel this order?</p>
      <button onClick={handleOnClick}>Cancel Order</button>
    </div>
  );
};

export default CancelOrderForm;