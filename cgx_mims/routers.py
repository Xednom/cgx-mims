from rest_framework import routers
from cgx.views import AgentViewSet, ManagerViewSet, BioConfirmMasterViewSet


router = routers.DefaultRouter()

router.register(r'agent', AgentViewSet)
router.register(r'manager', ManagerViewSet)
router.register(r'bio-confirm-master', BioConfirmMasterViewSet)
