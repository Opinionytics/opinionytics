import React from 'react';
import {Card, CardActions, CardTitle, CardText} from 'material-ui/Card'
import Dialog from 'material-ui/Dialog';
import FlatButton from 'material-ui/FlatButton';
import RaisedButton from 'material-ui/RaisedButton';

export default class CardTemplate extends React.Component{
    state = {
        open: false,
    };

    handleOpen = () => {
        this.setState({open: true});
    };
    
    handleClose = () => {
        this.setState({open: false});
    };

    render(){
        const actions = [
            <FlatButton
                label="Ok"
                primary={false}
                keyboardFocused={true}
                onClick={this.handleClose}
            />,
        ];
        
        return(
            <Card>
                <CardTitle title={this.props.featureTitle} subtitle={this.props.featureSubtitle} />
                <CardText>
                    {this.props.children}
                </CardText>

                <CardActions>
                    <RaisedButton label="Help" onClick={this.handleOpen} />

                    <Dialog
                        title="What is it ?"
                        actions={actions}
                        modal={false}
                        open={this.state.open}
                        onRequestClose={this.handleClose}
                    >
                        {this.props.featureDescription}
                    </Dialog>
                </CardActions>
            </Card>        
        );
    }
}