from rest_framework.routers import SimpleRouter
from ViewSet12 import views



router = SimpleRouter()
router.register('books12', views.ViewSetBook12, basename='books')
urlpatterns = router.urls