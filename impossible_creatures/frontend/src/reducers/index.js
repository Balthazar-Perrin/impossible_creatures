import { combineReducers } from "redux";
import animals from "./animals";
import errors from "./errors";
import messages from "./messages";
import auth from "./auth";


export default combineReducers({
  animalsReducer: animals,
  errors: errors,
  messages: messages,
  auth: auth
});
