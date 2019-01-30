Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#insurance-app',
  delimiters: ['[[',']]'],
  data: {
    insurances: [],
    message: null,
    loading: false,
    search_term: ''
  },
  mounted: function() {
    this.getInsurances();
  },
  methods: {
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
  }
});
