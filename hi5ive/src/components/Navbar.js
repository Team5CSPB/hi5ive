import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import { Input, Menu } from 'semantic-ui-react';

export default class Navar extends Component {
  state = { activeItem: 'home' };

  handleItemClick = (e, { name }) => this.setState({ activeItem: name });

  render() {
    const { activeItem } = this.state;
    const { user } = this.props;

    return (
      <Menu secondary>
        <Menu.Item
          as={Link}
          to="/"
          name="home"
          active={activeItem === 'home'}
          onClick={this.handleItemClick}
        />
        <Menu.Item
          as={Link}
          to="/users"
          name="5ivers"
          active={activeItem === '5ivers'}
          onClick={this.handleItemClick}
        />
        <Menu.Item
          as={Link}
          to="/my-profile"
          name="my-profile"
          active={activeItem === 'my-profile'}
          onClick={this.handleItemClick}
        />
        <Menu.Menu position="right">
          <Menu.Item>
            <Input icon="search" placeholder="Find Matches..." />
          </Menu.Item>
          <Menu.Item
            name="logout"
            active={activeItem === 'logout'}
            onClick={this.handleItemClick}
          />
        </Menu.Menu>
      </Menu>
    );
  }
}
