import React from 'react';
import ReactDOM from 'react-dom';
import App from './app/index.js';
import registerServiceWorker from './registerServiceWorker';
import {createStore} from 'redux';
import allReducers from './app/js/reducers/index.js';
import {Provider} from "react-redux";

const store = createStore(allReducers);

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>, 
    document.getElementById('root'));
registerServiceWorker();
