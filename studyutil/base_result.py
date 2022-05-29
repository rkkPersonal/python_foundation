
def data_response():
    data = {
        'code': 1,
        'message': 'success',
        'data': {
            "result": "good"
        }
    }
    return data


def result(file):
    response = {
        'code': 1,
        'message': 'success',
        'data': {
            "game": file.read()
        }
    }

    return response
