import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getAnimals, deleteAnimal } from "../../actions/animals";

export class Animals extends Component {
  static propTypes = {
    animals: PropTypes.array.isRequired,
    getAnimals: PropTypes.func.isRequired,
    deleteAnimal: PropTypes.func.isRequired,
  };

  componentDidMount() {
    this.props.getAnimals();
  }
  render() {
    return (
      <Fragment>
        <h2>Animals</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Name</th>
              <th>Species</th>
              <th>Owner</th>
              <th>Creator</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {this.props.animals.map((animal) => (
              <tr key={animal.id}>
                <td>{animal.name}</td>
                <td>{animal.species_name}</td>
                <td>{animal.owner_name}</td>
                <td>{animal.creator_name}</td>
                <td>
                  <button
                    onClick={this.props.deleteAnimal.bind(this, animal.id)}
                    className="btn btn-info btn-sm"
                  >
                    Details
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  animals: state.animalsReducer.animals,
});

export default connect(mapStateToProps, { getAnimals, deleteAnimal })(Animals);
