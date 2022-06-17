class MessageParser {
  constructor(actionProvider, state) {
    this.actionProvider = actionProvider;
    this.state = state;
  }

  parse(message) {
    if (message.includes("hello")) {
      this.actionProvider.handleHello();
    }
  }

  parse(message) {
    if (message.includes("order")) {
      this.actionProvider.checkOrder();
    }
  }

  //   parse(message) {
  //     console.log(message);
  //   }
}

export default MessageParser;
