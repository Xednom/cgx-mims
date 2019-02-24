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
    search_term: '',
  },
  mounted: function() {
    // no functions to be mounted cause this is search, nothing loaded automatically
  },
  methods: {
    getbioConfirms: function() {
        // Search function
          let api_url = '/api/v1/bio-confirm-master/';
          if(this.search_term==''||this.search_term==null) {
            swal({
              title: "TSG System",
              text: "Please fill up the search box",
              icon: "warning",
              buttons: false,
              timer: 2000
            });
            this.bioConfirms = null;
          }
          else {
            api_url = `/api/v1/bio-confirm-master/?search=${this.search_term}`
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
          }

        },
    getCarriers: function() {
        // Search function
          let api_url = '/api/v1/carrier/';
          if(this.search_term==''||this.search_term==null) {
            swal({
              title: "TSG System",
              text: "Please fill up the search box",
              icon: "warning",
              buttons: false,
              timer: 2000
            });
            this.carriers = null;
          }
          else {
            api_url = `/api/v1/carrier/?search=${this.search_term}`
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
          }
        },
    getDmes: function() {
        // Search function
          let api_url = '/api/v1/dme/';
          if(this.search_term!==''||this.search_term!==null) {
            api_url = `/api/v1/dme/?search=${this.search_term}`
          }
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
          let api_url = '/api/v1/insurance/';
          if(this.search_term!==''||this.search_term!==null) {
            api_url = `/api/v1/insurance/?search=${this.search_term}`
          }
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
