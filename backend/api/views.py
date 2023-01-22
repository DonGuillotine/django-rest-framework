import json
from django.http import JsonResponse

def api_view(request):
    # This returns a byte string of json data
    body = request.body
    data = {}
    try:
        # It needs to be converted to a Python Dictionary
        data = json.loads(body)
    except:
        pass
    print(data)
    return JsonResponse(data)