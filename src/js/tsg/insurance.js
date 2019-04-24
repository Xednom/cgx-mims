Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#insurance-app',
  delimiters: ['[[',']]'],
  data: {
    insurances: [],
    message: null,
    loading: false,
    saving: false,
    searching: false,
    loading_view: false,
    agentNames: [],
    managerNames: [],
    typeOfInsurance: [],
    currentInsurance: {},
    newInsurance: {
      'name': "",
      'promo_code': "",
      'agent': "",
      'manager': "",
      'date_of_birth': "",
      'state': "",
      'type_of_insurance': "",
      'test': "",
      'active_inactive': "",
      'status': "",
      'insurance_status': "",
      'policy_number': "",
      'verification_date': "",
      'deductible_remainding': "",
      'notes': "",
      'patient_id_photo': "",
      'insurance_card_photo_front': "",
      'insurance_card_photo_back': "",
      'additional_insurance_cards': "",
      'consent_recording': "",
    },
    search_term: '',

    // queries from Insurance app from date and to date
    insurance_from_date_created: '',
    insurance_to_date_created: '',
    insurance_name: '',
    insurance_promo_code: '',

    // for pagination
    currentPage: 1,
    pageSize: RECORDS_PER_PAGE,
    startPage: 1,
    endPage: null,
    maxPages: RECORDS_PER_PAGE,
    paginatedRecords: [],
  },
  mounted: function() {
    this.getInsurances();
    this.getAgentNames();
    this.getManagerNames();
    this.getTypeOfInsurance();
    this.setDefaultDates();
  },
  methods: {
    setDefaultDates: function() {
      let currentDate = moment(new Date()).format("YYYY-MM-DD");
      this.newInsurance.verification_date = currentDate;
    },
    onFileChange: function (event) {
      this.newInsurance[event.target.name] = event.target.files[0];
    },
    resetFields: function() {
        Object.keys(this.newInsurance).forEach(key => {
        this.newInsurance[key] = ''
      })
    },
    getInsurances: function() {
      let api_url = '/api/v1/insurance/';
      /* if(this.search_term!==''||this.search_term!==null) {
        api_url = `/api/v1/insurance/?search=${this.search_term}`
      } */
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
    viewInsurances: function () {
      // Search function
      api_url = `/api/v1/insurance/?date_created__gte=${this.insurance_from_date_created}&date_created__lte=${this.insurance_to_date_created}&name=${this.insurance_name}&promo_code=${this.insurance_promo_code}`
      this.loading_view = true;
      this.$http.get(api_url)
        .then((response) => {
          this.insurances = response.data;
          this.loading_view = false;
        })
        .catch((err) => {
          this.loading_view = false;
          console.log(err);
        })
    },
    addInsurance: function (event) {
      const formData = new FormData();
      Object.keys(this.newInsurance).forEach((key) => {
        let obj = this.newInsurance[key];
        if (obj instanceof File) {
          formData.append(key, obj, obj.name)
        } else {
          formData.append(key, obj);
        }
      });
      this.loading = true;
      this.$http.post('/api/v1/insurance/', formData).then((response) => {
          this.loading = false;
          swal({
            title: "TSG System",
            text: "Data has been saved successfully for Insurance",
            icon: "success",
            buttons: false,
            timer: 2000
          });
          // reset form for all input types
          this.resetFields();
          // return the current date after resetting the form
          this.setDefaultDates();
          // reset form for attachments
          event.target.reset();
        })
        .catch((err) => {
          this.loading = false;
          swal({
            title: "TSG System",
            text: err,
            icon: "error",
            buttons: "Ok",
          });
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
    getManagerNames: function() {
      this.loading = true;
      this.$http.get(`/api/v1/manager/`)
          .then((response) => {
            this.managerNames = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getTypeOfInsurance: function() {
      this.loading = true;
      this.$http.get(`/api/v1/type-of-insurance/`)
          .then((response) => {
            this.typeOfInsurance = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    viewInsurance: function (id) {
      this.loading_view = true;
      this.$http.get(`/api/v1/insurance/${id}/`)
          .then((response) => {
            this.currentInsurance = response.data;
            this.loading_view  = false;
          })
          .catch((err) => {
            this.loading_view = false;
            console.log(err);
          })
    },
    getPaginatedRecords: function() {
      const startIndex = this.startIndex;
      this.paginatedRecords = this.insurances.slice().splice(startIndex, this.pageSize);
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
    generateExcelFile: function() {
      let uri = 'data:application/vnd.ms-excel;base64,';

      let context = {
        worksheet: 'Worksheet1',
        header: this.htmlConverter(this.generateExcelHeader()),
        table: this.generateRows()
      }
      let htmlXML = this.generateXMLNS();
      let formattedTemplate = this.formatTemplate(htmlXML, context);

      let a = document.createElement('A');
      a.href = uri + this.base64(formattedTemplate);
      a.download = 'Insurance-Report-' + Date.now() + '.xlsx';
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
    },
    htmlConverter: function(data) {
      temporaryContainer = document.createElement('div');
      temporaryContainer.appendChild(data);

      return temporaryContainer.innerHTML
    },
    generateRows: function() {
      let insurances = this.insurances;
      let tableRows = '';

      for (let i=0; i<insurances.length; i++) {
        tableRows += this.htmlConverter(
          this.generateData(insurances[i])
          );
      }

      return tableRows

    },
    generateData: function(insurance) {
      let tr = document.createElement('tr');

      let name = document.createElement('td');
      let promoCode = document.createElement('td');
      let agent = document.createElement('td');
      let manager = document.createElement('td');
      let dateOfBirth = document.createElement('td');
      let state = document.createElement('td');
      let typeOfInsurance = document.createElement('td');
      let test = document.createElement('td');
      let activeInactive = document.createElement('td');
      let status = document.createElement('td');
      let insuranceStatus = document.createElement('td');
      let policyNumber = document.createElement('td');
      let verificationDate = document.createElement('td');
      let deductibleRemaining = document.createElement('td');
      let notes = document.createElement('td');
      let patientIDPhoto = document.createElement('td');
      let insuranceCardPhotoFront = document.createElement('td');
      let insuranceCardPhotoBack = document.createElement('td');
      let additionalInsuranceCards = document.createElement('td');
      let consentRecording = document.createElement('td');
      let dateCreated = document.createElement('td');
      let createdBy = document.createElement('td');
      let updatedBy = document.createElement('td');
      let userPromoCode = document.createElement('td');

      name.textContent = insurance['name'];
      promoCode.textContent = insurance['promo_code'];
      agent.textContent = insurance['agent'];
      manager.textContent = insurance['manager'];
      dateOfBirth.textContent = insurance['date_of_birth'];
      state.textContent = insurance['state'];
      typeOfInsurance.textContent = insurance['type_of_insurance'];
      test.textContent = insurance['test'];
      activeInactive.textContent = insurance['active_inactive'];
      status.textContent = insurance['status'];
      insuranceStatus.textContent = insurance['insurance_status'];
      policyNumber.textContent = insurance['policy_number'];
      verificationDate.textContent = insurance['verification_date'];
      deductibleRemaining.textContent = insurance['deductible_remainding'];
      notes.textContent = insurance['notes'];
      patientIDPhoto.textContent = insurance['patient_id_photo'];
      insuranceCardPhotoFront.textContent = insurance['insurance_card_photo_front'];
      insuranceCardPhotoBack.textContent = insurance['insurance_card_photo_back'];
      additionalInsuranceCards.textContent = insurance['additional_insurance_cards'];
      consentRecording.textContent = insurance['consent_recording'];
      dateCreated.textContent = insurance['date_created'];
      createdBy.textContent = insurance['created_by'];
      updatedBy.textContent = insurance['updated_by'];
      userPromoCode.textContent = insurance['user_promo_code'];

      tr.appendChild(name);
      tr.appendChild(promoCode);
      tr.appendChild(agent);
      tr.appendChild(manager);
      tr.appendChild(dateOfBirth);
      tr.appendChild(state);
      tr.appendChild(typeOfInsurance);
      tr.appendChild(test);
      tr.appendChild(activeInactive);
      tr.appendChild(status);
      tr.appendChild(insuranceStatus);
      tr.appendChild(policyNumber);
      tr.appendChild(verificationDate);
      tr.appendChild(deductibleRemaining);
      tr.appendChild(notes);
      tr.appendChild(patientIDPhoto);
      tr.appendChild(insuranceCardPhotoFront);
      tr.appendChild(insuranceCardPhotoBack);
      tr.appendChild(additionalInsuranceCards);
      tr.appendChild(consentRecording);
      tr.appendChild(dateCreated);
      tr.appendChild(createdBy);
      tr.appendChild(updatedBy);
      tr.appendChild(userPromoCode);

      return tr
    },
    generateExcelHeader: function() {
      let tr = document.createElement('tr');

      let name = document.createElement('th');
      let promoCode = document.createElement('th');
      let agent = document.createElement('th');
      let manager = document.createElement('th');
      let dateOfBirth = document.createElement('th');
      let state = document.createElement('th');
      let typeOfInsurance = document.createElement('th');
      let test = document.createElement('th');
      let activeInactive = document.createElement('th');
      let status = document.createElement('th');
      let insuranceStatus = document.createElement('th');
      let policyNumber = document.createElement('th');
      let verificationDate = document.createElement('th');
      let deductibleRemaining = document.createElement('th');
      let notes = document.createElement('th');
      let patientIDPhoto = document.createElement('th');
      let insuranceCardPhotoFront = document.createElement('th');
      let insuranceCardPhotoBack = document.createElement('th');
      let additionalInsuranceCards = document.createElement('th');
      let consentRecording = document.createElement('th');
      let dateCreated = document.createElement('th');
      let createdBy = document.createElement('th');
      let updatedBy = document.createElement('th');
      let userPromoCode = document.createElement('th');

      name.textContent = 'Patient Name';
      promoCode.textContent = 'Promo Code';
      agent.textContent = 'Agent';
      manager.textContent = 'Manager';
      dateOfBirth.textContent = 'Date of Birth';
      state.textContent = 'State';
      typeOfInsurance.textContent = 'Type of Insurance';
      test.textContent = 'Test';
      activeInactive.textContent = 'Active/Inactive';
      status.textContent = 'Status';
      insuranceStatus.textContent = 'Insurance Status';
      policyNumber.textContent = 'Policy Number';
      verificationDate.textContent = 'Verification Date';
      deductibleRemaining.textContent = 'Deductible Remaining';
      notes.textContent = 'Notes';
      patientIDPhoto.textContent = 'Patient ID Photo';
      insuranceCardPhotoFront.textContent = 'Insurance Card Photo Front';
      insuranceCardPhotoBack.textContent = 'Insurance Card Photo Back';
      additionalInsuranceCards.textContent = 'Additional Insurance Cards';
      consentRecording.textContent = 'Consent Recording';
      dateCreated.textContent = 'Date Created';
      createdBy.textContent = 'Created by';
      updatedBy.textContent = 'Updated by';
      userPromoCode.textContent = 'User Promo Code';

      tr.appendChild(name);
      tr.appendChild(promoCode);
      tr.appendChild(agent);
      tr.appendChild(manager);
      tr.appendChild(dateOfBirth);
      tr.appendChild(state);
      tr.appendChild(typeOfInsurance);
      tr.appendChild(test);
      tr.appendChild(activeInactive);
      tr.appendChild(status);
      tr.appendChild(insuranceStatus);
      tr.appendChild(policyNumber);
      tr.appendChild(verificationDate);
      tr.appendChild(deductibleRemaining);
      tr.appendChild(notes);
      tr.appendChild(patientIDPhoto);
      tr.appendChild(insuranceCardPhotoFront);
      tr.appendChild(insuranceCardPhotoBack);
      tr.appendChild(additionalInsuranceCards);
      tr.appendChild(consentRecording);
      tr.appendChild(dateCreated);
      tr.appendChild(createdBy);
      tr.appendChild(updatedBy);
      tr.appendChild(userPromoCode);

      return tr
    },
    generateXMLNS: function() {
      let htmlOpenTag = '<html xmlns:o="urn:schemas-microsoft.com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">';
      let htmlHead = '<head><!-- [if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet><x:Name>{worksheet}</x:Name><x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet></x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]--><meta http-equiv="content-type" content="text/plain; charset=UTF-8"></head>';
      let htmlBody = '<body><table>{header}{table}</table></body>';
      let htmlCloseTag = '</html>';

      return htmlOpenTag + htmlHead + htmlBody + htmlCloseTag;
    },
    base64: function(template) {
      return window.btoa(unescape(encodeURIComponent(template)))
    },
    formatTemplate: function(template, context) {
      return template.replace(/{(\w+)}/g, function(m, p) { return context[p] })
    }
  },
  watch: {
    insurances: function(newInsurancesRecords, oldInsurancesRecords) {
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
      return this.insurances.length;
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
