# Positivity Feature

## Having the Subjectivity from text input

class SubjectivityAnalyzer:
    
    def __init__(self,client):
        self.client = client
    
    def getSubjectivity(self,text=None,url=None,data=None):
        if url is not None:
            return self.__urlSubjectivity(url)
        elif text is not None:
            return self.__textSubjectivity(text)
        elif data is not None:
            return self.__dataSubjectivity(data)
        else:
            raise ValueError('Url or text must be provided')
        
    
    def __textSubjectivity(self, text):
        sentiment = self.client.Sentiment({"text": text})
        del sentiment['text'], sentiment['polarity'], sentiment['polarity_confidence']
        return sentiment
    
    ## Having the Subjectivity from URL input
    
    def __urlSubjectivity(self, url):
        sentiment = self.client.Sentiment({"url": url}) 
        del sentiment['text'], sentiment['polarity'], sentiment['polarity_confidence']
        return sentiment
    
    ## Having the Subjectivity from JSON input
    
    def __dataSubjectivity(self, data):
        data
        #TODO
        