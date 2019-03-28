from import_export import resources
from import_export.fields import Field
from .models import Agent, BioConfirmMaster, Manager


class BioConfirmMasterResource(resources.ModelResource):
    id = Field(attribute="id", column_name="ID")
    patient_name = Field(attribute="patient_name", column_name="PATIENT'S NAME")
    patient_phone_number = Field(attribute="patient_phone_number", column_name="PATIENT'S PHONE NUMBER")
    promo_code = Field(attribute="promo_code", column_name="PROMO CODE")
    agent = Field(attribute="agent", column_name="AGENT")
    manager = Field(attribute="manager", column_name="MANAGER")
    date_app_rec = Field(attribute="date_app_rec", column_name="DATE APP REC'D")
    date_sample_rec = Field(attribute="date_sample_rec", column_name="DATE SAMPLE REC'D")
    type_of_test = Field(attribute="type_of_test", column_name="TYPE OF TEST")
    date_of_qca = Field(attribute="date_of_qca", column_name="DATE OF QCA")
    insurance_verified_tsg_verification = Field(attribute="insurance_verified_tsg_verification",
                                             column_name="INSURANCE VERIFIED/TSG VERIFICATION")
    telemed_name = Field(attribute="telemed_name", column_name="TELEMED NAME")
    date_submitted_to_telemed = Field(attribute="date_submitted_to_telemed", column_name="DATE SUBMITTED TO TELEMED")
    date_telemed_returned = Field(attribute="date_telemed_returned", column_name="DATE TELEMED RETURNED")
    date_bioconfim_rec_app = Field(attribute="date_bioconfim_rec_app", column_name="DATE LAB REC'D APP")
    date_paid = Field(attribute="date_paid", column_name="DATE PAID")
    date_lab_recorded_app = Field(attribute="date_lab_recorded_app", column_name="DATE LAB RECORDED APP")
    lab_type = Field(attribute="lab_type", column_name="LAB TYPE")
    state = Field(attribute="state", column_name="STATE")
    status = Field(attribute="status", column_name="STATUS")
    month = Field(attribute="month", column_name="MONTH")
    insurance_company = Field(attribute="insurance_company", column_name="INSURANCE COMPANY")
    notes = Field(attribute="notes", column_name="NOTES")
    rejection_date = Field(attribute="rejection_date", column_name="REJECTIONS DATE")
    patient_id_photo = Field(attribute="patient_id_photo", column_name="PATIENT ID PHOTO")
    insurance_card_photo_front = Field(attribute="insurance_card_photo_front", column_name="INSURANCE CARD PHOTO")
    insurance_card_photo_back = Field(attribute="insurance_card_photo_back", column_name="INSURANCE CARD PHOTO BACK")
    additional_insurance_cards = Field(attribute="additional_insurance_cards", column_name="ADDITIONAL INSURANCE CARDS")
    consent_recording = Field(attribute="consent_recording", column_name="CONSENT RECORDING")
    date_created = Field(attribute="date_created", column_name="DATE CREATED")
    created_by = Field(attribute="created_by", column_name="CREATED BY")
    updated_by = Field(attribute="updated_by", column_name="UPDATED BY")
    user_promo_code = Field(attribute="user_promo_code", column_name="USER PROMO CODE")


    class Meta:
        model = BioConfirmMaster    
        exclude = ('id',)


class AgentResource(resources.ModelResource):
    name = Field(attribute="name", column_name="AGENT")

    class Meta:
        model = Agent
        exclude = ['id', 'agent__name']
