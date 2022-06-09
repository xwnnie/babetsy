import { useSelector } from "react-redux";

import OrderHistory from "../OrderHistory";
import EditAddressBtn from "../EditAddress";
import AccountSideBar from "../AccountSideBar";

import "./index.css";

const MyAccount = () => {
  const sessionUser = useSelector((state) => state.session.user);
  return (
    <div>
      <AccountSideBar />
      <div className="account-container">
        <div>
          <div>My Account</div>
          <div>{sessionUser?.username}</div>
          <div>{sessionUser?.address}</div>
          <EditAddressBtn />
        </div>

        {/* <OrderHistory /> */}
      </div>
    </div>
  );
};

export default MyAccount;
