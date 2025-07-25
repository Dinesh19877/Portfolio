from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import contact_form_submit

urlpatterns = [
    path('', views.homePage, name="homePage"),

    path('submit-form/', contact_form_submit, name='submit-form'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
