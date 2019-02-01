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
    /*addDme: function() {
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
      this.$http.post('/api/v1/dme/', formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          })
          .then((response) => {
            this.loading = false;
            console.log(formData);
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
    },*/

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
        this.loading = true;
        swal({
          title: "TSG System",
          text: "Data has been saved successfully for DME",
          icons: "success",
          buttons: false,
          timer: 2000
        });
        this.getDmes();
      })
      .catch((err) => {
        this.loading = true;
        console.log(err);
      })
    },
  }
});
