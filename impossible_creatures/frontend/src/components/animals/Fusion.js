import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addAnimal } from '../../actions/animals';

export class Form extends Component {
  state = {
    name: '',
    creator_id: '',
    owner_id: '',
    species_id: '',
  };

  static propTypes = {
    addAnimal: PropTypes.func.isRequired,
  };

  onChange = (e) => this.setState({ [e.target.name]: e.target.value });

  onSubmit = (e) => {
    e.preventDefault();
    const { name, creator_id, owner_id, species_id } = this.state;
    const animal = { name, creator_id, owner_id, species_id };
    this.props.addAnimal(animal);
    this.setState({
      name: '',
      creator_id: '',
      owner_id: '',
      species_id: '',
    });
  };

  render() {
    const { name, creator_id, owner_id, species_id } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Add Lead</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>Name</label>
            <input
              className="form-control"
              type="text"
              name="name"
              onChange={this.onChange}
              value={name}
            />
          </div>
          <div className="form-group">
            <label>Creator</label>
            <input
              className="form-control"
              type="text"
              name="creator_id"
              onChange={this.onChange}
              value={creator_id}
            />
          </div>
          <div className="form-group">
            <label>Owner</label>
            <input
              className="form-control"
              type="text"
              name="owner_id"
              onChange={this.onChange}
              value={owner_id}
            />
          </div>
          <div className="form-group">
            <label>Species</label>
            <textarea
              className="form-control"
              type="text"
              name="species_id"
              onChange={this.onChange}
              value={species_id}
            />
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default connect(null, { addAnimal })(Form);
