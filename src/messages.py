welcome = ""
help_msg = "I can roll dice based on a simple structure describing the dice and modifiers. " +
           "For example, you can say 4 D 20 plus 2 to roll 4 20 sided dice and add two to the result. " +
           "Or, you can say 4 D 6 drop lowest 1 to roll 4 six sided dice and drop the lowest result."
error = "I'm sorry, I have encountered an error, try again."
prompt_msg = "How many dice would you like me to roll?"
end_session = "Goodbye."


def get_welcome_response():
    return welcome


def get_error_response():
    return error


def get_help_response():
    return help_msg.format


def get_prompt_response():
    return prompt_msg


def get_end_response():
    return end_session
