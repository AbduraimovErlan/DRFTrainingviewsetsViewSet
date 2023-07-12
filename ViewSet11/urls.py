from rest_framework.routers import SimpleRouter
from ViewSet11 import views




router = SimpleRouter()
router.register('books11', views.ViewSetBook11, basename='books')
urlpatterns = router.urls