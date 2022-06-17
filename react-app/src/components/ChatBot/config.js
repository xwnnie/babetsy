import { createChatBotMessage } from "react-chatbot-kit";

const config = {
  initialMessages: [
    createChatBotMessage(`Hello there, what can I do for you?`),
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
