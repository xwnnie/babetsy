import { useSelector } from "react-redux";

import EditAddressBtn from "../EditAddress";
import AccountSideBar from "../AccountSideBar";

import "./index.css";

const MyAccount = () => {
  const sessionUser = useSelector((state) => state.session.user);
  return (
    <div>
      <AccountSideBar />
      <div className="account-container ">
        <div>Settings</div>
        <div className="account-details">
          <div>Username: {sessionUser?.username}</div>
          <div>Full name: {sessionUser?.full_name}</div>
          <div>Phone number: {sessionUser?.phone}</div>
          <div>Address: {sessionUser?.address}</div>
          <EditAddressBtn />
        </div>
      </div>
    </div>
  );
};

export default MyAccount;
