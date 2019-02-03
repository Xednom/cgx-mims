Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#carrier-app',
  delimiters: ['[[',']]'],
  data: {
    carriers: [],
    agentNames: [],
    message: null,
    loading: false,
    csrf_token: ['csrf_token'],
    newCarrier: {
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
    fileInput: {},
  },
  mounted: function() {
    this.getCarriers();
    this.getAgentNames();
  },
  methods: {
    onFileChange: function (event) {
      this.newCarrier[event.target.name] = event.target.files[0];
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

      // new code using axios
      addCarrier: function (event) {
        const formData = new FormData();
        Object.keys(this.newCarrier).forEach((key) => {
            let obj = this.newCarrier[key];
            if (obj instanceof File) {
              formData.append(key, obj, obj.name)
            } else {
              formData.append(key, obj);
            }
        });
        this.loading = true;
        this.$http.post('/api/v1/carrier/', formData).then((response) => {
          console.log(formData);
          this.loading = true;
          swal({
            title: "TSG System",
            text: "Data has been saved successfully for Carrier",
            icon: "success",
            buttons: false,
            timer: 2000
          });
          this.getCarriers();
          // reset form
          event.target.reset();
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
  }
});
