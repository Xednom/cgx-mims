from import_export import resources
from import_export.fields import Field
from .models import Agent, BioConfirmMaster, Manager


class BioConfirmMasterResource(resources.ModelResource):
    patient_name = Field(attribute="patient_name", column_name="PATIENT'S NAME")
    patient_phone_number = Field(attribute="patient_phone_number", column_name="PATIENT'S PHONE NUMBER")
    promo_code = Field(attribute="promo_code", column_name="PROMO CODE")
    agent = Field(attribute="agent", column_name="AGENT")
    date_app_rec = Field(attribute="date_app_rec", column_name="DATE APP REC'D")
    date_sample_rec = Field(attribute="date_sample_rec", column_name="DATE SAMPLE REC'D")
    type_of_test = Field(attribute="type_of_test", column_name="TYPE OF TEST")
    date_of_qca = Field(attribute="date_of_qca", column_name="DATE OF QCA")
    submitted_to_tamika_ins_verifier = Field(attribute="submitted_to_tamika_ins_verifier",
                                             column_name="SUBMITTED TO TAMIKA/INS. VERIFIER")
    telemed_name = Field(attribute="telemed_name", column_name="TELEMED NAME")
    date_submitted_to_telemed = Field(attribute="date_submitted_to_telemed", column_name="DATE SUBMITTED TO TELEMED")
    date_telemed_returned = Field(attribute="date_telemed_returned", column_name="DATE TELEMED RETURNED")
    date_bioconfim_rec_app = Field(attribute="date_bioconfim_rec_app", column_name="DATE LAB REC'D APP")
    date_paid = Field(attribute="date_paid", column_name="DATE PAID")
    state = Field(attribute="state", column_name="STATE")
    status = Field(attribute="status", column_name="STATUS")
    month = Field(attribute="month", column_name="MONTH")
    insurance_company = Field(attribute="insurance_company", column_name="INSURANCE COMPANY")
    notes = Field(attribute="notes", column_name="NOTES")
    rejection_date = Field(attribute="rejection_date", column_name="REJECTIONS DATE")

    class Meta:
        model = BioConfirmMaster
        fields = ['agent__name']
        exclude = ('id',)


class AgentResource(resources.ModelResource):
    name = Field(attribute="name", column_name="AGENT")

    class Meta:
        model = Agent
        exclude = ['id', 'agent__name']
