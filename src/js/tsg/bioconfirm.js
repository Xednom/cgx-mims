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
    },
    search_term: '',
    fileInput: {},
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
              console.log(formData);
              this.loading = false;
              swal({
                title: "TSG System",
                text: "Data has been saved successfully for Bio Confirm",
                icon: "success",
                buttons: false,
                timer: 2000
              })
              this.getBioConfirms();
              // reset form
              event.target.reset();
          })
          .catch((err) => {
            swal({
              title: "TSG System",
              text: "Something has happened when processing the data, if the error persist. Please contact your Administrator.",
              icons: "Error",
              buttons: "Ok",
            });
            console.log(err);
            this.loading = false;
          })
      },
  }
});