import React from 'react';
import CardTemplate from './CardTemplate';

export default class Summary extends React.Component{
    render(){    
        return(
            <CardTemplate
                featureTitle = 'Summary'
                featureSubtitle = 'The summary of the input text'
                featureDescription = 'We use idk'
            >
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                Donec mattis pretium massa. Aliquam erat volutpat. Nulla facilisi.
                Donec vulputate interdum sollicitudin. Nunc lacinia auctor quam sed pellentesque.
                Aliquam dui mauris, mattis quis lacus id, pellentesque lobortis odio.</p>
            </CardTemplate>
        );
    }
}