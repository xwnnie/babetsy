import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect, Link } from "react-router-dom";
import { signUp } from "../../store/session";

const SignUpForm = () => {
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState("");
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [repeatPassword, setRepeatPassword] = useState("");
  const [phone, setPhone] = useState("");
  const [address, setAddress] = useState("");

  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(
        signUp(username, fullName, email, password, phone, address)
      );
      if (data) {
        setErrors(data);
      }
    } else {
      setErrors(["Repeat password doesn't match Password"]);
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateFullName = (e) => {
    setFullName(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  const updatePhone = (e) => {
    setPhone(e.target.value);
  };

  const updateAddress = (e) => {
    setAddress(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className="login-form-container">
      <form onSubmit={onSignUp} className="login-form signup-form">
        <div className="login-form-logo">babetsy</div>
        <div className="auth-error">
          {errors.map((error, ind) => (
            <div key={ind}>
              <span class="material-symbols-outlined">error</span> {error}
            </div>
          ))}
        </div>
        <div>
          <input
            type="text"
            name="username"
            onChange={updateUsername}
            value={username}
            placeholder="Username*"
            required
          ></input>
        </div>
        <div>
          <input
            type="text"
            name="fullName"
            onChange={updateFullName}
            value={fullName}
            placeholder="Full Name*"
            required
          ></input>
        </div>
        <div>
          <input
            type="text"
            name="email"
            placeholder="Email*"
            onChange={updateEmail}
            value={email}
            required
          ></input>
        </div>
        <div>
          <input
            type="password"
            name="password"
            placeholder="Password*"
            onChange={updatePassword}
            value={password}
            required
          ></input>
        </div>
        <div>
          <input
            type="password"
            name="repeat_password"
            placeholder="Repeat Password*"
            onChange={updateRepeatPassword}
            value={repeatPassword}
            required
          ></input>
        </div>
        <div>
          <input
            type="tel"
            name="phone"
            onChange={updatePhone}
            value={phone}
            placeholder="Phone Number*"
            required
          ></input>
        </div>
        <div>
          <input
            type="text"
            name="address"
            placeholder="Address*"
            onChange={updateAddress}
            value={address}
            required
          ></input>
        </div>
        <div className="submit-group">
          <button type="submit" className="login-btn">
            Sign Up
          </button>
          <Link to="/login">
            <div className="auth-form-link">
              Already have an account? <span>Log In!</span>
            </div>
          </Link>
        </div>
      </form>
    </div>
  );
};

export default SignUpForm;
