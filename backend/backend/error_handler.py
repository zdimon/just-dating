from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['status'] = 1
        response.data['info'] = str(context['view'])

    return response