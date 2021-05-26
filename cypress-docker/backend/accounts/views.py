from django.contrib.auth import get_user_model
from django.core.serializers import serialize
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

CUSTOM_USER = get_user_model()


@csrf_exempt
def create_user(request):
    if request.method != "POST":
        return JsonResponse({"data": "Only POST method allowed!"})
    data = request.POST
    user = CUSTOM_USER.objects.create_user(
        email=data.get("email"), password=data.get("password")
    )
    return JsonResponse({"user": serialize("json", [user])})
