import React from 'react';
import TextField from 'material-ui/TextField';
import PasswordField from 'material-ui-password-field';
import RaisedButton from 'material-ui/RaisedButton';

const style = {
  margin: 12,
};

class SignUpPage extends React.Component {
  render() {
    return (
      <div>
        <TextField
          hintText="Username"
          errorText="This username already exists"
        /><br />
        <TextField
          hintText="First name"
        /><br />
        <TextField
          hintText="Surname"
        /><br />
        <TextField
          hintText="Mobile number or email address"
          errorText="This mobile number/email address already exists"
        /><br />
        <PasswordField
          hintText="At least 8 characters"
          floatingLabelText="Password"
          errorText="Your password is too short"
        /><br />
        <PasswordField
          floatingLabelText="Password confirmation"
          errorText="The passwords entered are different"
        /><br />

        <RaisedButton label="Submit" style={style} />
      </div>

    )
  }
}

export default SignUpPage;