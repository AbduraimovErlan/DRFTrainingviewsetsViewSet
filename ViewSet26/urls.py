from rest_framework.routers import SimpleRouter
from ViewSet26 import views




router = SimpleRouter()
router.register('books26', views.ViewSetBook26, basename='books')
urlpatterns = router.urls