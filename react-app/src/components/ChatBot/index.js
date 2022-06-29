import Chatbot from "react-chatbot-kit";
import "react-chatbot-kit/build/main.css";
import "./index.css";

import ActionProvider from "./ActionProvider";
import MessageParser from "./MessageParser";
import config from "./config";
import { useState } from "react";

const ChatBot = () => {
  const [showBot, setShowBot] = useState(false);

  return (
    <div>
      {!showBot ? (
        <div onClick={() => setShowBot(true)} className="open-chatbot-btn">
          <span class="material-symbols-outlined">sms</span>
          <div>
            <div>Have any question? </div>
            <div>Talk to our Customer Service Bot!</div>
          </div>
        </div>
      ) : null}
      {showBot ? (
        <div>
          <button
            onClick={() => setShowBot(false)}
            className="close-chatbot-btn"
          >
            <span class="material-symbols-outlined">close</span>
          </button>
          <div className="App chatbot">
            <header className="App-header">
              <Chatbot
                config={config}
                actionProvider={ActionProvider}
                messageParser={MessageParser}
              />
            </header>
          </div>
        </div>
      ) : null}
    </div>
  );
};

export default ChatBot;
