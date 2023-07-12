from ViewSet9 import views
from rest_framework.routers import SimpleRouter



router = SimpleRouter()
router.register('books9', views.ViewSetBook9, basename='books')
urlpatterns = router.urls

