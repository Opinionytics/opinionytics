import React, { Component } from 'react';
import logo from '../../../logo.svg';
import '../../css/style.css';
class Footer extends Component {
    render() {
      return (
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Opinionytics</h1>
        </header>
      );
    }
}

export default Footer;