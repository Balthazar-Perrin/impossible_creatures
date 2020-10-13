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
  };

  static propTypes = {
    fuseAnimals: PropTypes.func.isRequired,
  };

  onChange = (e) => this.setState({ [e.target.name]: e.target.value });

  onSubmit = (e) => {
    e.preventDefault();
    const { animal1_id, animal2_id, name, nameAnimal } = this.state;
    const query = { animal1_id, animal2_id, name, nameAnimal };
    console.log(this.state)
    this.props.fuseAnimals(this.state);
    
    this.setState({
      animal1_id: '',
      animal2_id: '',
      name: '',
      nameAnimal: '',
    });
  };

  render() {
    const { animal1_id, animal2_id, name, nameAnimal } = this.state;
    return (
      <div className="card card-body mt-4 mb-4">
        <h2>Fuse Animals</h2>
        <form onSubmit={this.onSubmit}>
          <div className="form-group">
            <label>Animal1</label>
            <input
              className="form-control"
              type="text"
              name="animal1_id"
              onChange={this.onChange}
              value={animal1_id}
            />
          </div>
          <div className="form-group">
            <label>Animal2</label>
            <input
              className="form-control"
              type="text"
              name="animal2_id"
              onChange={this.onChange}
              value={animal2_id}
            />
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
});

export default connect(mapStateToProps, { fuseAnimals })(Fusion);
