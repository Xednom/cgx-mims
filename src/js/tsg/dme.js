Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#dme-app',
  delimiters: ['[[',']]'],
  data: {
    dmes: [],
    message: null,
    loading: false,
    searching: false,
    loading_view: false,
    currentDme: {},
    newDme: {
        'submission_date': "",
        'first_name': "",
        'last_name': "",
        'agents_promod_code': "",
        'agents_email': "",
        'patients_first_name': "",
        'patients_last_name': "",
        'birth_date': "",
        'gender': "",
        'patients_phone_number': "",
        'best_time_to_call': "",
        'street_address': "",
        'street_address_line_2': "",
        'city': "",
        'state_province': "",
        'postal_zip_code': "",
        'country': "",
        'patient_id_photo': "",
        'insurance_type': "",
        'policy_number': "",
        'ppo_information_mem_id': "",
        'ppo_information_ppo_name': "",
        'insurance_status': "",
        'insurance_notes': "",
        'insurance_card_photo_front': "",
        'insurance_card_photo_back': "",
        'additional_insurance_cards': "",
        'location_of_back_pain': "",
        'location_of_shoulder_pain': "",
        'location_of_knee_pain': "",
        'location_of_ankle_pain': "",
        'location_of_elbow_pain': "",
        'location_of_wrist_pain': "",
        'height': "",
        'weight': "",
        'size_of_brace': "",
        'major_medical_conditions': "",
        'cause_of_pain_discomfort': "",
        'level_of_pain': "",
        'experiencing_discomfort': "",
        'frequency_of_pain': "",
        'describe_pain': "",
        'pain_symptoms': "",
        'pain_worse': "",
        'treatments_tried': "",
        'seen_doctor': "",
        'surgeries': "",
        'consent_recording': "",
        'ip': "",
        'submission_id': "",
        'edit_link': "",
    },
    search_term: '',

    // queries for DME app from date and to date
    dme_form_submission_date: '',
    dme_to_submission_date: '',
    dme_patients_first_name: '',
    dme_patients_last_name: '',

    // for pagination
    currentPage: 1,
    pageSize: RECORDS_PER_PAGE,
    startPage: 1,
    endPage: null,
    maxPages: RECORDS_PER_PAGE,
    paginatedRecords: [],
  },
  mounted: function() {
    this.getDmes();
    this.setDefaultDates();
  },
  methods: {
    setDefaultDates: function() {
      let currentDate = moment(new Date()).format("YYYY-MM-DD");
      this.newDme.submission_date = currentDate;
    },
    onFileChange: function (event) {
      this.newDme[event.target.name] = event.target.files[0];
    },
    resetFields: function() {
        Object.keys(this.newDme).forEach(key => {
        this.newDme[key] = ''
      })
    },
    getDmes: function() {
      let api_url = '/api/v1/dme/';
      /*if(this.search_term!==''||this.search_term!==null) {
         api_url = `/api/v1/dme/?search=${this.search_term}`
       }*/
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
    searchDmes: function () {
      // Search function
      api_url = `/api/v1/dme/?submission_date__gte=${this.dme_form_submission_date}&submission_date__lte=${this.dme_to_submission_date}&patients_first_name${this.dme_patients_first_name}&patients_last_name=${this.dme_patients_last_name}`
      this.searching = true;
      this.$http.get(api_url)
        .then((response) => {
          this.dmes = response.data;
          this.searching = false;
        })
        .catch((err) => {
          this.searching = false;
          console.log(err);
        })
    },
    // new code using axios
    addDme: function (event) {
      const formData = new FormData();
      Object.keys(this.newDme).forEach((key) => {
          let obj = this.newDme[key];
          if (obj instanceof File) {
            formData.append(key, obj, obj.name)
          } else {
            formData.append(key, obj);
          }
      });
      this.loading = true;
      axios.post('/api/v1/dme/', formData).then((response) => {
        swal({
          title: "TSG System",
          text: "Data has been saved successfully for DME",
          icon: "success",
          buttons: false,
          timer: 2000
        });
        this.loading = false;
        this.getDmes();
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
      this.loading_view = true;
      this.$http.get(`/api/v1/dme/${id}/`)
          .then((response) => {
            this.currentDme = response.data;
            this.loading_view = false;
          })
          .catch((err) => {
            this.loading_view = false;
            console.log(err);
          })
    },
    getPaginatedRecords: function() {
      const startIndex = this.startIndex;
      this.paginatedRecords = this.dmes.slice().splice(startIndex, this.pageSize);
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
    dmes: function(newDmesRecords, oldDmesRecords) {
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
      return this.dmes.length;
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
      for (let i = this.startPage; i <= this.endPage; i++) pages.push(i);
      return pages;
    },
  },
});
