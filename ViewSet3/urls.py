from django.urls import path
from ViewSet3 import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books3', views.ViewSetBook3, basename='books')
urlpatterns = router.urls
