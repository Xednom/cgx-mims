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
    search_term: ''
  },
  mounted: function() {
    this.getDmes();
  },
  methods: {
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
        // old code using http
    addDme: function() {
      // const formDme = document.getElementById('formDme');
      // const formData = new FormData(formDme);
      // key/value pair
      // formData.append('submission_date', this.newDme.submission_date)
      // formData.append('first_name', this.newDme.first_name)
      // formData.append('last_name', this.newDme.last_name)
      // formData.append('agetns_promod_code', this.newDme.agents_promod_code)
      // formData.append('agents_email', this.newDme.agents_email)
      // formData.append('patient_id_photo', this.newDme.patient_id_photo)
      // formData.append('insurance_card_photo_front', this.newDme.insurance_card_photo_front)
      // formData.append('insurance_card_photo_back', this.newDme.insurance_card_photo_back)
      // formData.append('additional_insurance_cards', this.newDme.additional_insurance_cards)
      // formData.append('submission_date', this.newDme.submission_date)
      this.loading = false;
      this.$http.post('/api/v1/dme/', this.newDme)
          //   headers: {
          //     'Content-Type': 'multipart/form-data'
          //   }
          // })
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

    // new code using axios
    // addDme: function () {
    //   this.loading = false;
    //   axios.post('/api/v1/dme/', this.newDme).then((response) => {
    //     this.loading = true;
    //     swal({
    //       title: "TSG System",
    //       text: "Data has been saved successfully for DME",
    //       icons: "success",
    //       buttons: false,
    //       timer: 2000
    //     })
    //     this.getDmes();
    //   })
    //   .catch((err) => {
    //     this.loading = true;
    //     console.log(err);
    //   })
    // },
  }
});
