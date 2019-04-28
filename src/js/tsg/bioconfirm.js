Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#bioconfirm-app',
  delimiters: ['[[',']]'],
  data: {
    bioconfirms: [],
    agentNames: [],
    managerNames: [],
    testChoices: [],
    statuses: [],
    message: null,
    loading: false,
    saving: false,
    searching: false,
    loading_view: false,
    currentBioConfirm: {},
    newBioConfirm: {
      'patient_name': "",
      'patient_phone_number': "",
      'promo_code': "",
      'agent': "",
      'manager': "",
      'date_app_rec': "",
      'date_sample_rec': "",
      'type_of_test': "",
      'date_of_qca': "",
      'insurance_verified_tsg_verification': "",
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
      'date_created': "",
      'created_by': "",
      'user_promo_code': "",
    },
    search_term: '',

    // queries for Bio Confirm Master app from date and to date
    // From dates
    bioconfirm_from_date_app_rec: '',
    bioconfirm_from_date_sample_rec: '',
    bioconfirm_from_date_of_qca: '',
    bioconfirm_from_date_created: '',
    // To dates
    bioconfirm_to_date_app_rec: '',
    bioconfirm_to_date_sample_rec: '',
    bioconfirm_to_date_of_qca: '',
    bioconfirm_to_date_created: '',
    bioconfirm_search_patient_name: '',

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
    this.getManagerNames();
    this.getTestChoices();
    this.getStatuses();
		this.setDefaultDates();
  },
  methods: {
    setDefaultDates: function() {
      let currentDate = moment(new Date()).format("YYYY-MM-DD");
      this.newBioConfirm.date_app_rec = currentDate;
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
      /*if(this.search_term!==''||this.search_term!==null) {
        api_url = `/api/v1/bio-confirm-master/?search=${this.search_term}`
      }*/
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
    searchBioConfirms: function () {
      // Search function
      api_url = `/api/v1/bio-confirm-master/?date_app_rec__gte=${this.bioconfirm_from_date_app_rec}&date_app_rec__lte=${this.bioconfirm_to_date_app_rec}&date_sample_rec__gte=${this.bioconfirm_from_date_sample_rec}&date_sample_rec__lte=${this.bioconfirm_to_date_sample_rec}&date_of_qca__gte=${this.bioconfirm_from_date_of_qca}&date_of_qca__lte=${this.bioconfirm_to_date_of_qca}&date_created__gte=${this.bioconfirm_from_date_created}&date_created__lte=${this.bioconfirm_to_date_created}&patient_name=${this.bioconfirm_search_patient_name}`
      
      this.searching = true;
      this.$http.get(api_url)
        .then((response) => {
          this.bioconfirms = response.data;
          this.searching = false;
        })
        .catch((err) => {
          this.searching = false;
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
    getManagerNames: function () {
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
    getTestChoices: function () {
        this.loading = true;
        this.$http.get(`/api/v1/test-choices/`)
          .then((response) => {
            this.testChoices = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
      },
      getStatuses: function () {
        this.loading = true;
        this.$http.get(`/api/v1/status/`)
          .then((response) => {
            this.statuses = response.data;
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
      this.saving = true;
      this.$http.post(`/api/v1/bio-confirm-master/`, formData).then((response) => {
          swal({
            title: "TSG System",
            text: "Data has been saved successfully for Bio Confirm",
            icon: "success",
            buttons: false,
            timer: 2000
          })
        this.saving = false;
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
        this.saving = false;
      })
    },
    // viewing of full datas
    viewBioConfirm: function(id) {
      this.loading_view = true;
      this.$http.get(`/api/v1/bio-confirm-master/${id}/`)
          .then((response) => {
            this.loading_view = false;
            this.currentBioConfirm = response.data;
          })
          .catch((err) => {
            this.loading_view = false;
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
      a.download = 'Bio-Confirm-Report-' + Date.now() + '.xlsx';
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
      let bioconfirms = this.bioconfirms;
      let tableRows = '';

      for (let i=0; i<bioconfirms.length; i++) {
        tableRows += this.htmlConverter(
          this.generateData(bioconfirms[i])
          );
      }

      return tableRows

    },
    generateData: function(bioconfirm) {
      let tr = document.createElement('tr');

      let patientName = document.createElement('td');
      let patientPhoneNumber = document.createElement('td');
      let promoCode = document.createElement('td');
      let agent = document.createElement('td');
      let manager = document.createElement('td');
      let dateAppRec = document.createElement('td');
      let dateSampleRec = document.createElement('td');
      let typeOfTest = document.createElement('td');
      let dateOfQCA = document.createElement('td');
      let insuranceVerifiedTSGVerification = document.createElement('td');
      let telemedName = document.createElement('td');
      let dateSubmittedToTelemed = document.createElement('td');
      let dateTelemedReturned = document.createElement('td');
      let dateBioconfirmRecApp = document.createElement('td');
      let datePaid = document.createElement('td');
      let dateLabRecordedApp = document.createElement('td');
      let labType = document.createElement('td');
      let state = document.createElement('td');
      let status = document.createElement('td');
      let month = document.createElement('td');
      let insuranceCompany = document.createElement('td');
      let notes = document.createElement('td');
      let rejectionDate = document.createElement('td');
      let patientIDPhoto = document.createElement('td');
      let insuranceCardPhotoFront = document.createElement('td');
      let insuranceCardPhotoBack = document.createElement('td');
      let additionalInsuranceCards = document.createElement('td');
      let consentRecording = document.createElement('td');
      let dateCreated = document.createElement('td');
      let createdBy = document.createElement('td');
      let updatedBy = document.createElement('td');
      let userPromoCode = document.createElement('td');

      patientName.textContent = bioconfirm['patient_name'];
      patientPhoneNumber.textContent = bioconfirm['patient_phone_number'];
      promoCode.textContent = bioconfirm['promo_code'];
      agent.textContent = bioconfirm['agent'];
      manager.textContent = bioconfirm['manager'];
      dateAppRec.textContent = bioconfirm['date_app_rec'];
      dateSampleRec.textContent = bioconfirm['date_sample_rec'];
      typeOfTest.textContent = bioconfirm['type_of_test'];
      dateOfQCA.textContent = bioconfirm['date_of_qca'];
      insuranceVerifiedTSGVerification.textContent = bioconfirm['insurance_verified_tsg_verification'];
      telemedName.textContent = bioconfirm['telemed_name'];
      dateSubmittedToTelemed.textContent = bioconfirm['date_submitted_to_telemed'];
      dateTelemedReturned.textContent = bioconfirm['date_telemed_returned'];
      dateBioconfirmRecApp.textContent = bioconfirm['date_bioconfim_rec_app'];
      datePaid.textContent = bioconfirm['date_paid'];
      dateLabRecordedApp.textContent = bioconfirm['date_lab_recorded_app'];
      labType.textContent = bioconfirm['lab_type'];
      state.textContent = bioconfirm['state'];
      status.textContent = bioconfirm['status'];
      month.textContent = bioconfirm['month'];
      insuranceCompany.textContent = bioconfirm['insurance_company'];
      notes.textContent = bioconfirm['notes'];
      rejectionDate.textContent = bioconfirm['rejection_date'];
      patientIDPhoto.textContent = bioconfirm['patient_id_photo'];
      insuranceCardPhotoFront.textContent = bioconfirm['insurance_card_photo_front'];
      insuranceCardPhotoBack.textContent = bioconfirm['insurance_card_photo_back'];
      additionalInsuranceCards.textContent = bioconfirm['additional_insurance_cards'];
      consentRecording.textContent = bioconfirm['consent_recording'];
      dateCreated.textContent = bioconfirm['date_created'];
      createdBy.textContent = bioconfirm['created_by'];
      updatedBy.textContent = bioconfirm['updated_by'];
      userPromoCode.textContent = bioconfirm['user_promo_code'];

      tr.appendChild(patientName);
      tr.appendChild(patientPhoneNumber);
      tr.appendChild(promoCode);
      tr.appendChild(agent);
      tr.appendChild(manager);
      tr.appendChild(dateAppRec);
      tr.appendChild(dateSampleRec);
      tr.appendChild(typeOfTest);
      tr.appendChild(dateOfQCA);
      tr.appendChild(insuranceVerifiedTSGVerification);
      tr.appendChild(telemedName);
      tr.appendChild(dateSubmittedToTelemed);
      tr.appendChild(dateTelemedReturned);
      tr.appendChild(dateBioconfirmRecApp);
      tr.appendChild(datePaid);
      tr.appendChild(dateLabRecordedApp);
      tr.appendChild(labType);
      tr.appendChild(state);
      tr.appendChild(status);
      tr.appendChild(month);
      tr.appendChild(insuranceCompany);
      tr.appendChild(notes);
      tr.appendChild(rejectionDate);
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

      let patientName = document.createElement('th');
      let patientPhoneNumber = document.createElement('th');
      let promoCode = document.createElement('th');
      let agent = document.createElement('th');
      let manager = document.createElement('th');
      let dateAppRec = document.createElement('th');
      let dateSampleRec = document.createElement('th');
      let typeOfTest = document.createElement('th');
      let dateOfQCA = document.createElement('th');
      let insuranceVerifiedTSGVerification = document.createElement('th');
      let telemedName = document.createElement('th');
      let dateSubmittedToTelemed = document.createElement('th');
      let dateTelemedReturned = document.createElement('th');
      let dateBioconfirmRecApp = document.createElement('th');
      let datePaid = document.createElement('th');
      let dateLabRecordedApp = document.createElement('th');
      let labType = document.createElement('th');
      let state = document.createElement('th');
      let status = document.createElement('th');
      let month = document.createElement('th');
      let insuranceCompany = document.createElement('th');
      let notes = document.createElement('th');
      let rejectionDate = document.createElement('th');
      let patientIDPhoto = document.createElement('th');
      let insuranceCardPhotoFront = document.createElement('th');
      let insuranceCardPhotoBack = document.createElement('th');
      let additionalInsuranceCards = document.createElement('th');
      let consentRecording = document.createElement('th');
      let dateCreated = document.createElement('th');
      let createdBy = document.createElement('th');
      let updatedBy = document.createElement('th');
      let userPromoCode = document.createElement('th');

      patientName.textContent = 'Patient Name';
      patientPhoneNumber.textContent = 'Patient Phone Number';
      promoCode.textContent = 'Promo Code';
      agent.textContent = 'Agent';
      manager.textContent = 'Manager';
      dateAppRec.textContent = 'Date App Rec';
      dateSampleRec.textContent = 'Date Sample Rec';
      typeOfTest.textContent = 'Type of Test';
      dateOfQCA.textContent = 'Date of QCA';
      insuranceVerifiedTSGVerification.textContent = 'Insurance Verified TSG Verification';
      telemedName.textContent = 'Telemed Name';
      dateSubmittedToTelemed.textContent = 'Date Submitted to Telemed';
      dateTelemedReturned.textContent = 'Date Telemed Return';
      dateBioconfirmRecApp.textContent = 'Date Bioconfirm Rec App';
      datePaid.textContent = 'Date Paid';
      dateLabRecordedApp.textContent = 'Date Lab Recorded App';
      labType.textContent = 'Lab Type';
      state.textContent = 'State';
      status.textContent = 'Status';
      month.textContent = 'Month';
      insuranceCompany.textContent = 'Insurance Company';
      notes.textContent = 'Notes';
      rejectionDate.textContent = 'Rejection Date';
      patientIDPhoto.textContent = 'Patient ID Photo';
      insuranceCardPhotoFront.textContent = 'Insurance Card Photo Front';
      insuranceCardPhotoBack.textContent = 'Insurance Card Photo Back';
      additionalInsuranceCards.textContent = 'Additional Insurance Cards';
      consentRecording.textContent = 'Consent Recording';
      dateCreated.textContent = 'Date Created';
      createdBy.textContent = 'Created by';
      updatedBy.textContent = 'Updated by';
      userPromoCode.textContent = 'User Promo Code';

      tr.appendChild(patientName);
      tr.appendChild(patientPhoneNumber);
      tr.appendChild(promoCode);
      tr.appendChild(agent);
      tr.appendChild(manager);
      tr.appendChild(dateAppRec);
      tr.appendChild(dateSampleRec);
      tr.appendChild(typeOfTest);
      tr.appendChild(dateOfQCA);
      tr.appendChild(insuranceVerifiedTSGVerification);
      tr.appendChild(telemedName);
      tr.appendChild(dateSubmittedToTelemed);
      tr.appendChild(dateTelemedReturned);
      tr.appendChild(dateBioconfirmRecApp);
      tr.appendChild(datePaid);
      tr.appendChild(dateLabRecordedApp);
      tr.appendChild(labType);
      tr.appendChild(state);
      tr.appendChild(status);
      tr.appendChild(month);
      tr.appendChild(insuranceCompany);
      tr.appendChild(notes);
      tr.appendChild(rejectionDate);
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
    },
    generatePDF: function() {
      let columns = this.generatePDFColumns();

      let pdf = new jsPDF('l', 'pt');
      let options = {
        theme: 'grid',
        headerStyles: {
          fillColor: [233, 236, 239],
          textColor: 26
        }
      }
      pdf.autoTable(columns, this.bioconfirms, options);
      pdf.save('Bioconfirm-Report-' + Date.now() + '.pdf');
    },
    generatePDFColumns: function() {
      return [
        {title: "Patient Name", dataKey: "patient_name"},
        {title: "Promo Code", dataKey: "promo_code"},
        {title: "Agent Name", dataKey: "agent"},
        {title: "Date Submitted to Telemed", dataKey: "date_submitted_to_telemed"},
        {title: "Date Telemed Returned", dataKey: "date_telemed_returned"},
        {title: "Date Application Recorded", dataKey: "date_app_rec"},
        {title: "Date Sample Recorded", dataKey: "date_sample_rec"},
        {title: "Date Paid", dataKey: "date_paid"},
        {title: "Insurance Company Name", dataKey: "insurance_company"},
        {title: "Rejection Date", dataKey: "rejection_date"},
        {title: "Date Submitted to Tamika ins verifier", dataKey: "date_submitted_to_tamika_ins_verifier"},
      ];
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
      for (let i = this.startPage; i <= this.endPage; i++) pages.push(i);
      return pages;
    },
  },
});
