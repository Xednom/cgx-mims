from import_export import resources
from .models import BioConfirmMaster


class BioConfirmMasterResource(resources.ModelResource):
    class Meta:
        model = BioConfirmMaster
