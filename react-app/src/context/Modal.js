import { createContext, useContext, useRef, useState, useEffect } from "react";
import ReactDOM from "react-dom";
import { useHistory } from "react-router-dom";
import "./Modal.css";

export const ModalContext = createContext();

const ModalProvider = ({ children }) => {
  const modalRef = useRef();
  const [value, setValue] = useState();

  useEffect(() => {
    setValue(modalRef.current);
  }, []);

  // const history = useHistory();
  // const locations = history?.location?.pathname.split("/")
  // console.log("locations", history?.location?.pathname)

  return (
    <>
      <ModalContext.Provider value={value}>{children}</ModalContext.Provider>
      <div ref={modalRef} />
    </>
  );
};

export function Modal({ onClose, children }) {
  const modalNode = useContext(ModalContext);
  if (!modalNode) return null;

  console.log("****", children)

  return ReactDOM.createPortal(
    <div id="modal">
      <div id="modal-background" onClick={onClose} />
      <div id="modal-content" className={`${Object.keys(children.props)[1]}-modal-container`}>{children}</div>
    </div>,
    modalNode
  );
}

export default ModalProvider;
