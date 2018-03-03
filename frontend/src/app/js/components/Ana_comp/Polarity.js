import React from 'react';
import CardTemplate from './CardTemplate';

export default class Polarity extends React.Component{
    render(){    
        return(
            <CardTemplate
                featureTitle = 'Polarity'
                featureSubtitle = 'The polarity of the input text'
                featureDescription = 'We use idk'
            >
                <p>0.1</p>
            </CardTemplate>
        );
    }
}