from rest_framework import routers
from cgx.views import AgentViewSet, ManagerViewSet, BioConfirmMasterViewSet
from carrier.views import CarrierViewSet
from dme.views import DMEIIViewSet
from insurance.views import InsuranceViewSet


router = routers.DefaultRouter()

router.register(r'bio-confirm-master', BioConfirmMasterViewSet)
router.register(r'carrier', CarrierViewSet)
router.register(r'dme', DMEIIViewSet)
router.register(r'insurance', InsuranceViewSet)
