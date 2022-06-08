import { useSelector } from "react-redux";

import OrderHistory from "../OrderHistory";
import EditAddressBtn from "../EditAddress";

const MyAccount = () => {
    const sessionUser = useSelector(state => state.session.user);
    return (
        <div>
            <div>
                <div>My Account</div>
                <div>{sessionUser?.username}</div>
                <div>{sessionUser?.address}</div>
                <EditAddressBtn />
            </div>
            
            <OrderHistory />
        </div>
    )
}

export default MyAccount;