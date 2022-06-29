// import { useSelector } from "react-redux";

import { createChatBotMessage } from "react-chatbot-kit";

import Orders from "./Orders";
import Address from "./Address";

// const sessionUser = useSelector(state => state.session.user);
const config = {
  initialMessages: [
    createChatBotMessage(`Hello there, what can I do for you?`),
  ],
  widgets: [
    {
      widgetName: "orders",
      widgetFunc: (props) => <Orders {...props} />,
    },
    {
      widgetName: "updateAddress",
      widgetFunc: (props) => <Address {...props} />,
    },
  ],
  botName: "Bot",
  //   customStyles: {
  //     botMessageBox: {
  //       backgroundColor: "#ccdd9f",
  //     },
  //     chatButton: {
  //       backgroundColor: "#ccdd9f",
  //     },
  //   },
};

export default config;
