Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#dme-app',
  delimiters: ['[[',']]'],
  data: {
    dmes: [],
    message: null,
    loading: false,
    newDme: {
        'submission_date': "",
        'first_name': "",
        'last_name': "",
        'agents_promod_code': "",
        'agents_email': "",
        'patients_first_name': "",
        'patients_last_name': "",
        'birth_date': "",
        'gender': "",
        'patients_phone_number': "",
        'best_time_to_call': "",
        'street_address': "",
        'street_address_line_2': "",
        'city': "",
        'state_province': "",
        'postal_zip_code': "",
        'country': "",
        'patient_id_photo': "",
        'insurance_type': "",
        'policy_number': "",
        'ppo_information_mem_id': "",
        'ppo_information_ppo_name': "",
        'insurance_status': "",
        'insurance_notes': "",
        'insurance_card_photo_front': "",
        'insurance_card_photo_back': "",
        'additional_insurance_cards': "",
        'location_of_back_pain': "",
        'location_of_shoulder_pain': "",
        'location_of_knee_pain': "",
        'location_of_elbow_pain': "",
        'localtion_of_wrist_pain': "",
        'height': "",
        'weight': "",
        'size_of_brace': "",
        'major_medical_conditions': "",
        'cause_of_pain_discomfort': "",
        'level_of_pain': "",
        'experiencing_discomfort': "",
        'frequency_of_pain': "",
        'describe_pain': "",
        'pain_symptoms': "",
        'pain_worse': "",
        'treatments_tried': "",
        'seen_doctor': "",
        'surgeries': "",
        'consent_recording': "",
        'ip': "",
        'submission_id': "",
        'edit_link': "",
    },
    search_term: '',
    fileInput: {},
  },
  mounted: function() {
    this.getDmes();
  },
  methods: {
    onFileChange: function (event) {
      this.newDme[event.target.name] = event.target.files[0];
    },
    reset: function () {
      this.newDme.submission_date = this.newDme.first_name = this.newDme.last_name = this.newDme.agents_promod_code = null;
      this.newDme.agents_email = this.newDme.patients_first_name = this.newDme.patients_last_name = this.newDme.birth_date = null;
      this.newDme.gender = this.newDme.patients_phone_number = this.newDme.best_time_to_call = this.newDme.street_address = null;
      this.newDme.street_address_line_2 = this.newDme.city = this.newDme.state_province = this.newDme.postal_zip_code = null;
      this.newDme.country = this.newDme.patient_id_photo = this.newDme.insurance_type = this.newDme.policy_number = null;
      this.newDme.ppo_information_mem_id = this.newDme.ppo_information_ppo_name = this.newDme.insurance_status = this.newDme.insurance_notes = null;
      this.newDme.insurance_card_photo_front = this.newDme.insurance_card_photo_back = this.newDme.additional_insurance_cards = this.newDme.location_of_back_pain = null;
      this.newDme.location_of_shoulder_pain = this.newDme.location_of_knee_pain = this.newDme.location_of_elbow_pain = this.newDme.localtion_of_wrist_pain = null;
      this.newDme.height = this.newDme.weight = this.newDme.size_of_brace = this.newDme.major_medical_conditions = null;
      this.newDme.cause_of_pain_discomfort = this.newDme.level_of_pain = this.newDme.experiencing_discomfort = this.newDme.frequency_of_pain = null;
      this.newDme.describe_pain = this.newDme.pain_symptoms = this.newDme.pain_worse = this.newDme.treatments_tried = null;
      this.newDme.seen_doctor = this.newDme.surgeries = this.newDme.consent_recording = this.newDme.ip = null;
      this.newDme.submission_id = this.newDme.edit_link = null;

    },
    getDmes: function() {
          let api_url = '/api/v1/dme/';
          // if(this.search_term!==''||this.search_term!==null) {
          //   api_url = `/api/v1/dme/?search=${this.search_term}`
          // }
          this.loading = false;
          this.$http.get(api_url)
              .then((response) => {
                this.dmes = response.data;
                this.loading = false;
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        },

    // new code using axios
   addDme: function () {
      const formData = new FormData();
      Object.keys(this.newDme).forEach((key) => {
          let obj = this.newDme[key];
          if (obj instanceof File) {
            formData.append(key, obj, obj.name)
          } else {
            formData.append(key, obj);
          }
      });
      this.loading = false;
      axios.post('/api/v1/dme/', formData).then((response) => {
        console.log(formData);
        this.loading = false;
        swal({
          title: "TSG System",
          text: "Data has been saved successfully for DME",
          icons: "success",
          buttons: false,
          timer: 2000
        });
        this.reset();
        this.getDmes();
      })
      .catch((err) => {
        this.loading = false;
        swal({
          title: "TSG System",
          text: "Something has happened when processing the data, if the error persist. Please contact your Administrator.",
          icons: "Error",
          buttons: "Ok",
        });
        console.log(err);
      })
    },
  }
});
