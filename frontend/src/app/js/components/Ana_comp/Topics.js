import React from 'react';
import CardTemplate from './CardTemplate';

export default class Topics extends React.Component{
    render(){    
        return(
            <CardTemplate
                featureTitle = 'Topics'
                featureSubtitle = 'The topics of the input text'
                featureDescription = 'We use idk'
            >
                <ul>
                  <li>News</li>
                  <li>Business</li>
                  <li>World</li>
                </ul>
            </CardTemplate>
        );
    }
}