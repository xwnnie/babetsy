import "./index.css";
import { NavLink, useHistory } from "react-router-dom";
// import { useDispatch, useSelector } from "react-redux";
// import { logout } from "../../store/session";


const AccountSideBar = () => {
  const history = useHistory();
//   const dispatch = useDispatch();
//   const onLogout = async (e) => {
//     history.push("/");
//     await dispatch(logout());
//   };
//   const sessionUser = useSelector((state) => state.session.user);
  return (
    <div className="sidebar-container">
      <div className="sidebar-menu main">
        <div className="sidebar-menu-item sidebar-header">
          My Account
        </div>
        <div className="sidebar-menu-item">
          <NavLink to="/my-account" exact={true} activeClassName="selected">
            Settings
          </NavLink>
        </div>
        <div className="sidebar-menu-item">
          <NavLink to="/my-orders" exact={true} activeClassName="selected">
            All purchases
          </NavLink>
        </div>
        <div className="sidebar-menu-item">
          <NavLink to="/my-reviews" exact={true} activeClassName="selected">
            Reviews
          </NavLink>
        </div>
      </div>
    </div>
  );
};

export default AccountSideBar;
