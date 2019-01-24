Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#dme-app',
  delimiters: ['[[',']]'],
  data: {
    dmes: [],
    message: null,
    loading: false,
    search_term: ''
  },
  mounted: function() {
    this.getDmes();
  },
  methods: {
    getDmes: function() {
          let api_url = '/api/v1/dme/';
          if(this.search_term!==''||this.search_term!==null) {
            api_url = `/api/v1/dme/?search=${this.search_term}`
          }
          this.loading = false;
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
  }
});
