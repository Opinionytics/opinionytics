# Topics Involved Feature

## Classifying text from a string input 

class TopicClassifier:
    
    def __init__(self, client):
        self.client = client

    def getTopics(self, text=None, url=None, data=None):
        if url is not None:
            return self.__classifyUrl(url)
        elif text is not None:
            return self.__classifyText(text)
        elif data is not None:
            #TODO
            ""
        else:
            raise ValueError('Url or text must be provided')

    def __classifyText(self, text):
        classifications = self.client.Classify({"text": text})
        for i in classifications["categories"]:
            del i["code"] # delete the code field of the json object
        return classifications["categories"]
    
    ## Classifying Text from An URL
    
    def __classifyUrl(self, url):
        classifications = self.client.Classify({"url": url})
        for i in classifications["categories"]:
            del i["code"] # delete the code field of the json object
        return classifications['categories']
    
    ## Classifying data from a file input
    
    def __classifyData(self, data):
        ""
        #TODO
            

