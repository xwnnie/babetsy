import { useHistory } from "react-router-dom";
import "./index.css";
import Recommend from "./Recommend";

const HomePage = () => {
    const history = useHistory();

  return (
    <div className="home-page-container">
      {/* <h1>HomePage</h1> */}
      <div className="ad-1">
        <div className="ad-1-text">
          <h1>Hello, sunshine!</h1>
          <button onClick={() => history.push("/summer")}>Shop now</button>
        </div>
      </div>
      <Recommend />
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
      <div className="ad-1 ad-2">
        <div className="ad-1-text ad-2-text">
          <h1>Ready for your newborn?</h1>
          <button onClick={() => history.push("/newborn")}>Shop now</button>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
