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

  freeShipping() {
    const message = this.createChatBotMessage(
      "Free shipping on all orders over $25"
    );

    this.setState((prev) => ({
      ...prev,
      messages: [...prev.messages, message],
    }));
  }

  checkOrder() {
    const message = this.createChatBotMessage("Check your orders: ", {
      widget: "orders",
    });

    this.setState((prev) => ({
      ...prev,
      messages: [...prev.messages, message],
    }));
  }

  updateAddress() {
    const message = this.createChatBotMessage(
      "Update your address here:",
      {
        widget: "updateAddress",
      }
    );

    this.setState((prev) => ({
      ...prev,
      messages: [...prev.messages, message],
    }));
  }

  account() {
    const message = this.createChatBotMessage(
      "Access your account:",
      {
        widget: "updateAddress",
      }
    );

    this.setState((prev) => ({
      ...prev,
      messages: [...prev.messages, message],
    }));
  }

  else() {
    const message = this.createChatBotMessage(
      "Sorry I don't understand.  Please try some keywords like \"orders\", \"my account\" or \"free shipping policy\"."
    );

    this.setState((prev) => ({
      ...prev,
      messages: [...prev.messages, message],
    }));
  }
}

export default ActionProvider;
