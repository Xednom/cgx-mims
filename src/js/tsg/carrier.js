Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#carrier-app',
  delimiters: ['[[',']]'],
  data: {
    carriers: [],
    agentNames: [],
    managerNames: [],
    testChoices: [],
    statuses: [],
    message: null,
    loading: false,
    saving: false,
    searching: false,
    loading_view: false,
    csrf_token: ['csrf_token'],
    currentCarrier: {},
    newCarrier: {
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
    },
    search_term: '',

    // queries for Carrier app from date and to date
    // From dates
    carrier_from_date_app_rec: '',
    carrier_from_date_sample_rec: '',
    carrier_from_date_of_qca: '',
    carrier_from_date_created: '',
    
    // To dates
    carrier_to_date_app_rec: '',
    carrier_to_date_sample_rec: '',
    carrier_to_date_of_qca: '',
    carrier_to_date_created: '',
    carrier_search_patient_name: '',

    // for pagination
    currentPage: 1,
    pageSize: RECORDS_PER_PAGE,
    startPage: 1,
    endPage: null,
    maxPages: RECORDS_PER_PAGE,
    paginatedRecords: [],
  },
  mounted: function() {
    this.getCarriers();
    this.getAgentNames();
    this.getManagerNames();
    this.getStatuses();
    this.getTestChoices();
    this.setDefaultDates();
  },
  methods: {
    setDefaultDates: function() {
      let currentDate = moment(new Date()).format("YYYY-MM-DD");
      this.newCarrier.date_app_rec = currentDate;
    },
    onFileChange: function (event) {
      this.newCarrier[event.target.name] = event.target.files[0];
    },
    resetFields: function() {
        Object.keys(this.newCarrier).forEach(key => {
        this.newCarrier[key] = ''
      })
    },
    getCarriers: function() {
      let api_url = '/api/v1/carrier/';
      /*if(this.search_term!==''||this.search_term!==null) {
        api_url = `/api/v1/carrier/?search=${this.search_term}`
      }*/
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
    searchCarriers: function () {
      // Search function
      api_url = `/api/v1/carrier/?date_app_rec__gte=${this.carrier_from_date_app_rec}&date_app_rec__lte=${this.carrier_to_date_app_rec}&date_sample_rec__gte=${this.carrier_from_date_sample_rec}&date_sample_rec__lte=${this.carrier_to_date_sample_rec}&date_of_qca__gte=${this.carrier_from_date_of_qca}&date_of_qca__lte=${this.carrier_to_date_of_qca}&date_created__gte=${this.carrier_from_date_created}&date_created__lte=${this.carrier_to_date_created}&patient_name=${this.carrier_search_patient_name}`
      this.searching = true;
      this.$http.get(api_url)
        .then((response) => {
          this.carriers = response.data;
          this.searching = false;

          this.generateExcelFile('wow', 'wow');
        })
        .catch((err) => {
          this.searching = false;
          console.log(err);
        })
    },
    downloadCarriers: function () {
      api_url = `/api/v1/carrier/?date_app_rec__gte=${this.carrier_from_date_app_rec}&date_app_rec__lte=${this.carrier_to_date_app_rec}&date_sample_rec__gte=${this.carrier_from_date_sample_rec}&date_sample_rec__lte=${this.carrier_to_date_sample_rec}&date_of_qca__gte=${this.carrier_from_date_of_qca}&date_of_qca__lte=${this.carrier_to_date_of_qca}&date_created__gte=${this.carrier_from_date_created}&date_created__lte=${this.carrier_to_date_created}&patient_name=${this.carrier_search_patient_name}?format=xlsx`      
      this.$http.get(api_url)
        .then((response) => {
            let a = document.createElement('A')
            a.href = response.data
            a.download = true
            document.body.appendChild(a)
            a.click()
          })
        .catch((err) => {
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
      this.saving = true;
      axios.post('/api/v1/carrier/', formData).then((response) => {
        console.log(formData);
        swal({
          title: "TSG System",
          text: "Data has been saved successfully for Carrier",
          icon: "success",
          buttons: false,
          timer: 2000
        });
        this.saving = false;
        this.getCarriers();
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
          text: "Something has happened when processing the data, if the error persist. Please contact your Administrator.",
          icon: "error",
          buttons: "Ok",
        });
        this.saving = false;
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
    // viewing of full datas
    viewCarrier: function(id) {
      this.loading_view = true;
      this.$http.get(`/api/v1/carrier/${id}/`)
          .then((response) => {
            this.loading_view = false;
            this.currentCarrier = response.data;
          })
          .catch((err) => {
            this.loading_view = false;
            console.log(err);
          })
    },
    getPaginatedRecords: function() {
      const startIndex = this.startIndex;
      this.paginatedRecords = this.carriers.slice().splice(startIndex, this.pageSize);
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
      a.download = 'Carrier-Report-' + Date.now() + '.xlsx';
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
      let carriers = this.carriers;
      let tableRows = '';

      for (let i=0; i<carriers.length; i++) {
        tableRows += this.htmlConverter(
          this.generateData(carriers[i])
          );
      }

      return tableRows

    },
    generateData: function(carrier) {
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

      patientName.textContent = carrier['patient_name'];
      patientPhoneNumber.textContent = carrier['patient_phone_number'];
      promoCode.textContent = carrier['promo_code'];
      agent.textContent = carrier['agent'];
      manager.textContent = carrier['manager'];
      dateAppRec.textContent = carrier['date_app_rec'];
      dateSampleRec.textContent = carrier['date_sample_rec'];
      typeOfTest.textContent = carrier['type_of_test'];
      dateOfQCA.textContent = carrier['date_of_qca'];
      insuranceVerifiedTSGVerification.textContent = carrier['insurance_verified_tsg_verification'];
      telemedName.textContent = carrier['telemed_name'];
      dateSubmittedToTelemed.textContent = carrier['date_submitted_to_telemed'];
      dateTelemedReturned.textContent = carrier['date_telemed_returned'];
      dateBioconfirmRecApp.textContent = carrier['date_bioconfim_rec_app'];
      datePaid.textContent = carrier['date_paid'];
      dateLabRecordedApp.textContent = carrier['date_lab_recorded_app'];
      labType.textContent = carrier['lab_type'];
      state.textContent = carrier['state'];
      status.textContent = carrier['status'];
      month.textContent = carrier['month'];
      notes.textContent = carrier['notes'];
      rejectionDate.textContent = carrier['rejection_date'];
      patientIDPhoto.textContent = carrier['patient_id_photo'];
      insuranceCardPhotoFront.textContent = carrier['insurance_card_photo_front'];
      insuranceCardPhotoBack.textContent = carrier['insurance_card_photo_back'];
      additionalInsuranceCards.textContent = carrier['additional_insurance_cards'];
      consentRecording.textContent = carrier['consent_recording'];
      dateCreated.textContent = carrier['date_created'];
      createdBy.textContent = carrier['created_by'];
      updatedBy.textContent = carrier['updated_by'];
      userPromoCode.textContent = carrier['user_promo_code'];

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
    generateExcelHeader: function(carrier) {
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

      let pdf = new jsPDF('p', 'pt', 'a4');
      let carriers = this.carriers;
      let imgData = "data:image/png;base64,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/vif3X3XFZcf+AaxrpF9Lh6QfnqXdh06dTu3150//dmuXQeuoKeecuD137RfPTRg0ODLrvjBj28Y1z79tIqlD5YuxiOvGXF217NeWfRq7wv7Drp8yOChV53X+4Ibxt2kIMMrdBjVr580fuz16emnvbTgle7n9VZ7Lr5k0NCrhuV/9tnNN447p0d3r1wNadq06Uknnfja62/Yhl88YJCipVatWnqzK6SltU5MTFRkmXnZkOHXXGd/uyHoELX5MO8KAABqj+p9qaVxSsoD0+6b8/Ts7/fra39XSVfuzp07Tbj15gsv+J4mL7s0856sXzZv3mx9bm7Dhg2m3XfPmWdkVCxaAxRJzPztb24aPza1efP3133w4frc73To8PvHp9uXmg+/9NPazX36Sb89n33+ef/vXzz3j0+Ovu7aGn8G067tqY88+ED3bmcrOinYulUByvD/uSrkl4ndzu7607t+op2vMvv370+qF/qjSDlEbT6cuwIAgNojoTzKt50AAABQueo9kQIAAICPQAoAAMARgRQAAIAjAikAAABHBFIAAACOCKQAAAAcEUgBAAA4IpACAABwRCAFAADgiEAKAADAEYEUAACAIwIpAAAARwRSAAAAjgikAAAAHBFIAQAAOCKQAgAAcEQgBQAA4IhACgAAwBGBFAAAgCMCKQAAAEcEUgAAAI4IpAAAABwlbNm2w0sCAACgOhLKy8u9JAAAAKqDV3sAAACOCKQAAAAcEUgBAAA4IpACAABwRCAFAADgiEAKAADAEYEUAACAIwIpAAAARwRSAAAAjgikAAAAHBFIAQAAOCKQAgAAcEQgBQAA4IhACgAAwBGBFAAAgCMCKQAAAEcEUgAAAI4IpAAAABwRSAEAADgikAIAAHD07QdSm/LzZz351Oeff+FN13p79+17/He/P6fnd9u27/joY9O93Npt//79i//6N/0rKyvzsgAAwEGrRiD1zrurFDoE/w0YNPiJP8zesWOHV6L69u0rfvjXj9039YFHHn2spKTEyz0sbHOuuPLqarVfDc6afO8DDz1SVLSrU8fTExISvBm125p/vzfupltvvu0OJbwsAABw0A7qidSH69dPe+DBq0dcm/fRx15WpbZu3fboY9Mn33OfwhHLOe64Y9NPa9egQYPzzz/3uOOOs8yDt+HTT++dev9vfjvDm645n2zY8Pqbb7ZITX3u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";

      pdf.setFont('helvetica');

      for (let i=0; i<carriers.length; i++) {
        if (i != 0) {
          pdf.addPage();
        }

        this.setPDFLayout(pdf, carriers[i], imgData);
      }

      pdf.save('Carrier-Report-' + Date.now() + '.pdf');
    },
    setPDFLayout: function(pdf, data, imgData) {
      pdf.addImage(imgData, 'PNG', 0, 20, 596, 820);

      pdf.setFontSize(16);
      pdf.setTextColor(35);
      pdf.text(168, 50, data.patient_name);

      pdf.setFontSize(10);
      pdf.setTextColor(63);

      pdf.text(17, 153, data.patient_name || "");
      pdf.text(212, 153, data.patient_phone_number || "");
      pdf.text(407, 153, data.date_submitted_to_tamika_ins_verifier || "");
      pdf.text(17, 215, data.promo_code || "");
      pdf.text(212, 215, data.status || "");
      pdf.text(407, 215, data.state || "");
      pdf.text(17, 276, data.type_of_test || "");
      pdf.text(212, 276, data.agent || "");
      pdf.text(407, 276, data.telemed_name || "");
      pdf.text(17, 338, data.insurance_company || "");

      pdf.text(17, 400, data.notes || "");

      pdf.text(17, 671, data.notes || "");
      pdf.text(212, 671, data.notes || "");
      pdf.text(407, 671, data.notes || "");
      pdf.text(17, 733, data.notes || "");
      pdf.text(212, 733, data.notes || "");
      pdf.text(407, 733, data.notes || "");
      pdf.text(17, 795, data.notes || "");
      pdf.text(212, 795, data.notes || "");
      pdf.text(407, 795, data.notes || "");

      if (data.patient_id_photo != '') {
        pdf.addPage();
        this.getDataURI(data.patient_id_photo, function(imageURI) {
          pdf.addImage(imageURI, 0, 0, 500, 500);
        });
      }

      if (data.insurance_card_photo_back != '') {
        pdf.addPage();
        this.getDataURI(data.insurance_card_photo_back, function(imageURI) {
          pdf.addImage(imageURI, 0, 0, 500, 500);
        });
      }

      if (data.insurance_card_photo_front != '') {
        pdf.addPage();
        this.getDataURI(data.insurance_card_photo_front, function(imageURI) {
          pdf.addImage(imageURI, 0, 0, 500, 500);
        });
      }

      if (data.additional_insurance_cards != '') {
        pdf.addPage();
        this.getDataURI(data.additional_insurance_cards, function(imageURI) {
          pdf.addImage(imageURI, 0, 0, 500, 500);
        });
      }

      if (data.consent_recording != '') {
        pdf.addPage();
        this.getDataURI(data.consent_recording, function(imageURI) {
          pdf.addImage(imageURI, 0, 0, 500, 500);
        });
      }
    },
    getDataURI: function(url, callback) {
      let image = new Image();
      image.setAttribute('crossOrigin', 'anonymous');
      image.crossOrigin = 'anonymous';

      image.onload = function() {
        let canvas = document.createElement('canvas');
        canvas.width = this.naturalWidth;
        canvas.height = this.naturalHeight;

        let context = canvas.getContext('2d');
        context.fillStyle = '#fff';
        context.fillRect(0, 0, canvas.width, canvas.height);

        canvas.getContext('2d').drawImage(this, 0, 0);

        callback(canvas.toDataURL('image/jpeg'));
      }

      image.src = url;
    }
  },
  watch: {
    carriers: function(newCarrierRecords, oldCarrierRecords) {
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
      return this.carriers.length;
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
