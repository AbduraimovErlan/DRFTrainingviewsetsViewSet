from ViewSet2 import views
from rest_framework.routers import SimpleRouter
from ViewSet2.views import ViewSetBook2

router = SimpleRouter()
router.register('books2', views.ViewSetBook2, basename='books')
urlpatterns = router.urls