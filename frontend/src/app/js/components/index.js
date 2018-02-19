import React, { Component } from 'react';
import logo from '../../../logo.svg';
import '../../css/style.css';
import {createStore} from 'redux';
import allReducers from '../reducers';
import {Provider} from "react-redux";

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Opinionytics</h1>
        </header>
        <p className="App-intro">
          To get started, edit <b><code>src/app/js/components/index.js</code></b> and save to reload.
        </p>
      </div>
    );
  }
}

export default App;
