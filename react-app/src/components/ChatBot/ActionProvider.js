// import { createChatBotMessage } from "react-chatbot-kit";

class ActionProvider {
  constructor(
    createChatBotMessage,
    setStateFunc,
    createClientMessage,
    stateRef,
    createCustomMessage,
    ...rest
  ) {
    this.createChatBotMessage = createChatBotMessage;
    this.setState = setStateFunc;
    this.createClientMessage = createClientMessage;
    this.stateRef = stateRef;
    this.createCustomMessage = createCustomMessage;
  }

  handleHello() {
    const message = this.createChatBotMessage("Hello. Nice to meet you.");

    this.setState((prev) => ({
      ...prev,
      messages: [...prev.messages, message],
    }));
  }

  checkOrder() {
      let text = "Order History";
      let url =  "https://babetsy.herokuapp.com/my-orders";
      const orderLink = text.link(url);

    const message = this.createChatBotMessage(
      `Please check your ${orderLink} here: https://babetsy.herokuapp.com/my-orders.`
    );

    this.setState((prev) => ({
      ...prev,
      messages: [...prev.messages, message],
    }));
  }
}

export default ActionProvider;
