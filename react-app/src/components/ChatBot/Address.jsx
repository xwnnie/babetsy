import { Link } from "react-router-dom";

const Address = () => {

    return (
        <div>
            <Link to='/my-account' className="chatbot-option-link">My Account</Link>
            {/* <Link to='/my-orders'>Order History</Link> */}
        </div>
    )
}

export default Address;