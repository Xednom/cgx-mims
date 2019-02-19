Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#pc-and-fb-app',
  delimiters: ['[[',']]'],
  data: {
    pcfbs: [],
    message: null,
    loading: false,
    currentPcFb: {},
    newPcFb: {
        'submission_date': "",
        'promo_code': "",
        'agent_name': "",
        'agents_email': "",
        'patient_first_name': "",
        'patient_last_name': "",
        'birth_date': "",
        'gender': "",
        'patient_phone_number': "",
        'best_time_to_call': "",
        'street_address': "",
        'street_address_2': "",
        'city': "",
        'state_province': "",
        'postal_zip_code': "",
        'country': "",
        'insurance_type': "",
        'medicare_medicaid_policy': "",
        'ppo_hmo_information_mem_id': "",
        'ppo_hmo_information_ppo_name': "",
        'insurance_status': "",
        'location_of_pain': "",
        'level_of_pain': "",
        'discomfort': "",
        'freq_of_pain': "",
        'prescribe_pain_cream': "",
        'location_of_foot_issue': "",
        'describe_foot_issue': "",
        'order_status': "",
        'date_faxed_to_pharmacy': "",
        'ip': "",
        'patient_id_photo': "",
        'insurance_card_photo': "",
        'ppo_card_photo': "",
        'consent_recording': "",
        'ip': "",
        'submission_id': "",
        'date_created': "",
        'created_by': "",
        'updated_by': "",
        'user_promo_code': "",
    },
    search_term: '',

    // for pagination
    currentPage: 1,
    pageSize: RECORDS_PER_PAGE,
    startPage: 1,
    endPage: null,
    maxPages: RECORDS_PER_PAGE,
    paginatedRecords: [],
  },
  mounted: function() {
    this.getPcFbs();
    this.setDefaultDates();
  },
  methods: {
    setDefaultDates: function() {
      let currentDate = moment(new Date()).format("YYYY-MM-DD");
      this.newPcFb.submission_date = currentDate;
    },
    onFileChange: function (event) {
      this.newPcFb[event.target.name] = event.target.files[0];
    },
    resetFields: function() {
        Object.keys(this.newPcFb).forEach(key => {
        this.newPcFb[key] = ''
      })
    },
    getPcFbs: function() {
      let api_url = '/api/v1/pain-cream-and-foot-bath/';
      /*if(this.search_term!==''||this.search_term!==null) {
         api_url = `/api/v1/pain-cream-and-foot-bath/?search=${this.search_term}`
       }*/
      this.loading = false;
      this.$http.get(api_url)
          .then((response) => {
            this.pcfbs = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    // new code using axios
    addPcFb: function (event) {
      const formData = new FormData();
      Object.keys(this.newPcFb).forEach((key) => {
          let obj = this.newPcFb[key];
          if (obj instanceof File) {
            formData.append(key, obj, obj.name)
          } else {
            formData.append(key, obj);
          }
      });
      this.loading = true;
      axios.post('/api/v1/pain-cream-and-foot-bath/', formData).then((response) => {
        swal({
          title: "TSG System",
          text: "Data has been saved successfully for Pain Cream and Foot Bath",
          icon: "success",
          buttons: false,
          timer: 2000
        });
        this.loading = false;
        this.getpcfbs();
        // reset form
        this.resetFields();
        // return the current date after resetting the form
        this.setDefaultDates();
        // reset form
        event.target.reset();
      })
      .catch((err) => {
        this.loading = false;
        swal({
          title: "TSG System",
          text: "Something has happened when processing the data, if the error persist. Please contact your Administrator.",
          icon: "error",
          buttons: "Ok",
        });
        console.log(err);
      })
    },
    // view data
    viewDme: function (id) {
      this.loading = true;
      this.$http.get(`/api/v1/pain-cream-and-foot-bath/${id}/`)
          .then((response) => {
            this.currentPcFb = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getPaginatedRecords: function() {
      const startIndex = this.startIndex;
      this.paginatedRecords = this.pcfbs.slice().splice(startIndex, this.pageSize);
    },
    goToPage: function(page) {
      if (page < 1) {
        return this.currentPage = 1;
      }
      if (page > this.totalPages) {
        return this.currentPage = this.totalPages;
      }
      this.currentPage = page;
    },
    setPageGroup: function() {
      if (this.totalPages <= this.maxPages) {
        this.startPage = 1;
        this.endPage = Math.min(this.totalPages, this.maxPages);
      } else {
        let maxPagesBeforeCurrentPage = Math.floor(this.maxPages / 2);
        let maxPagesAfterCurrentPage = Math.ceil(this.maxPages / 2) - 1;
        if (this.currentPage <= maxPagesBeforeCurrentPage) {
            // current page near the start
            this.startPage = 1;
            this.endPage = this.maxPages;
        } else if (this.currentPage + maxPagesAfterCurrentPage >= this.totalPages) {
            // current page near the end
            this.startPage = this.totalPages - this.maxPages + 1;
            this.endPage = this.totalPages;
        } else {
            // current page somewhere in the middle
            this.startPage = this.currentPage - maxPagesBeforeCurrentPage;
            this.endPage = this.currentPage + maxPagesAfterCurrentPage;
        }
      }
    },
  },
  watch: {
    pcfbs: function(newPcFbsRecords, oldpcfbsRecords) {
      this.setPageGroup();
      this.getPaginatedRecords();
    },
    currentPage: function(newCurrentPage, oldCurrentPage) {
      this.setPageGroup();
      this.getPaginatedRecords();
    },
  },
  computed: {
    totalItems: function() {
      return this.pcfbs.length;
    },
    totalPages: function() {
      return Math.ceil(this.totalItems / this.pageSize);
    },
    startIndex: function() {
      return (this.currentPage - 1) * this.pageSize;
    },
    endIndex: function() {
      return Math.min(this.startIndex + this.pageSize - 1, this.totalItems - 1);
    },
    pages: function() {
      let pages = [];
      for (let i = this.startPage; i < this.endPage; i++) pages.push(i);
      return pages;
    },
  },
});
