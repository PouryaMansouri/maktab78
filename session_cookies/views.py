from django.shortcuts import render, HttpResponse


def set_cookie(request):
    response = HttpResponse('Cookie set')
    response.set_cookie('name', 'Akbar')
    response.set_cookie('name2', 'Akbar2')
    return response


def get_cookie(request):
    name = request.COOKIES.get('name2', 'Guest')
    return HttpResponse(name)


def set_session(request):
    request.session['name'] = 'Akbar'
    request.session['name2'] = 'Akbar_session2'
    return HttpResponse('Session set')


def get_session(request):
    name = request.session.get('name', 'Guest')
    return HttpResponse(name)


def is_akbar(request):
    name = request.session.get('name', 'Guest')
    if name == 'Akbar':
        return HttpResponse('Hello Akbar')
    else:
        return HttpResponse('Hello Guest')




#
# # Create your views here.
#
#
# def set_cookie(request):
#     response = HttpResponse("Cookie Set")
#     response.set_cookie('name', 'Akbar')
#     return response
#
#
# def get_cookie(request):
#     name = request.COOKIES['name']
#     return HttpResponse(name)
#
#
# def set_session(request):
#     request.session['name'] = 'Akbar'
#     # expire in 10 seconds
#     request.session.set_expiry(10)
#     # set name ali to session with 20 seconds expire
#     request.session['ali'] = 'ali'
#     request.session.set_expiry(20)
#     return HttpResponse("Session Set")
#
#
# def get_session(request):
#     name = request.session['name']
#     return HttpResponse(name)
#
#
# def is_akbar(request):
#     name = request.session['name']
#     if name == 'Akbar':
#         return HttpResponse('Yes')
#     else:
#         return HttpResponse('No')
#
#
def read_request_data(request):
    print("start")
    print(request.META)
    # ip
    print("-----------------")
    print(request.META['REMOTE_ADDR'])
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.path)
    print(request.method)
    # session
    print('------session------')
    print(request.session)
    print(request.session.session_key)
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    print(request.session.get('name'))
    print(request.session.get('ali', 'default'))
    # cookies
    print('------cookies------')
    print(request.COOKIES)
    print(request.COOKIES.get('name'))
    print(request.COOKIES.get('ali', 'default'))
    print(request.COOKIES.get('name', 'default'))
    print("end")
    return HttpResponse('Done')
