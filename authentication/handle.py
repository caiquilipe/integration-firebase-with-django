def get_errors(errors: dict):
    responses = []
    for values in errors.values():
        for value in values:
            responses.append(value)
    return responses
    