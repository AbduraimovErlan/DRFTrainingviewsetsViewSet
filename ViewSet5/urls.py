from rest_framework.routers import SimpleRouter
from ViewSet5 import views



router = SimpleRouter()
router.register('books5', views.ViewSetBook5, basename='books')
urlpatterns = router.urls