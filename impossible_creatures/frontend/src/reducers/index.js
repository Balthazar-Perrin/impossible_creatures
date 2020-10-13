import { combineReducers } from "redux";
import animals from "./animals";
import errors from "./errors";
import messages from "./messages";


export default combineReducers({
  animalsReducer: animals,
  errors: errors,
  messages: messages
});
