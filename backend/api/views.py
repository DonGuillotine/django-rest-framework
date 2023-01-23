import json
from django.http import JsonResponse

def api_view(request):
    # This returns a byte string of json data
    # The sent data is captured using request.body
    body = request.body
    data = {}
    try:
        # It needs to be converted to a Python Dictionary
        data = json.loads(body)
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse(data)