import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getSpecies } from "../../actions/animals";

export class Species extends Component {
  static propTypes = {
    species: PropTypes.array.isRequired,
    getSpecies: PropTypes.func.isRequired,
  };

  componentDidMount() {
    this.props.getSpecies()
  }
  render() {
    
    return (
      <Fragment>
        <h2>Animals</h2>
        <table className="table table-striped">
          <thead>
            <tr>
              <th>Name</th>
			  <th>Parent 1</th>
			  <th>Parent 2</th>
			  <th>Creator</th>
            </tr>
          </thead>
          <tbody>
            {this.props.species.map((animal) => (
              <tr key={animal.id}>
                <td>{animal.name ? animal.name : "None"}</td>
				<td>{animal.parent1}</td>
				<td>{animal.parent2}</td>
				<td>{animal.creator}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </Fragment>
    );
  }
}

const mapStateToProps = (state) => ({
  species: state.animalsReducer.animals,
});

export default connect(mapStateToProps, { getSpecies })(Species);
