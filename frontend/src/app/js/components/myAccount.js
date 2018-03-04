import React from 'react';
import TextField from 'material-ui/TextField';
import { NavLink } from "react-router-dom";

class MyAccount extends React.Component {
	render() {
		return (
			<ul className="header">
                <TextField
                    hintText="Input Text"
                />
                <li><NavLink to="/profile">Profile</NavLink></li>
            </ul>
		);
	}
}

export default  MyAccount;