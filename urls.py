from django.urls import path
from django.views.generic import RedirectView
from gaushala_django import views

urlpatterns = [
    path('', RedirectView.as_view(url='/login/')),
    path('home/', RedirectView.as_view(url='/home/')),
    path('cattle_management_overview/', RedirectView.as_view(url='/cattle_management_overview/')),

    # Other URL patterns
]