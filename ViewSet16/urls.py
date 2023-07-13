from rest_framework.routers import SimpleRouter
from ViewSet16 import views



router = SimpleRouter()
router.register('books16', views.ViewSetBook16, basename='books')
urlpatterns = router.urls