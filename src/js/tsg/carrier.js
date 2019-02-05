Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#carrier-app',
  delimiters: ['[[',']]'],
  data: {
    carriers: [],
    agentNames: [],
    message: null,
    loading: false,
    csrf_token: ['csrf_token'],
    newCarrier: {
      'patient_name': "",
      'patient_phone_number': "",
      'promo_code': "",
      'agent': "",
      'date_app_rec': "",
      'date_sample_rec': "",
      'type_of_test': "",
      'date_of_qca': "",
      'submitted_to_tamika_ins_verifier': "",
      'telemed_name': "",
      'date_submitted_to_telemed': "",
      'date_telemed_returned': "",
      'date_bioconfim_rec_app': "",
      'date_paid': "",
      'state': "",
      'status': "",
      'month': "",
      'insurance_company': "",
      'notes': "",
      'rejection_date': "",
      'patient_id_photo': "",
      'insurance_card_photo_front': "",
      'insurance_card_photo_back': "",
      'additional_insurance_cards': "",
      'consent_recording': "",
    },
    search_term: '',
    fileInput: {},
  },
  mounted: function() {
    this.getCarriers();
    this.getAgentNames();
  },
  methods: {
    reset: function() {
      this.newCarrier.patient_name = this.newCarrier.patient_phone_number = this.newCarrier.promo_code = null;
      this.newCarrier.agent = this.newCarrier.date_app_rec = this.newCarrier.date_sample_rec = null;
      this.newCarrier.type_of_test = this.newCarrier.date_of_qca = this.newCarrier.submitted_to_tamika_ins_verifier = null;
      this.newCarrier.telemed_name = this.newCarrier.date_submitted_to_telemed = this.newCarrier.date_telemed_returned = null;
      this.newCarrier.date_bioconfim_rec_app = this.newCarrier.date_paid = this.newCarrier.state = null;
      this.newCarrier.status = this.newCarrier.month = this.newCarrier.insurance_company = null;
      this.newCarrier.notes = this.newCarrier.rejection_date = null;
    },
    onFileChange: function (event) {
      this.newCarrier[event.target.name] = event.target.files[0];
    },
    getCarriers: function() {
          let api_url = '/api/v1/carrier/';
          if(this.search_term!==''||this.search_term!==null) {
            api_url = `/api/v1/carrier/?search=${this.search_term}`
          }
          this.loading = false;
          this.$http.get(api_url)
              .then((response) => {
                this.carriers = response.data;
                this.loading = false;
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        },

      // new code using axios
      addCarrier: function () {
        const formData = new FormData();
        Object.keys(this.newCarrier).forEach((key) => {
            let obj = this.newCarrier[key];
            if (obj instanceof File) {
              formData.append(key, obj, obj.name)
            } else {
              formData.append(key, obj);
            }
        });
        this.loading = true;
        this.$http.post('/api/v1/carrier/', formData).then((response) => {
          console.log(formData);
          this.loading = false;
          swal({
            title: "TSG System",
            text: "Data has been saved successfully for Carrier",
            icon: "success",
            buttons: false,
            timer: 2000
          });
          this.reset();
          this.getCarriers();
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
      getAgentNames: function() {
      this.loading = true;
      this.$http.get(`/api/v1/agent/`)
          .then((response) => {
            this.agentNames = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
  }
});
