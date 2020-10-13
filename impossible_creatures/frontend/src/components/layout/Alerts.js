import React, { Component, Fragment } from 'react';
import { withAlert } from 'react-alert';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';

export class Alerts extends Component {
  static propTypes = {
    error: PropTypes.object.isRequired,
    message: PropTypes.object.isRequired,
  }
  

  componentDidUpdate(prevProps) {
    const { error, alert, message } = this.props;
    if (error !== prevProps.error) {
      if(error.msg.name) alert.error(`Name: ${error.msg.name.join()}`)
      if(error.msg.creator_id) alert.error(`Creator: ${error.msg.creator_id.join()}`)
      if(error.msg.owner_id) alert.error(`Owner: ${error.msg.owner_id.join()}`)
      if(error.msg.species_id) alert.error(`Species: ${error.msg.species_id.join()}`)
    }
    
    if(message !== prevProps.message) {
      if(message.deleteAnimal) alert.success(message.deleteAnimal)
      if(message.addAnimal) alert.success(message.addAnimal)
    }
  }

  render() {
    return <Fragment />;
  }
}

const mapStateToProps = state => ({
  error: state.errors,
  message: state.messages
});

export default connect(mapStateToProps)(withAlert()(Alerts));