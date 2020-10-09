import axios from "axios";

import { GET_ANIMALS, DELETE_ANIMAL } from "./types";

export const getAnimals = () => (dispatch) => {
  axios
    .get("/api/animal/")
    .then((res) => {
      dispatch({
        type: GET_ANIMALS,
        payload: res.data,
      });
    })
    .catch((err) => console.log(err));
};

//export const detailsAnimal = () => (dispatch) => {
//  axios
//    .get("/api/animal/")
//    .then((res) => {
//      dispatch({
//        type: GET_ANIMALS,
//        payload: res.data,
//      });
//    })
//    .catch((err) => console.log(err));
//};

export const deleteAnimal = (id) => (dispatch) => {
  axios
    .delete(`/api/animal/${id}/`)
    .then((res) => {
      dispatch({
        type: DELETE_ANIMAL,
        payload: id,
      });
    })
    .catch((err) => console.log(err));
};
