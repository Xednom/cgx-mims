Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#bioconfirm-app',
  delimiters: ['[[',']]'],
  data: {
    bioconfirms: [],
    agentNames: [],
    message: null,
    loading: false,
    currentBioConfirm: {},
    newBioConfirm: {
      'patient_name': "",
      'patient_phone_number': "",
      'promo_code': "",
      'agent': "",
      'date_app_rec': "",
      'date_sample_rec': "",
      'type_of_test': "",
      'date_of_qca': "",
      'submitted_to_tamika_ins_verifier': "",
      'telemed_name': "",
      'date_submitted_to_telemed': "",
      'date_telemed_returned': "",
      'date_bioconfim_rec_app': "",
      'date_paid': "",
      'state': "",
      'status': "",
      'month': "",
      'insurance_company': "",
      'notes': "",
      'rejection_date': "",
      'patient_id_photo': "",
      'insurance_card_photo_front': "",
      'insurance_card_photo_back': "",
      'additional_insurance_cards': "",
      'consent_recording': "",
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
    this.getBioConfirms();
    this.getAgentNames();
		this.setDefaultDates();
  },
  methods: {
    setDefaultDates: function() {
      let currentDate = moment(new Date()).format("YYYY-MM-DD");
      this.newBioConfirm.submitted_to_tamika_ins_verifier = currentDate;
      this.newBioConfirm.date_app_rec = currentDate;
      this.newBioConfirm.date_sample_rec = currentDate;
      this.newBioConfirm.date_of_qca = currentDate;
      this.newBioConfirm.date_submitted_to_telemed = currentDate;
      this.newBioConfirm.date_telemed_returned = currentDate;
      this.newBioConfirm.date_bioconfim_rec_app = currentDate;
      this.newBioConfirm.date_paid = currentDate;
      this.newBioConfirm.rejection_date = currentDate;
    },
    onFileChange: function (event) {
      this.newBioConfirm[event.target.name] = event.target.files[0];
    },
    resetFields: function() {
        Object.keys(this.newBioConfirm).forEach(key => {
        this.newBioConfirm[key] = ''
      })
    },
    getBioConfirms: function() {
      let api_url = '/api/v1/bio-confirm-master/';
      if(this.search_term!==''||this.search_term!==null) {
        api_url = `/api/v1/bio-confirm-master/?search=${this.search_term}`
      }
      this.loading = true;
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
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },

    // new code using axios
    addBioConfirm: function(event) {
      const formData = new FormData();
      Object.keys(this.newBioConfirm).forEach((key) => {
        let obj = this.newBioConfirm[key];
        if (obj instanceof File) {
          formData.append(key, obj, obj.name)
        } else {
          formData.append(key, obj);
        }
      });
      this.loading = true;
      axios.post(`/api/v1/bio-confirm-master/`, formData).then((response) => {
          swal({
            title: "TSG System",
            text: "Data has been saved successfully for Bio Confirm",
            icon: "success",
            buttons: false,
            timer: 2000
          })
          this.loading = false;
          this.getBioConfirms();
          // reset form
          this.resetFields();
          // return the current date after resetting the form
          this.setDefaultDates();
          // reset form
          event.target.reset();
      })
      .catch((err) => {
        swal({
          title: "TSG System",
          text: "Please check if the Patient name is already in the database. And if yes, and the error still persist please contact your site administrator.",
          icon: "error",
          buttons: "Ok",
        });
        console.log(err);
        this.loading = false;
      })
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
    getPaginatedRecords: function() {
      const startIndex = this.startIndex;
      this.paginatedRecords = this.bioconfirms.slice().splice(startIndex, this.pageSize);
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
    }
  },
  watch: {
    bioconfirms: function(newBioconfirmRecords, oldBioconfirmRecords) {
      this.setPageGroup();
      this.getPaginatedRecords();
    },
    currentPage: function(newCurrentPage, oldCurrentPage) {
      this.setPageGroup();
      this.getPaginatedRecords()
    },
  },
  computed: {
    totalItems: function() {
      return this.bioconfirms.length;
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
