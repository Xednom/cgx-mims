Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#pc-and-fb-app',
  delimiters: ['[[',']]'],
  data: {
    pcfbs: [],
    buttonsLoading: [],
    message: null,
    loading: false,
    saving: false,
    searching: false,
    loading_view: false,
    currentPcFb: {},
    agentNames: [],
    newPcFb: {
        'submission_date': "",
        'promo_code': "",
        'agent_name': "",
        'agent_email': "",
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

    // from date queries
    pcfb_from_date_created: '',
    pcfb_from_date_faxed_to_pharmacy: '',
    pcfb_from_submission_date: '',
    pcfb_patient_first_name: '',
    pcfb_patient_last_name: '',

    // to date queries
    pcfb_to_date_created: '',
    pcfb_to_date_faxed_to_pharmacy: '',
    pcfb_to_submission_date: '',

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
    this.getAgentNames();
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
    searchPcFbs: function () {
      let api_url = `/api/v1/pain-cream-and-foot-bath/?date_created__gte=${this.pcfb_from_date_created}&date_created__lte=${this.pcfb_to_date_created}&date_faxed_to_pharmacy__gte=${this.pcfb_from_date_faxed_to_pharmacy}&date_faxed_to_pharmacy__lte=${this.pcfb_to_date_faxed_to_pharmacy}&submission_date__gte=${this.pcfb_from_submission_date}&submission_date__lte=${this.pcfb_to_submission_date}&patient_first_name=${this.pcfb_patient_first_name}&patient_last_name=${this.pcfb_patient_last_name}`;
      /*if(this.search_term!==''||this.search_term!==null) {
         api_url = `/api/v1/pain-cream-and-foot-bath/?search=${this.search_term}`
       }*/
      this.searching = true;
      this.$http.get(api_url)
        .then((response) => {
          this.pcfbs = response.data;
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
      this.saving = true;
      axios.post('/api/v1/pain-cream-and-foot-bath/', formData).then((response) => {
        swal({
          title: "TSG System",
          text: "Data has been saved successfully for Pain Cream and Foot Bath",
          icon: "success",
          buttons: false,
          timer: 2000
        });
        this.saving = false;
        this.getPcFbs();
        // reset form
        this.resetFields();
        // return the current date after resetting the form
        this.setDefaultDates();
        // reset form
        event.target.reset();
      })
      .catch((err) => {
        this.saving = false;
        swal({
          title: "TSG System",
          text: JSON.stringify(err.body),
          icon: "error",
          buttons: "Ok",
        });
        console.log(err);
      })
    },
    // view data
    viewPcFb: function (id) {
      this.loading_view = true;
      this.$http.get(`/api/v1/pain-cream-and-foot-bath/${id}/`)
          .then((response) => {
            this.currentPcFb = response.data;
            this.loading_view = false;
          })
          .catch((err) => {
            this.loading_view = false;
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
      a.download = 'PCFB-Report-' + Date.now() + '.xlsx';
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
      let pcfbs = this.pcfbs;
      let tableRows = '';

      for (let i=0; i<pcfbs.length; i++) {
        tableRows += this.htmlConverter(
          this.generateData(pcfbs[i])
          );
      }

      return tableRows

    },
    generateData: function(pcfb) {
      let tr = document.createElement('tr');

      let submissionDate = document.createElement('td');
      let promoCode = document.createElement('td');
      let agent = document.createElement('td');
      let agentEmail = document.createElement('td');
      let patientFirstName = document.createElement('td');
      let patientLastName = document.createElement('td');
      let birthDate = document.createElement('td');
      let gender = document.createElement('td');
      let patientPhoneNumber = document.createElement('td');
      let bestTimeToCall = document.createElement('td');
      let streetAddress = document.createElement('td');
      let streetAddress2 = document.createElement('td');
      let city = document.createElement('td');
      let stateProvince = document.createElement('td');
      let postalZipCode = document.createElement('td');
      let country = document.createElement('td');
      let insuranceType = document.createElement('td');
      let medicareMedicaidPolicy = document.createElement('td');
      let ppoHmoInformationMemID = document.createElement('td');
      let ppoHmoInformationPpoName = document.createElement('td');
      let insuranceStatus = document.createElement('td');
      let locationOfPain = document.createElement('td');
      let levelOfPain = document.createElement('td');
      let discomfort = document.createElement('td');
      let feqOfPain = document.createElement('td');
      let prescribePainCream = document.createElement('td');
      let locationOfFootIssue = document.createElement('td');
      let describeFootIssue = document.createElement('td');
      let orderStatus = document.createElement('td');
      let dateFaxedToPharmacy = document.createElement('td');
      let ip = document.createElement('td');
      let submissionID = document.createElement('td');
      let patientIDPhoto = document.createElement('td');
      let insuranceCardPhoto = document.createElement('td');
      let ppoCardPhoto = document.createElement('td');
      let consentRecording = document.createElement('td');
      let dateCreated = document.createElement('td');
      let createdBy = document.createElement('td');
      let updatedBy = document.createElement('td');
      let userPromoCode = document.createElement('td');

      submissionDate.textContent = pcfb['submission_date'];
      promoCode.textContent = pcfb['promo_code'];
      agent.textContent = pcfb['agent'];
      agentEmail.textContent = pcfb['agent_email'];
      patientFirstName.textContent = pcfb['patient_first_name'];
      patientLastName.textContent = pcfb['patient_last_name'];
      birthDate.textContent = pcfb['birth_date'];
      gender.textContent = pcfb['gender'];
      patientPhoneNumber.textContent = pcfb['patient_phone_number'];
      bestTimeToCall.textContent = pcfb['best_time_to_call'];
      streetAddress.textContent = pcfb['street_address'];
      streetAddress2.textContent = pcfb['street_address_2'];
      city.textContent = pcfb['city'];
      stateProvince.textContent = pcfb['state_province'];
      postalZipCode.textContent = pcfb['postal_zip_code'];
      country.textContent = pcfb['country'];
      insuranceType.textContent = pcfb['insurance_type'];
      medicareMedicaidPolicy.textContent = pcfb['medicare_medicaid_policy'];
      ppoHmoInformationMemID.textContent = pcfb['ppo_hmo_information_mem_id'];
      ppoHmoInformationPpoName.textContent = pcfb['ppo_hmo_information_ppo_name'];
      insuranceStatus.textContent = pcfb['insurance_status'];
      locationOfPain.textContent = pcfb['location_of_pain'];
      levelOfPain.textContent = pcfb['level_of_pain'];
      discomfort.textContent = pcfb['discomfort'];
      feqOfPain.textContent = pcfb['feq_of_pain'];
      prescribePainCream.textContent = pcfb['prescribe_pain_cream'];
      locationOfFootIssue.textContent = pcfb['location_of_foot_issue'];
      describeFootIssue.textContent = pcfb['describe_foot_issue'];
      orderStatus.textContent = pcfb['order_status'];
      dateFaxedToPharmacy.textContent = pcfb['date_faxed_to_pharmacy'];
      ip.textContent = pcfb['ip'];
      submissionID.textContent = pcfb['submission_id'];
      patientIDPhoto.textContent = pcfb['patient_id_photo'];
      insuranceCardPhoto.textContent = pcfb['insurance_card_photo'];
      ppoCardPhoto.textContent = pcfb['ppo_card_photo'];
      consentRecording.textContent = pcfb['consent_recording'];
      dateCreated.textContent = pcfb['date_created'];
      createdBy.textContent = pcfb['created_by'];
      updatedBy.textContent = pcfb['updated_by'];
      userPromoCode.textContent = pcfb['user_promo_code'];

      tr.appendChild(submissionDate);
      tr.appendChild(promoCode);
      tr.appendChild(agent);
      tr.appendChild(agentEmail);
      tr.appendChild(patientFirstName);
      tr.appendChild(patientLastName);
      tr.appendChild(birthDate);
      tr.appendChild(gender);
      tr.appendChild(patientPhoneNumber);
      tr.appendChild(bestTimeToCall);
      tr.appendChild(streetAddress);
      tr.appendChild(streetAddress2);
      tr.appendChild(city);
      tr.appendChild(stateProvince);
      tr.appendChild(postalZipCode);
      tr.appendChild(country);
      tr.appendChild(insuranceType);
      tr.appendChild(medicareMedicaidPolicy);
      tr.appendChild(ppoHmoInformationMemID);
      tr.appendChild(ppoHmoInformationPpoName);
      tr.appendChild(insuranceStatus);
      tr.appendChild(locationOfPain);
      tr.appendChild(levelOfPain);
      tr.appendChild(discomfort);
      tr.appendChild(feqOfPain);
      tr.appendChild(prescribePainCream);
      tr.appendChild(locationOfFootIssue);
      tr.appendChild(describeFootIssue);
      tr.appendChild(orderStatus);
      tr.appendChild(dateFaxedToPharmacy);
      tr.appendChild(ip);
      tr.appendChild(submissionID);
      tr.appendChild(patientIDPhoto);
      tr.appendChild(insuranceCardPhoto);
      tr.appendChild(ppoCardPhoto);
      tr.appendChild(consentRecording);
      tr.appendChild(dateCreated);
      tr.appendChild(createdBy);
      tr.appendChild(updatedBy);
      tr.appendChild(userPromoCode);

      return tr
    },
    generateExcelHeader: function() {
      let tr = document.createElement('tr');

      let submissionDate = document.createElement('th');
      let promoCode = document.createElement('th');
      let agent = document.createElement('th');
      let agentEmail = document.createElement('th');
      let patientFirstName = document.createElement('th');
      let patientLastName = document.createElement('th');
      let birthDate = document.createElement('th');
      let gender = document.createElement('th');
      let patientPhoneNumber = document.createElement('th');
      let bestTimeToCall = document.createElement('th');
      let streetAddress = document.createElement('th');
      let streetAddress2 = document.createElement('th');
      let city = document.createElement('th');
      let stateProvince = document.createElement('th');
      let postalZipCode = document.createElement('th');
      let country = document.createElement('th');
      let insuranceType = document.createElement('th');
      let medicareMedicaidPolicy = document.createElement('th');
      let ppoHmoInformationMemID = document.createElement('th');
      let ppoHmoInformationPpoName = document.createElement('th');
      let insuranceStatus = document.createElement('th');
      let locationOfPain = document.createElement('th');
      let levelOfPain = document.createElement('th');
      let discomfort = document.createElement('th');
      let feqOfPain = document.createElement('th');
      let prescribePainCream = document.createElement('th');
      let locationOfFootIssue = document.createElement('th');
      let describeFootIssue = document.createElement('th');
      let orderStatus = document.createElement('th');
      let dateFaxedToPharmacy = document.createElement('th');
      let ip = document.createElement('th');
      let submissionID = document.createElement('th');
      let patientIDPhoto = document.createElement('th');
      let insuranceCardPhoto = document.createElement('th');
      let ppoCardPhoto = document.createElement('th');
      let consentRecording = document.createElement('th');
      let dateCreated = document.createElement('th');
      let createdBy = document.createElement('th');
      let updatedBy = document.createElement('th');
      let userPromoCode = document.createElement('th');

      submissionDate.textContent = 'Submission Date';
      promoCode.textContent = 'Promo Code';
      agent.textContent = 'Agent';
      agentEmail.textContent = 'Agent Email';
      patientFirstName.textContent = 'Patient First Name';
      patientLastName.textContent = 'Patient Last Name';
      birthDate.textContent = 'Birthdate';
      gender.textContent = 'Gender';
      patientPhoneNumber.textContent = 'Patient Phone Number';
      bestTimeToCall.textContent = 'Best Time to Call';
      streetAddress.textContent = 'Street Address';
      streetAddress2.textContent = 'Street Address 2';
      city.textContent = 'City';
      stateProvince.textContent = 'State Province';
      postalZipCode.textContent = 'Postal Zip Code';
      country.textContent = 'Country';
      insuranceType.textContent = 'Insurance Type';
      medicareMedicaidPolicy.textContent = 'Medicare Medicaid Policy';
      ppoHmoInformationMemID.textContent = 'PPO HMO Information Mem ID';
      ppoHmoInformationPpoName.textContent = 'PPO HMO Information PPO Name';
      insuranceStatus.textContent = 'Insurance Status';
      locationOfPain.textContent = 'Location of Pain';
      levelOfPain.textContent = 'Level of Pain';
      discomfort.textContent = 'Discomfort';
      feqOfPain.textContent = 'Frequency of Pain';
      prescribePainCream.textContent = 'Prescribe Pain Cream';
      locationOfFootIssue.textContent = 'Location of Foot Issue';
      describeFootIssue.textContent = 'Describe Foot Issue';
      orderStatus.textContent = 'Order Status';
      dateFaxedToPharmacy.textContent = 'Date Faxed to Pharmacy';
      ip.textContent = 'IP';
      submissionID.textContent = 'Submission ID';
      patientIDPhoto.textContent = 'patient ID Photo';
      insuranceCardPhoto.textContent = 'Insurance Card Photo';
      ppoCardPhoto.textContent = 'PPO Card Photo';
      consentRecording.textContent = 'Consent Recording';
      dateCreated.textContent = 'Date Created';
      createdBy.textContent = 'Created by';
      updatedBy.textContent = 'Updated by';
      userPromoCode.textContent = 'User Promo Code';

      tr.appendChild(submissionDate);
      tr.appendChild(promoCode);
      tr.appendChild(agent);
      tr.appendChild(agentEmail);
      tr.appendChild(patientFirstName);
      tr.appendChild(patientLastName);
      tr.appendChild(birthDate);
      tr.appendChild(gender);
      tr.appendChild(patientPhoneNumber);
      tr.appendChild(bestTimeToCall);
      tr.appendChild(streetAddress);
      tr.appendChild(streetAddress2);
      tr.appendChild(city);
      tr.appendChild(stateProvince);
      tr.appendChild(postalZipCode);
      tr.appendChild(country);
      tr.appendChild(insuranceType);
      tr.appendChild(medicareMedicaidPolicy);
      tr.appendChild(ppoHmoInformationMemID);
      tr.appendChild(ppoHmoInformationPpoName);
      tr.appendChild(insuranceStatus);
      tr.appendChild(locationOfPain);
      tr.appendChild(levelOfPain);
      tr.appendChild(discomfort);
      tr.appendChild(feqOfPain);
      tr.appendChild(prescribePainCream);
      tr.appendChild(locationOfFootIssue);
      tr.appendChild(describeFootIssue);
      tr.appendChild(orderStatus);
      tr.appendChild(dateFaxedToPharmacy);
      tr.appendChild(ip);
      tr.appendChild(submissionID);
      tr.appendChild(patientIDPhoto);
      tr.appendChild(insuranceCardPhoto);
      tr.appendChild(ppoCardPhoto);
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
    generatePDF: function(id, buttonNumber) {
      this.loadButton(buttonNumber);

      let link = document.createElement('a');
      link.href = `/rx/${id}/pcfb-report.pdf`;
      link.download = 'PCFB-Report-' + Date.now();
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    },
    loadButton: function(buttonNumber) {
      Vue.set(this.buttonsLoading, buttonNumber, 1);

      let self = this;

      setTimeout(function() {
        Vue.set(self.buttonsLoading, buttonNumber, 0);
      }, 8000);
    }
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
      for (let i = this.startPage; i <= this.endPage; i++) pages.push(i);
      return pages;
    },
  },
});
