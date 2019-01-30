from rest_framework import routers
from cgx.views import AgentViewSet, ManagerViewSet, BioConfirmMasterViewSet
from carrier.views import CarrierViewSet
from dme.views import DMEIIViewSet
from insurance.views import InsuranceViewSet


router = routers.DefaultRouter()

router.register(r'agent', AgentViewSet)
router.register(r'manager', ManagerViewSet)
router.register(r'bio-confirm-master', BioConfirmMasterViewSet, base_name="BioConfirmMaster")
router.register(r'carrier', CarrierViewSet, base_name="Carrier")
router.register(r'dme', DMEIIViewSet)
router.register(r'insurance', InsuranceViewSet, base_name="Insurance")
