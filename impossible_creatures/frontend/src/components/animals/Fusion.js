import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { fuseAnimals } from '../../actions/animals';


export class Fusion extends Component {
  state = {
    animal1_id: '',
    animal2_id: '',
    name: '',
    nameAnimal: '',
    user: this.props.auth.user.id,
  };

  static propTypes = {
    fuseAnimals: PropTypes.func.isRequired,
    auth: PropTypes.object.isRequired,
  };

  onChange = (e) => this.setState({ [e.target.name]: e.target.value });

  onSubmit = (e) => {
    e.preventDefault();
    const { animal1_id, animal2_id, name, nameAnimal, user } = this.state;
    const query = { animal1_id, animal2_id, name, nameAnimal };
    console.log(this.state)
    this.props.fuseAnimals(this.state);

    this.setState({
      animal1_id: '',
      animal2_id: '',
      name: '',
      nameAnimal: '',
    });
    this.props.history.push('/')
  };

  render() {
    const { animal1_id, animal2_id, name, nameAnimal, user } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Fuse Animals</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>Animal 1</label>
            <select name="animal1_id" className="form-control" value={this.state.value} onChange={this.onChange}>
              {this.props.animals.map((animal) => (
              <option value={animal.id}>{animal.name}</option>
              ))}
            </select>

          </div>
          <div className="form-group">
            <label>Animal 2</label>
            <select name="animal2_id" className="form-control" value={this.state.value} onChange={this.onChange}>
              {this.props.animals.map((animal) => (
              <option value={animal.id}>{animal.name}</option>
            ))}
            </select>
          </div>
          <div className="form-group">
            <label>Name Species</label>
            <input
              className="form-control"
              type="text"
              name="name"
              onChange={this.onChange}
              value={name}
            />
          </div>
          <div className="form-group">
            <label>Name Animal</label>
            <textarea
              className="form-control"
              type="text"
              name="nameAnimal"
              onChange={this.onChange}
              value={nameAnimal}
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

const mapStateToProps = (state) => ({
  animals: state.animalsReducer.animals,
  auth: state.auth,
});

export default connect(mapStateToProps, { fuseAnimals })(Fusion);
