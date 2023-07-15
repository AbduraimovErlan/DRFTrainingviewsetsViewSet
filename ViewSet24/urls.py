from rest_framework.routers import SimpleRouter
from ViewSet24 import views




router = SimpleRouter()
router.register('books24', views.ViewSetBook24, basename='books')
urlpatterns = router.urls