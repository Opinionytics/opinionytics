# Summary Feature

## Summarize a text input

import json

### Summarize text input with sentences number


class SummaryGenerator:
    
    def __init__(self,client):
        self.client = client

    def getSummary(self,text=None,url=None,data=None,sentencesNumber=3,sentencesPercentage=None):
        if url is not None:
            if sentencesPercentage is not None:
                return self.__summaryUrlToPercentage(url,sentencesPercentage)
            else:
                return self.__summaryUrlToSentences(url,sentencesNumber)
        elif text is not None:
            if sentencesPercentage is not None:
                return self.__summaryTextToSentences(text,sentencesPercentage)
            else:
                return self.__summaryTextToPercentage(text,sentencesNumber)
        elif data is not None:
            #TODO
            return ""
        else:
            raise ValueError('Url or text must be provided')

    def __summaryTextToSentences(self, text, title=None, sentencesNumber=3):
        summary = self.client.Summarize({'text': text, 'title': title, 'sentences_number': sentencesNumber})
        result = ''
        for sentence in summary['sentences']:
            result += sentence + '\n'

        return result

    ### Summarize text input with sentences percentage

    def __summaryTextToPercentage(self, text, title=None, sentencesPercentage=10):
        summary = self.client.Summarize({'text': text, 'title': title, 'sentences_percentage': sentencesPercentage})
        result = ''
        for sentence in summary['sentences']:
            result += sentence + '\n'
        return result

    ## Summarize an URL input

    #### Summarize an URL input with sentences number

    def __summaryUrlToSentences(self, url, SENTENCES_NUMBER):
        summary = self.client.Summarize({'url': url, 'sentences_number': SENTENCES_NUMBER})
        result = ''
        for sentence in summary['sentences']:
            result += sentence + '\n'
        return result

    #### Summarize an URL input with sentences percentage

    def __summaryUrlToPercentage(self, url, SENTENCES_PERCENTAGE):
        summary = self.client.Summarize({'url': url, 'sentences_percentage': SENTENCES_PERCENTAGE})
        result = ''
        for sentence in summary['sentences']:
            result += sentence + '\n'
        return result

    ## Summarize a JSON input

    ### Summarize JSON input with sentences number

    def __summaryDataToSentences(self, data, SENTENCES_NUMBER):
        ""
        #TODO

    ### Summarize JSON input with sentences number

    def __summaryDataToPercentage(self, data, SENTENCES_PERCENTAGE):
        ""
        #TODO