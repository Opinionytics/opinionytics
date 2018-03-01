import React, { Component } from 'react';
import '../../css/style.css';
import Footer from './footer.js';
import Header from './header.js'
import Form from './form.js'


class App extends Component {
  render() {
    return (
      <div className="App">
        <Header />
        <Form />
        <Footer />
      </div>
    );
  }
}

export default App;
