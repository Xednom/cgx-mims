Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#bioconfirm-app',
  delimiters: ['[[',']]'],
  data: {
    bioconfirms: [],
    agentNames: [],
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
    this.getAgentNames();
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
        getAgentNames: function() {
          this.loading = true;
          this.$http.get(`/api/v1/agent/`)
              .then((response) => {
                this.agentNames = response.data;
                this.loading = true;
              })
              .catch((err) => {
                this.loading = false;
                console.log(err);
              })
        },
        addBioConfirm: function() {
        this.loading = true;
        this.$http.post('/api/v1/bio-confirm-master/', this.newBioConfirm)
            .then((response) => {
              this.loading = true;
              swal({
                title: "TSG System",
                text: "Data has been saved successfully for Bio Confirm Master",
                icon: "success",
                buttons: false,
                timer: 2000
              })
              this.getBioConfirms();
            })
            .catch((err) => {
              this.loading = true;
              console.log(err);
            })
      },
  }
});
