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
  },
  methods: {
    onFileChange: function (event) {
      this.newInsurance[event.target.name] = event.target.files[0];
    },
    reset: function () {
      this.newInsurance.name = this.newInsurance.promo_code = this.newInsurance.agent = this.newInsurance.manager = null;
      this.newInsurance.date_of_birth = this.newInsurance.state = this.newInsurance.type_of_insurance = this.newInsurance.test = null;
      this.newInsurance.active_inactive = this.newInsurance.status = this.newInsurance.insurance_status = this.newInsurance.policy_number = null;
      this.newInsurance.verification_date = this.newInsurance.deductible_remainding = this.newInsurance.notes = this.newInsurance.patient_id_photo = null;
      this.$refs.insurance_card_photo_front.value = this.$refs.insurance_card_photo_back.value = this.$refs.additional_insurance_cards.value = this.$refs.consent_recording.value = '';
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
      addInsurance: function () {
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
            this.reset();
          })
          .catch((err) => {
            this.loading = false;
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
  }
});
