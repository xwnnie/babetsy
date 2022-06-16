import "./index.css";

const ErrorMessage = ({ label, message }) => {
  if (!message) return null;
    // console.log("********", message)
  return (
    <p className="error-message">
      <span className="material-symbols-outlined">error</span>
      {/* {message ? (label ? `${label}: ` : "") + `${message}` : ""} */}
      {/* {label ? ({label}) : ""}  */}
      {label.length ? ` ${label}: ` : ""}
      {message}
    </p>
  );
};

export default ErrorMessage;
