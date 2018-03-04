import React from 'react';
import SignInPage from './signUpPage.js';
import LogInPage from './logInPage.js';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
//import '../css/style.css';
import {
	Route,
	NavLink,
	HashRouter
  } from "react-router-dom";

export default class mainNavBar extends React.Component {
	render() {
		return (
			<div>
				<HashRouter>
					<div>
						<ul className="header">
							<li><NavLink to="/">Home</NavLink></li>
							<li><NavLink to="/login">Log in</NavLink></li>
							<li><NavLink to="/signup">Sign up</NavLink></li>
						</ul>
						<div className="content">
							<MuiThemeProvider>
								<Route path="/login" component={LogInPage}/>
							</MuiThemeProvider>
							<MuiThemeProvider>
								<Route path="/signup" component={SignInPage}/>
							</MuiThemeProvider>
						</div>
					</div>
				</HashRouter>
			</div>
		);
	}
}

