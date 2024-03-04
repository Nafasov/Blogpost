from django.urls import path


from .views import home_api_view, contact_api_view


app_name = 'main-api'


urlpatterns = [
    path('list/', home_api_view, name='list'),
    path('contact/', contact_api_view, name='contact')
]
