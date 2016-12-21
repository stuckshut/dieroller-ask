import messages
import dice
from response import Response


def on_launch(request, session):
    return Response.create_ask_response(
        messages.get_welcome_response(),
        messages.get_welcome_response()
    )


def on_intent(request, session):
    if request.intent_name == 'DieRollSimple':
        num_dice = 1
        if 'NumDice' in request.slots.keys():
            num_dice = request.slots['NumDice'].get('value')
        if 'DieType' in request.slots.keys():
            die_type = request.slots['DieType'].get('value')
        else:
            return on_error(request, session)
        roll = {"num": num_dice,
                "sides": die_type,
                "result": sum(dice.roll(str(num_dice) + "d" + str(die_type)))
                }
        return Response.create_tell_response(
            messages.get_die_roll_response(roll)
        )

    # elif request.intent_name == 'DieRollComplex':
    #     result = parse_complex()
    #     return Response.create_tell_response(
    #         messages.get_die_roll_response(result)
    #     )

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

