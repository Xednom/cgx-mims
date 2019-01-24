Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#bioconfirm-app',
  delimiters: ['[[',']]'],
  data: {
    bioconfirms: [],
    carriers: [],
    message: null,
    loading: false,
    newBioConfirm: {
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
    this.getBioConfirms();
    this.getCarriers();
  },
  methods: {
    getBioConfirms: function() {
          let api_url = '/api/v1/bio-confirm-master/';
          if(this.search_term!==''||this.search_term!==null) {
            api_url = `/api/v1/bio-confirm-master/?search=${this.search_term}`
          }
          this.loading = false;
          this.$http.get(api_url)
              .then((response) => {
                this.bioconfirms = response.data;
                this.loading = false;
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
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
  }
});
