"""
Build a response object to send back to Alexa
"""


class Response(object):

    def __init__(self):
        self.version = '1.0'
        self.sessionAttributes = None
        self.shouldEndSession = True
        self.outputSpeech = {
            'type': 'string',
            'text': 'Default Response'
        }
        self.card = None
        self.promptSpeech = None
        """
        self.card = {
            "type": "string",
            "title": "string",
            "content": "string",
            "text": "string",
            "image": {
                "smallImageUrl": "string",
                "largeImageUrl": "string"
            }
        }
        """

    @classmethod
    def create_tell_response(cls, message):
        response = Response()
        response.outputSpeech = cls.build_message(message)
        response.shouldEndSession = True

        return response

    @classmethod
    def create_ask_response(cls, message, prompt):
        response = Response()
        response.outputSpeech = cls.build_message(message)
        prompt_speech = cls.build_message(prompt)
        response.promptSpeech = {
            'outputSpeech': prompt_speech
        }
        response.shouldEndSession = False

        return response

    def to_dict(self):
        out = dict({
            "version": self.version,
            "response": {
                "shouldEndSession": self.shouldEndSession
            }
        })
        if self.outputSpeech is not None:
            out['response']['outputSpeech'] = self.outputSpeech

        if self.card is not None:
            out['response']['card'] = self.card

        if self.promptSpeech is not None:
            out['response']['reprompt'] = self.promptSpeech

        if self.sessionAttributes is not None:
            out['sessionAttributes'] = self.sessionAttributes

        return out

    def create_card(self,
                    card_type=None,
                    title=None,
                    content=None,
                    text=None,
                    image_small=None,
                    image_large=None):
        pass

    @staticmethod
    def build_message(message):
        if message.find('pu-erh') is not -1:
            message = message.replace('pu-erh', '<say-as>poo-air</say-as>')
            outputSpeech = {
                'type': 'SSML',
                'ssml': '<speak>' + message + '</speak>'
            }
        else:
            outputSpeech = {
                'type': 'PlainText',
                'text': message
            }
        return outputSpeech
