class MessageParser {
  constructor(actionProvider, state) {
    this.actionProvider = actionProvider;
    this.state = state;
  }

  parse(message) {
    if (message.toLowerCase().includes("hello")) {
      this.actionProvider.handleHello();
    } else if (message.toLowerCase().includes("order")) {
      this.actionProvider.checkOrder();
    } else if (
      message.toLowerCase().includes("free") ||
      message.toLowerCase().includes("shipping")
    ) {
      this.actionProvider.freeShipping();
    } else if (message.toLowerCase().includes("address")) {
      this.actionProvider.updateAddress();
    } else if (message.toLowerCase().includes("account")) {
      this.actionProvider.account();
    } else {
      this.actionProvider.else();
    }
  }
}

export default MessageParser;
