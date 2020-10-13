import axios from 'axios';
import { createMessage, returnErrors } from './messages';
import { tokenConfig } from './auth';

import { GET_ANIMALS, DELETE_ANIMAL, ADD_ANIMAL, GET_TRANSACTIONS, FUSE_ANIMALS, SELL_ANIMAL, GET_SPECIES } from './types';

export const getAnimals = (id) => (dispatch, getState) => {
  axios
    .get(`/api/inventory/${id}`, tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_ANIMALS,
        payload: res.data,
      });
    })
    .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};

export const deleteAnimal = (id) => (dispatch, getState) => {
  axios
    .delete(`/api/animal/${id}/`, tokenConfig(getState))
    .then((res) => {
      dispatch(createMessage({ deleteLead: 'Lead Deleted' }));
      dispatch({
        type: DELETE_ANIMAL,
        payload: id,
      });
    })
    .catch((err) => console.log(err));
};

export const addAnimal = (animal) => (dispatch, getState) => {
  axios
    .post('/api/animal/', animal, tokenConfig(getState))
    .then((res) => {
      dispatch(createMessage({ addLead: 'Lead Added' }));
      dispatch({
        type: ADD_ANIMAL,
        payload: res.data,
      });
    })
    .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};

export const fuseAnimals = (state) => (dispatch, getState) => {
  axios
    .post('/api/fusion/', state, tokenConfig(getState))
    .then((res) => {
      dispatch(createMessage({ addLead: 'Animals Fused' }));
      dispatch({
        type: FUSE_ANIMALS,
        payload: state,
      });
    })
    .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};

export const getTransactions = () => (dispatch, getState) => {
  axios
    .get(`/api/transaction/`, tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_TRANSACTIONS,
        payload: res.data,
      });
    })
    .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};

export const sellAnimal = (id) => (dispatch, getState) => {
  axios
    .post(`/api/sell/`, tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: SELL_ANIMAL,
        payload: id,
      });
    })
    .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};

export const getSpecies = () => (dispatch, getState) => {
  axios
    .get(`/api/species/`, tokenConfig(getState))
    .then((res) => {
      dispatch({
        type: GET_SPECIES,
        payload: res.data,
      });
    })
    .catch((err) => dispatch(returnErrors(err.response.data, err.response.status)));
};