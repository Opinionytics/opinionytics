import React from 'react';
import {Card, CardTitle, CardText} from 'material-ui/Card'
export default class Popularity extends React.Component{
    render(){
      return(
        <Card>
            <CardTitle title="Positivity" subtitle="The positivity of the input text" />
            <CardText>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Donec mattis pretium massa. Aliquam erat volutpat. Nulla facilisi.
                Donec vulputate interdum sollicitudin. Nunc lacinia auctor quam sed pellentesque.
                Aliquam dui mauris, mattis quis lacus id, pellentesque lobortis odio.
            </CardText>
        </Card>
      );
    }
}