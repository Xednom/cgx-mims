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
      'patient_name': null,
      'patient_phone_number': null,
      'promo_code': null,
      'agent': null,
      'date_app_rec': null,
      'date_sample_rec': null,
      'type_of_test': null,
      'date_of_qca': null,
      'submitted_to_tamika_ins_verifier': null,
      'telemed_name': null,
      'date_submitted_to_telemed': null,
      'date_telemed_returned': null,
      'date_bioconfim_rec_app': null,
      'date_paid': null,
      'state': null,
      'status': null,
      'month': null,
      'insurance_company': null,
      'notes': null,
      'rejection_date': null,
    },
    search_term: ''
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
        // old code using http
      //   addCarrier: function() {
      //   this.loading = true;
      //   this.$http.post('/api/v1/carrier/', this.newCarrier)
      //       .then((response) => {
      //         this.loading = true;
      //         swal({
      //           title: "TSG System",
      //           text: "Data has been saved successfully for Carrier",
      //           icon: "success",
      //           buttons: false,
      //           timer: 2000
      //         })
      //         this.reset();
      //         this.getCarriers();
      //       })
      //       .catch((err) => {
      //         this.loading = true;
      //         console.log(err);
      //       })
      // },

      // new code using axios
      addCarrier: function () {
        this.loading = true;
        axios.post('/api/v1/carrier/', this.newCarrier).then((response) => {
          this.loading = true;
          swal({
            title: "TSG System",
            text: "Data has been saved successfully for Carrier",
            icon: "success",
            buttons: false,
            timer: 2000
          })
          this.reset();
          this.getCarriers();
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
  }
});
