from rest_framework.routers import SimpleRouter
from ViewSet27 import views

router = SimpleRouter()
router.register('books27', views.ViewSetBook27, basename='books')
urlpatterns = router.urls