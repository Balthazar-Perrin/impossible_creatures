import { GET_ANIMALS, DELETE_ANIMAL } from "../actions/types.js";

const initialState = {
  animals: [],
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_ANIMALS:
      return {
        ...state,
        animals: action.payload,
      };
    case DELETE_ANIMAL:
      return {
        ...state,
        animals: state.animals.filter((animal) => animal.id !== action.payload),
      };
    default:
      return state;
  }
}
