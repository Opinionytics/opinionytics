import React, { Component } from 'react';
import '../../css/style.css';
import Footer from './footer.js';
import Header from './header.js'
import Form from './form.js'
import showResults from "./showResults";
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import Analytics from './analytics';
import MainNavBar from './mainNavBar';

class App extends Component {
  render() {
    return (
      <div className="App">
        <MainNavBar />
        <Header />
        <Form onSubmit={showResults}/>
        <Analytics />
        <Footer />
      </div>
    );
  }
}

export default App;
