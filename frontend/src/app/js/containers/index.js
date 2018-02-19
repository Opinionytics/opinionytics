import React, {Component} from 'react';
import {bindActionCreators} from 'redux';
import {connect} from 'react-redux';

class Containers extends Component {

    func() {
        return this.props.users.map((user) => {
            return(
                //TODO
            );
        });
    }
    render(){
        return (
            <ul>
                {this.func()}
            </ul>
        );
    }
}
function mapStateToProps(state){
    return{
        //TODO
    }; 
}

export default connect(mapStateToProps)(UserList)