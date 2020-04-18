from django.urls import include, path
from accounts import views as accounts_views



urlpatterns = [
    path('', accounts_views.UserUpdateView.as_view(), name='signup'),
    path('settings/account/', accounts_views.UserUpdateView.as_view(), name='my_account'),
]

