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
    currentCarrier: {},
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
    this.setDefaultDates();
  },
  methods: {
    setDefaultDates: function() {
      let currentDate = moment(new Date()).format("YYYY-MM-DD");
      this.newCarrier.submitted_to_tamika_ins_verifier = currentDate;
      this.newCarrier.date_app_rec = currentDate;
      this.newCarrier.date_sample_rec = currentDate;
      this.newCarrier.date_of_qca = currentDate;
      this.newCarrier.date_submitted_to_telemed = currentDate;
      this.newCarrier.date_telemed_returned = currentDate;
      this.newCarrier.date_bioconfim_rec_app = currentDate;
      this.newCarrier.date_paid = currentDate;
      this.newCarrier.rejection_date = currentDate;
    },
    onFileChange: function (event) {
      this.newCarrier[event.target.name] = event.target.files[0];
    },
    resetFields: function() {
        Object.keys(this.newCarrier).forEach(key => {
        this.newCarrier[key] = ''
      })
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
      addCarrier: function (event) {
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
          swal({
            title: "TSG System",
            text: "Data has been saved successfully for Carrier",
            icon: "success",
            buttons: false,
            timer: 2000
          });
          this.loading = false;
          this.getCarriers();
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
    // viewing of full datas
    viewCarrier: function(id) {
    this.loading = true;
    this.$http.get(`/api/v1/carrier/${id}/`)
        .then((response) => {
          this.loading = false;
          this.currentCarrier = response.data;
        })
        .catch((err) => {
          this.loading = false;
          console.log(err);
        })
  },
  }
});
