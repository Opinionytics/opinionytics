import React from 'react';
import CardTemplate from './CardTemplate';

export default class Popularity extends React.Component{
    render(){    
        return(
            <CardTemplate
                featureTitle = 'Popularity'
                featureSubtitle = 'Popularity of the input text'
                featureDescription = 'We use idk'
            >
                <p>5.56</p>
            </CardTemplate>
        );
    }
}