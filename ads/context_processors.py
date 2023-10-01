from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse

def cp_setting(request):
    #print(settings)
    return {"settings": settings}

def csrf_failure(request, reason=""):
    #ctx = {'content': request.POST, "message": request.COOKIES, "meta":request.META,"body":request.body}
    ctx={'content': request.POST, "message": request.COOKIES}
    print(request.META[settings.CSRF_HEADER_NAME])
    return JsonResponse(ctx)