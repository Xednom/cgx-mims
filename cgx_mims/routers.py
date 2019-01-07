from rest_framework import routers
from cgx.viewset import AgentViewSet, ManagerViewSet, BioConfirmMasterViewSet


router = routers.DefaultRouter()

router.register(r'agent', AgentViewSet)
router.register(r'manager', ManagerViewSet)
router.register(r'bioconfirmmaster', BioConfirmMasterViewSet)
