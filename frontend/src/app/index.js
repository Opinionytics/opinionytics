import React, { Component } from 'react';
import './css/style.css';
import Footer from './js/components/footer.js';
import Header from './js/components/header.js'
import Form from './js/components/form.js'
import showResults from "./js/components/showResults";
import getMuiTheme from 'material-ui/styles/getMuiTheme';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
// import Analytics from './js/components/analytics';
import MainNavBar from './js/components/mainNavBar';

class App extends Component {
  render() {
    return (
      <div className="App">
        <MainNavBar />
        <Header />
        <section>
          <Form onSubmit={showResults}/>
          {/* <Analytics /> */}
        </section>
        <Footer />
      </div>
    );
  }
}

export default App;
