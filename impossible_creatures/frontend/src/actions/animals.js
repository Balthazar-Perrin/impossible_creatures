import axios from "axios";
import { createMessage, returnErrors } from './messages'

import { GET_ANIMALS, DELETE_ANIMAL, ADD_ANIMAL } from "./types";

export const getAnimals = () => (dispatch) => {
  axios
    .get(`/api/animal/`)
    .then((res) => {
      dispatch({
        type: GET_ANIMALS,
        payload: res.data,
      });
    })
    .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};

export const deleteAnimal = (id) => (dispatch) => {
  axios
    .delete(`/api/animal/${id}/`)
    .then((res) => {
      dispatch(createMessage({ deleteAnimal: 'Animal deleted'}))
      dispatch({
        type: DELETE_ANIMAL,
        payload: id,
      });
    })
    .catch((err) => console.log(err));
};

export const addAnimal = (animal) => (dispatch) => {
  axios
    .post('/api/animal/', animal)
    .then((res) => {
      dispatch(createMessage({ addAnimal: 'Animal Added'}))
      dispatch({
        type: ADD_ANIMAL,
        payload: res.data,
      });
    })
    .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};