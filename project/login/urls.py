from django.urls import path
from .views import login, signup, submit, home, voting


urlpatterns = [
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
    path('submit/', submit, name='submit'),
    path('home/', home, name='home'),
    path('voting/', voting, name='voting'),
]