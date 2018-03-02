import React from 'react';
import ReactDOM from 'react-dom';
import Topics from './components/Topics.js'
import Popularity from './components/Popularity.js'
import Subjectivity from './components/Subjectivity.js'
import Polarity from './components/Polarity.js'
import Summary from './components/Summary.js'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

export default class Analytics extends React.Component {
  render() {
    return (
      <MuiThemeProvider>
          <Topics />
          <Popularity />
          <Subjectivity />
          <Polarity />
          <Summary />
      </MuiThemeProvider>
    );
  }
}

