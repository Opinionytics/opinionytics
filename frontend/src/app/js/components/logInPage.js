import React from 'react';
import TextField from 'material-ui/TextField';
import PasswordField from 'material-ui-password-field';
import RaisedButton from 'material-ui/RaisedButton';
//import { withRouter } from 'react-router-dom';
import {
	Route,
	NavLink,
	HashRouter
  } from "react-router-dom";

import MyAccount from './myAccount';

const style = {
  margin: 12,
};

/*
const Butt = withRouter(({ history }) => (
  <RaisedButton
    label="Log In"
    type='button'
    onClick={() => { history.push('./myAccoun') }}
  />
))*/

class LogInPage extends React.Component {
	render() {
		return (
      <div>
        <TextField
          hintText="Username"
        /><br />
        <PasswordField
          floatingLabelText="Password"
        /><br />
        
        <HashRouter>
          <div>
            <NavLink to="/account"><RaisedButton label="Log In" /></NavLink>

            <div className="content">
                  <Route path="/account" component={MyAccount}/>
            </div>
          </div>
        </HashRouter>
      </div>
    )
  }
}

export default LogInPage;