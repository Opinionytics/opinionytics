import React from 'react';
import CardTemplate from './CardTemplate';

export default class Subjectivity extends React.Component{
    render(){    
        return(
            <CardTemplate
                featureTitle = 'Subjectivity'
                featureSubtitle = 'The Subjectivity of the input text'
                featureDescription = 'We use Alien'
            >
                <SubjectivityGraph />
            </CardTemplate>
        );
    }
}

class SubjectivityGraph extends React.Component{
    render(){    
        return(
            <p>Insérer un graph ici.</p>
        );
    }
}