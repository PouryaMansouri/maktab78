from django.urls import path
from .views import (
    set_cookie,
    get_cookie,
set_session,
get_session,
is_akbar,
read_request_data
)

app_name = 'session_cookies'
urlpatterns = [
    path('set_cookie/', set_cookie, name='set_cookie_akbar'),
    path('get_cookie/', get_cookie, name='get_cookie_akbar'),
    path('set_session/', set_session, name='set_session_akbar'),
    path('get_session/', get_session, name='get_session_akbar'),
    path('is_akbar/', is_akbar, name='is_akbar'),
    path('read_request_data/', read_request_data, name='read_request_data'),
    ]























#
# app_name = 'session_cookies'
# urlpatterns = [
#     # path('set_cookie/', set_cookie, name='set_cookie'),
#     # path('get_cookie/', get_cookie, name='get_cookie'),
#     # path('set_session/', set_session, name='set_session'),
#     # path('get_session/', get_session, name='get_session'),
#     # path('is_akbar/', is_akbar, name='is_akbar'),
#     # path('read_request_data/', read_request_data, name='read_request_data'),
#     ]
