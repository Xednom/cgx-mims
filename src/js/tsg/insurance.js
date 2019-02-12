Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#insurance-app',
  delimiters: ['[[',']]'],
  data: {
    insurances: [],
    message: null,
    loading: false,
    agentNames: [],
    managerNames: [],
    typeOfInsurance: [],
    currentInsurance: {},
    newInsurance: {
      'name': "",
      'promo_code': "",
      'agent': "",
      'manager': "",
      'date_of_birth': "",
      'state': "",
      'type_of_insurance': "",
      'test': "",
      'active_inactive': "",
      'status': "",
      'insurance_status': "",
      'policy_number': "",
      'verification_date': "",
      'deductible_remainding': "",
      'notes': "",
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
    this.getInsurances();
    this.getAgentNames();
    this.getManagerNames();
    this.getTypeOfInsurance();
    this.setDefaultDates();
  },
  methods: {
    setDefaultDates: function() {
      let currentDate = moment(new Date()).format("YYYY-MM-DD");
      this.newInsurance.verification_date = currentDate;
    },
    onFileChange: function (event) {
      this.newInsurance[event.target.name] = event.target.files[0];
    },
    resetFields: function() {
        Object.keys(this.newInsurance).forEach(key => {
        this.newInsurance[key] = ''
      })
    },
    getInsurances: function() {
          let api_url = '/api/v1/insurance/';
          if(this.search_term!==''||this.search_term!==null) {
            api_url = `/api/v1/insurance/?search=${this.search_term}`
          }
          this.loading = false;
          this.$http.get(api_url)
              .then((response) => {
                this.insurances = response.data;
                this.loading = false;
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        },
      addInsurance: function (event) {
        const formData = new FormData();
        Object.keys(this.newInsurance).forEach((key) => {
          let obj = this.newInsurance[key];
          if (obj instanceof File) {
            formData.append(key, obj, obj.name)
          } else {
            formData.append(key, obj);
          }
        });
        this.loading = false;
        this.$http.post('/api/v1/insurance/', formData).then((response) => {
            this.loading = true;
            swal({
              title: "TSG System",
              text: "Data has been saved successfully for Insurance",
              icon: "success",
              buttons: false,
              timer: 2000
            });
            // reset form for all input types
            this.resetFields();
            // return the current date after resetting the form
            this.setDefaultDates();
            // reset form for attachments
            event.target.reset();
          })
          .catch((err) => {
            this.loading = false;
            swal({
              title: "TSG System",
              text: err,
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
      getManagerNames: function() {
      this.loading = true;
      this.$http.get(`/api/v1/manager/`)
          .then((response) => {
            this.managerNames = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
      getTypeOfInsurance: function() {
        this.loading = true;
        this.$http.get(`/api/v1/type-of-insurance/`)
            .then((response) => {
              this.typeOfInsurance = response.data;
              this.loading = false;
            })
            .catch((err) => {
              this.loading = false;
              console.log(err);
            })
      },
      viewInsurance: function (id) {
        this.loading = true;
        this.$http.get(`/api/v1/insurance/${id}/`)
            .then((response) => {
              this.currentInsurance = response.data;
              this.loading = false;
            })
            .catch((err) => {
              this.loading = false;
              console.log(err);
            })
      },
  }
});
