# Positivity Feature

## Having the Positivity from text input

class PositivityAnalyzer:
    
    def __init__(self,client):
        self.client = client
    
    def getPositivity(self,text=None,url=None,data=None):
        if url is not None:
            return self.__urlPositivity(url)
        elif text is not None:
            return self.__textPositivity(text)
        elif data is not None:
            return self.__dataPositivity(data)
        else:
            raise ValueError('Url or text must be provided')
    
    def __textPositivity(self, text):
        sentiment = self.client.Sentiment({"text": text})
        del sentiment['text'], sentiment['subjectivity'], sentiment['subjectivity_confidence']
        return sentiment

    ## Having the Positivity from url input

    def __urlPositivity(self, url):
        sentiment = self.client.Sentiment({"url": url})
        del sentiment['text'], sentiment['subjectivity'], sentiment['subjectivity_confidence']
        return sentiment

    ## Having the Positivity from JSON input

    def __dataPositivity(self, data):
        # TODO
        for text in data:
            self.__textPositivity(text.get('text'))