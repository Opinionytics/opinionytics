import React from 'react';
import Topics from './Ana_comp/Topics.js'
import Popularity from './Ana_comp/Popularity.js'
import Subjectivity from './Ana_comp/Subjectivity.js'
import Polarity from './Ana_comp/Polarity.js'
import Summary from './Ana_comp/Summary.js'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';

export default class Analytics extends React.Component {
  render() {
    return (
      <MuiThemeProvider>
        <div id="anaCards">
          <Topics />
          <Popularity />
          <Subjectivity />
          <Polarity />
          <Summary />
        </div>
      </MuiThemeProvider>
    );
  }
}

