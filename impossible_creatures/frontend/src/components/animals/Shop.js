import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getTransactions } from "../../actions/animals";


export class Shop extends Component {
  static propTypes = {
    animals: PropTypes.array.isRequired,
    getTransactions: PropTypes.func.isRequired,
  };

  componentDidMount() {
    this.props.getTransactions()
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
	              <tr key={animal.animal_id}>
	                <td>{animal.price}</td>
	                <td>{animal.date_sell_start}</td>
	                <td>{animal.seller_id}</td>
	                <td>
	                </td>
	              </tr>
	            ))}
	          </tbody>
	        </table>
	    </Fragment>
		)
	}
}

const mapStateToProps = (state) => ({
  animals: state.animalsReducer.animals
});

export default connect(mapStateToProps, { getTransactions })(Shop)
