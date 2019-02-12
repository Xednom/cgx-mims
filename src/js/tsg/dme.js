Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#dme-app',
  delimiters: ['[[',']]'],
  data: {
    dmes: [],
    message: null,
    loading: false,
    currentDme: {},
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
    this.setDefaultDates();
  },
  methods: {
    setDefaultDates: function() {
      let currentDate = moment(new Date()).format("YYYY-MM-DD");
      this.newDme.submission_date = currentDate;
    },
    onFileChange: function (event) {
      this.newDme[event.target.name] = event.target.files[0];
    },
    resetFields: function() {
        Object.keys(this.newDme).forEach(key => {
        this.newDme[key] = ''
      })
    },
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

    // new code using axios
   addDme: function (event) {
      const formData = new FormData();
      Object.keys(this.newDme).forEach((key) => {
          let obj = this.newDme[key];
          if (obj instanceof File) {
            formData.append(key, obj, obj.name)
          } else {
            formData.append(key, obj);
          }
      });
      this.loading = true;
      axios.post('/api/v1/dme/', formData).then((response) => {
        console.log(formData);
        swal({
          title: "TSG System",
          text: "Data has been saved successfully for DME",
          icon: "success",
          buttons: false,
          timer: 2000
        });
        this.loading = false;
        this.getDmes();
        // reset form
        this.resetFields();
        // return the current date after resetting the form
        this.setDefaultDates();
        // reset form
        event.target.reset();
      })
      .catch((err) => {
        this.loading = false;
        swal({
          title: "TSG System",
          text: "Please check if the Patient name is already in the database. And if yes, and the error still persist please contact your site administrator.",
          icon: "error",
          buttons: "Ok",
        });
        console.log(err);
      })
    },
    // view data
    viewDme: function (id) {
      this.loading = true;
      this.$http.get(`/api/v1/dme/${id}/`)
          .then((response) => {
            this.currentDme = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
  }
});
