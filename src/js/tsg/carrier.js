Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#carrier-app',
  delimiters: ['[[',']]'],
  data: {
    carriers: [],
    message: null,
    loading: false,
    search_term: ''
  },
  mounted: function() {
    this.getCarriers();
  },
  methods: {
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
