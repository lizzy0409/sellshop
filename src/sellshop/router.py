from product.viewsets import CategoryViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', CategoryViewset)

