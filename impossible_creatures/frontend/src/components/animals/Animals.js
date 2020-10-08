import React, { Component } from "react";
import { Link } from "react-router";

export class Animals extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading",
    };
  }

  componentDidMount() {
    fetch("api/animal")
      .then((response) => {
        if (response.status > 400) {
          return this.setState(() => {
            return { placeholder: "Something went wrong!" };
          });
        }
        return response.json();
      })
      .then((data) => {
        this.setState(() => {
          return {
            data,
            loaded: true,
          };
        });
      });
  }

  render() {
    return (
      <div>
        <h1>Animals list</h1>
        {this.state.data.map((animal) => {
          return (
            <ul className="list-group ">
              <li className="list-group-item" key={animal.id}>
                {animal.name}
                <br />({animal.species_name})
                <br /> -- Owned By {animal.owner_name}
                <br /> -- Created by {animal.creator_name}
              </li>
            </ul>
          );
        })}
      </div>
    );
  }
}

export default Animals;
