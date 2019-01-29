Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#dme-app',
  delimiters: ['[[',']]'],
  data: {
    dmes: [],
    message: null,
    loading: false,
    newDme: {
        'submission_date': null,
        'first_name': null,
        'last_name': null,
        'agents_promod_code': null,
        'agents_email': null,
        'patients_first_name': null,
        'patients_last_name': null,
        'birth_date': null,
        'gender': null,
        'patients_phone_number': null,
        'best_time_to_call': null,
        'street_address': null,
        'street_address_line_2': null,
        'city': null,
        'state_province': null,
        'postal_zip_code': null,
        'country': null,
        'patient_id_photo': null,
        'insurance_type': null,
        'policy_number': null,
        'ppo_information_mem_id': null,
        'ppo_information_ppo_name': null,
        'insurance_status': null,
        'insurance_notes': null,
        'insurance_card_photo_front': null,
        'insurance_card_photo_back': null,
        'additional_insurance_cards': null,
        'location_of_back_pain': null,
        'location_of_shoulder_pain': null,
        'location_of_knee_pain': null,
        'location_of_elbow_pain': null,
        'localtion_of_wrist_pain': null,
        'height': null,
        'weight': null,
        'size_of_brace': null,
        'major_medical_conditions': null,
        'cause_of_pain_discomfort': null,
        'level_of_pain': null,
        'experiencing_discomfort': null,
        'frequency_of_pain': null,
        'describe_pain': null,
        'pain_symptoms': null,
        'pain_worse': null,
        'treatments_tried': null,
        'seen_doctor': null,
        'surgeries': null,
        'consent_recording': null,
        'ip': null,
        'submission_id': null,
        'edit_link': null,
    },
    search_term: ''
  },
  mounted: function() {
    this.getDmes();
  },
  methods: {
    getDmes: function() {
          let api_url = '/api/v1/dme/';
          if(this.search_term!==''||this.search_term!==null) {
            api_url = `/api/v1/dme/?search=${this.search_term}`
          }
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
    addDme: function() {
      this.loading = false;
      this.$http.post('/api/v1/dme/', this.newDme)
          .then((response) => {
            this.loading = false;
            swal({
              title: "TSG System",
              text: "Data has been saved successfully for DME",
              icon: "success",
              buttons: false,
              timer: 2000
            })
            this.getDmes();

          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
  }
});
