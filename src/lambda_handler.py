from __future__ import print_function

from request import Request, Session
from handlers import on_launch, on_intent, on_session_ended, on_error


def lambda_handler(event, context):

    session = Session(event['session'])
    request = Request(event['request'])

    if session.applicationId != '':
        handler = on_error
    elif request.type == 'LaunchRequest':
        handler = on_launch
    elif request.type == 'IntentRequest':
        handler = on_intent
    elif request.type == 'SessionEndedRequest':
        handler = on_session_ended
    else:
        handler = on_error

    return handler(request, session).to_dict()
