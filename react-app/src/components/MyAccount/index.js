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
        {/* <div>Settings</div> */}
        <div className="account-details">
          <div>
            Username: <span id="username">{sessionUser?.username}</span>
          </div>
          <div>
            Full Name: <span id="full_name">{sessionUser?.full_name}</span>
          </div>
          <div>
            Phone number: <span id="phone">{sessionUser?.phone}</span>
          </div>
          <div>
            Address: <span id="address">{sessionUser?.address}</span>
          </div>
          <EditAddressBtn />
        </div>
      </div>
    </div>
  );
};

export default MyAccount;
