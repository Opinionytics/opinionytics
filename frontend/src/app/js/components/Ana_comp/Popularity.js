import React from 'react';
import {Card, CardTitle, CardText} from 'material-ui/Card'
export default class Popularity extends React.Component{
    render(){
      return(
        <Card>
            <CardTitle title="Positivity" subtitle="The positivity of the input text" />
            <CardText>
                <p>10%</p>
            </CardText>
        </Card>
      );
    }
}