import { useHistory } from "react-router-dom";
import "./index.css";

const HomePage = () => {
    const history = useHistory();

  return (
    <div className="home-page-container">
      {/* <h1>HomePage</h1> */}
      <div className="ad-1">
        <div className="ad-text">
          <h1>Hello, sunshine!</h1>
          <button onClick={() => history.push("/summer")}>Shop now</button>
        </div>
      </div>
      <div className="ad-donate">
        <div className="ad-donate-text">
          <p>
            We're partnering with Save the Children to protect children in the
            U.S. and around the world. Be a part of the support with us and
            donate today!
          </p>
          <a href="https://www.savethechildren.org/us/ways-to-help/ways-to-give/donate-childrens-charity">
            Donate Today
          </a>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
