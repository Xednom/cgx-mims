Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#search-app',
  delimiters: ['[[',']]'],
  data: {
    bioConfirms: [],
    carriers: [],
    dmes: [],
    insurances: [],
    agentNames: [],
    message: null,
    loading: false,
    currentBioConfirm: {},
    currentCarrier: {},
    currentDme: {},
    currentInsurance: {},

    // queries for Carrier app from date and to date
    // From dates
    carrier_from_date_app_rec: '',
    carrier_from_date_sample_rec: '',
    carrier_from_date_of_qca: '',
    carrier_from_date_created: '',
    // To dates
    carrier_to_date_app_rec: '',
    carrier_to_date_sample_rec: '',
    carrier_to_date_of_qca: '',
    carrier_to_date_created: '',
    carrier_search_patient_name: '',

    // queries for Bio Confirm Master app from date and to date
    // From dates
    bioconfirm_from_date_app_rec: '',
    bioconfirm_from_date_sample_rec: '',
    bioconfirm_from_date_of_qca: '',
    bioconfirm_from_date_created: '',
    // To dates
    bioconfirm_to_date_app_rec: '',
    bioconfirm_to_date_sample_rec: '',
    bioconfirm_to_date_of_qca: '',
    bioconfirm_to_date_created: '',
    bioconfirm_search_patient_name: '',

    // queries for DME app from date and to date
    dme_form_submission_date: '',
    dme_to_submission_date: '',
    dme_patients_first_name: '',
    dme_patients_last_name: '',

    // queries from Insurance app from date and to date
    insurance_from_date_created: '',
    insurance_to_date_created: '',
    insurance_name: '',
    insurance_promo_code: '',
  },
  mounted: function() {
    // no functions to be mounted cause this is search, nothing loaded automatically
  },
  methods: {
    getBioConfirms: function() {
      // Search function
      api_url = `/api/v1/bio-confirm-master/?date_app_rec__gte=${this.bioconfirm_from_date_app_rec}&date_app_rec__lte=${this.bioconfirm_to_date_app_rec}&date_sample_rec__gte=${this.bioconfirm_from_date_sample_rec}&date_sample_rec__lte=${this.bioconfirm_to_date_sample_rec}&date_of_qca__gte=${this.bioconfirm_from_date_of_qca}&date_of_qca__lte=${this.bioconfirm_to_date_of_qca}&date_created__gte=${this.bioconfirm_from_date_created}&date_created__lte=${this.bioconfirm_to_date_created}&patient_name=${this.bioconfirm_search_patient_name}`
        this.bioConfirms = null;
        this.loading = true;
        this.$http.get(api_url)
            .then((response) => {
              this.bioConfirms = response.data;
              this.loading = false;
            })
            .catch((err) => {
              this.loading = false;
              console.log(err);
            })
    },
    getCarriers: function() {
        // Search function
      api_url = `/api/v1/carrier/?date_app_rec__gte=${this.carrier_from_date_app_rec}&date_app_rec__lte=${this.carrier_to_date_app_rec}&date_sample_rec__gte=${this.carrier_from_date_sample_rec}&date_sample_rec__lte=${this.carrier_to_date_sample_rec}&date_of_qca__gte=${this.carrier_from_date_of_qca}&date_of_qca__lte=${this.carrier_to_date_of_qca}&date_created__gte=${this.carrier_from_date_created}&date_created__lte=${this.carrier_to_date_created}&patient_name=${this.carrier_search_patient_name}`
        this.loading = true;
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
    extractCarrier: function () {
      api_url = `/api/v1/carrier/?format=xlsx`
      this.loading = true;
      this.$http.get(api_url)
          .then((response) => {
            this.loading = false;
            this.carriers = response.data;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getDmes: function() {
        // Search function
      api_url = `/api/v1/dme/?submission_date__gte=${this.dme_form_submission_date}&submission_date__lte=${this.dme_to_submission_date}&patients_first_name${this.dme_patients_first_name}&patients_last_name=${this.dme_patients_last_name}`
          this.loading = true;
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
    getInsurances: function() {
        // Search function
        api_url = `/api/v1/insurance/?date_created__gte=${this.insurance_from_date_created}&date_created__lte=${this.insurance_to_date_created}&name=${this.insurance_name}&promo_code=${this.insurance_promo_code}`
          this.loading = true;
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
      getAllSearch: function () {
        this.getbioConfirms();
        this.getCarriers();
        this.getDmes();
        this.getInsurances();
      },
      // viewing of full datas
      viewBioConfirm: function(id) {
      this.loading = true;
      this.$http.get(`/api/v1/bio-confirm-master/${id}/`)
          .then((response) => {
            this.loading = false;
            this.currentBioConfirm = response.data;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
  }
});
