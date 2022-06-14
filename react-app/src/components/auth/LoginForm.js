import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect, Link } from "react-router-dom";
import { login } from "../../store/session";

import "./auth.css";

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const user = useSelector((state) => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const loginDemo = async (e) => {
    e.preventDefault();
    const data = await dispatch(login("demo@aa.io", "password"));
    if (data) {
      const errors = {};
      if (Array.isArray(data)) {
        data.forEach((error) => {
          const label = error.split(":")[0].slice(0, -1);
          const message = error.split(":")[1].slice(1);
          errors[label] = message;
        });
      } else {
        errors.overall = data;
      }
      setErrors(errors);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div className="login-form-container">
      <form onSubmit={onLogin} className="login-form">
        <div className="login-form-logo">BABETSY</div>
        <div className="auth-error">
          {errors.map((error, ind) => (
            <div key={ind}>
              <span class="material-symbols-outlined">error</span> {error}
            </div>
          ))}
        </div>
        <div>
          <input
            name="email"
            type="text"
            placeholder="Email"
            value={email}
            onChange={updateEmail}
            required
          />
        </div>
        <div>
          <input
            name="password"
            type="password"
            placeholder="Password"
            value={password}
            onChange={updatePassword}
            required
          />
        </div>
        <div className="submit-group">
          <button type="submit" className="login-btn">
            Login
          </button>
          <button id="demo-btn" onClick={loginDemo}>
            Demo User
          </button>
          <Link to="/sign-up">
            <div className="auth-form-link">
              Don't have an account? <span>Sign Up!</span>
            </div>
          </Link>
        </div>
      </form>
    </div>
  );
};

export default LoginForm;
