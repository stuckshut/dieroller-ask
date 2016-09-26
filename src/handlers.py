import messages
from die_roller import parse_simple, parse_complex
from response import Response


def on_launch(request, session):
    return Response.create_ask_response(
        messages.get_welcome_response(),
        messages.get_welcome_response()
    )


def on_intent(request, session):
    if request.intent_name == 'DieRollSimple':
        result = parse_simple()
        return Response.create_tell_response(
            messages.get_die_roll_response()
        )

    elif request.intent_name == 'DieRollComplex':
        result = parse_complex()
        return Response.create_tell_response(
            messages.get_die_roll_response()
        )

    elif request.intent_name == 'AMAZON.HelpIntent':
        return Response.create_ask_response(
            messages.get_help_response() + ' ' + messages.get_prompt_response(),
            messages.get_prompt_response()
        )

    elif request.intent_name == 'AMAZON.StopIntent' or request.intent_name == 'AMAZON.CancelIntent':
        return Response.create_tell_response(
            messages.get_end_response()
        )

    # If we drop through all the intents, we probably failed somehow
    return on_error(request, session)


def on_session_ended(request, session):
    return Response.create_tell_response("")


def on_error(request, session):
    return Response.create_tell_response(messages.get_error_response())

