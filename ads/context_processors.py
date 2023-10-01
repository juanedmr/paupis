from django.conf import settings

def cp_setting(request):
    #print(settings)
    return {"settings": settings}
