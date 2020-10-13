import { GET_ANIMALS, DELETE_ANIMAL, ADD_ANIMAL, GET_TRANSACTIONS, FUSE_ANIMALS } from "../actions/types.js";

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
    case ADD_ANIMAL:
      return {
        ...state,
        animals: [...state.animals, action.payload],
      };
    case GET_TRANSACTIONS:
      return {
        ...state,
        animals: action.payload,
      };
    case FUSE_ANIMALS:
      return {
        ...state,
        animals: [...state.animals, action.payload],
      };
    default:
      return state;
  }
}
