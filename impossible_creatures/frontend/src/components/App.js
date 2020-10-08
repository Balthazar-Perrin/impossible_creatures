import React, { Component, Fragment } from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import ReactDOM from "react-dom";

import Header from "./layout/Header";
import Animals from "./animals/Animals";
import AnimalDetails from "./animals/AnimalDetails";

class App extends Component {
  render() {
    return (
      <Fragment>
        <div className="container">
          <Router>
            <Header />
            <Switch>
              <Route path="/" exact component={() => <Animals />} />
              <Route
                path="/animal/:animalId"
                component={() => <AnimalDetails />}
              />
            </Switch>
          </Router>
        </div>
      </Fragment>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
