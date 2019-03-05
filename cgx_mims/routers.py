from rest_framework import routers
from cgx.views import (AgentViewSet, ManagerViewSet, 
                       BioConfirmMasterViewSet, StatusViewSet,
                       TestChoicesViewSet)
from carrier.views import CarrierViewSet
from dme.views import DMEIIViewSet
from insurance.views import InsuranceViewSet, TypeOfInsuranceViewSet
from paincreamandfootbath.views import PainCreamAndFootBathViewSet
from supplies.views import SupplyViewSet


router = routers.DefaultRouter()

router.register(r'agent', AgentViewSet)
router.register(r'manager', ManagerViewSet)
router.register(r'status', StatusViewSet)
router.register(r'test-choices', TestChoicesViewSet)
router.register(r'bio-confirm-master', BioConfirmMasterViewSet, base_name="BioConfirmMaster")
router.register(r'carrier', CarrierViewSet, base_name="Carrier")
router.register(r'dme', DMEIIViewSet, base_name="DME_II")
router.register(r'type-of-insurance', TypeOfInsuranceViewSet)
router.register(r'insurance', InsuranceViewSet, base_name="Insurance")
router.register(r'pain-cream-and-foot-bath', PainCreamAndFootBathViewSet, base_name="PainCreamAndFootBath")
router.register(r'supplies', SupplyViewSet)