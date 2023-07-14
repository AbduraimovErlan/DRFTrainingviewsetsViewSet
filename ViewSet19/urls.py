from rest_framework.routers import SimpleRouter
from ViewSet19 import views


router = SimpleRouter()
router.register('books19', views.ViewSetBook19, basename='books')
urlpatterns = router.urls