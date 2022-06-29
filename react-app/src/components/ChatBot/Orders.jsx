import { Link } from "react-router-dom";

const Orders = () => {

    return (
        <div>
            <Link to='/my-orders' className="chatbot-option-link"> Order History</Link>
            {/* <Link to='/my-orders'>Order History</Link> */}
        </div>
    )
}

export default Orders;