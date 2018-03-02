import React from 'react';
import {Card, CardActions, CardTitle, CardText} from 'material-ui/Card'
import Dialog from 'material-ui/Dialog';
import FlatButton from 'material-ui/FlatButton';
import RaisedButton from 'material-ui/RaisedButton';

export default class Subjectivity extends React.Component{
    handleOpen = () => {
        const actions = [
            <FlatButton
                label="Ok"
                primary={true}
                keyboardFocused={true}
                onClick={this.handleClose}
            />,
        ];

        <Dialog
        title="Dialog With Actions"
        actions={actions}
        modal={false}
        open={this.state.open}
        onRequestClose={this.handleClose}
    >
The actions in this window were passed in as an array of React objects.
    </Dialog>
    };

    render(){
        
    return(
        <Card>
            <CardTitle title="Subjectivity" subtitle="The Subjectivity of the input text" />
            <CardText>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Donec mattis pretium massa. Aliquam erat volutpat. Nulla facilisi.
                Donec vulputate interdum sollicitudin. Nunc lacinia auctor quam sed pellentesque.
                Aliquam dui mauris, mattis quis lacus id, pellentesque lobortis odio.
            </CardText>

            <CardActions>
                <RaisedButton label="Help" onClick={this.handleOpen}>
                   
                </RaisedButton>
            </CardActions>

            
            
        </Card>

        
    );
    }
  }