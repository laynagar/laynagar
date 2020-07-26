from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from .views import IndexView, PortfolioView1, PortfolioView2, Contact, About


app_name = 'Gallery'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('portfolio1/', PortfolioView1.as_view(), name='portfolio-1'),
    path('portfolio2/', PortfolioView2.as_view(), name='portfolio-2'),
    path('contact/', Contact.as_view(), name='contact'),
    path('about/', About.as_view(), name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 