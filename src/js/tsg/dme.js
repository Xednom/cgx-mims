Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
  el: '#dme-app',
  delimiters: ['[[',']]'],
  data: {
    dmes: [],
    message: null,
    loading: false,
    saving: false,
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
      this.saving = true;
      axios.post('/api/v1/dme/', formData).then((response) => {
        swal({
          title: "TSG System",
          text: "Data has been saved successfully for DME",
          icon: "success",
          buttons: false,
          timer: 2000
        });
        this.saving = false;
        this.getDmes();
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
      a.download = 'DME-Report-' + Date.now() + '.xlsx';
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
      let dmes = this.dmes;
      let tableRows = '';

      for (let i=0; i<dmes.length; i++) {
        tableRows += this.htmlConverter(
          this.generateData(dmes[i])
          );
      }

      return tableRows

    },
    generateData: function(dme) {
      let tr = document.createElement('tr');

      let submissionDate = document.createElement('td');
      let firstName = document.createElement('td');
      let lastName = document.createElement('td');
      let agentsPromoCode = document.createElement('td');
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
      let patientIDPhoto = document.createElement('td');
      let insuranceType = document.createElement('td');
      let policyNumber = document.createElement('td');
      let ppoHmoInformationMemID = document.createElement('td');
      let ppoHmoInformationPpoName = document.createElement('td');
      let insuranceStatus = document.createElement('td');
      let insuranceNotes = document.createElement('td');
      let insuranceCardPhotoFront = document.createElement('td');
      let insuranceCardPhotoBack = document.createElement('td');
      let additionalInsuranceCards = document.createElement('td');
      let locationOfBackPain = document.createElement('td');
      let locationOfShoulderPain = document.createElement('td');
      let locationOfKneePain = document.createElement('td');
      let locationOfAnklePain = document.createElement('td');
      let locationOfElbowPain = document.createElement('td');
      let locationOfWristPain = document.createElement('td');
      let height = document.createElement('td');
      let weight = document.createElement('td');
      let sizeOfBrace = document.createElement('td');
      let majorMedicalConditions = document.createElement('td');
      let causeOfPainDiscomfort = document.createElement('td');
      let levelOfPain = document.createElement('td');
      let experiencingDiscomfort = document.createElement('td');
      let frequencyOfPain = document.createElement('td');
      let describePain = document.createElement('td');
      let painSymptoms = document.createElement('td');
      let painWorse = document.createElement('td');
      let treatmentsTried = document.createElement('td');
      let seenDoctor = document.createElement('td');
      let surgeries = document.createElement('td');
      let consentRecording = document.createElement('td');
      let ip = document.createElement('td');
      let submissionID = document.createElement('td');
      let editLink = document.createElement('td');
      let dateCreated = document.createElement('td');
      let createdBy = document.createElement('td');
      let updatedBy = document.createElement('td');
      let userPromoCode = document.createElement('td');

      submissionDate.textContent = dme['submission_date'];
      firstName.textContent = dme['submission_date'];
      lastName.textContent = dme['submission_date'];
      agentsPromoCode.textContent = dme['promo_code'];
      agentEmail.textContent = dme['agentEmail'];
      patientFirstName.textContent = dme['patient_first_name'];
      patientLastName.textContent = dme['patient_last_name'];
      birthDate.textContent = dme['birth_date'];
      gender.textContent = dme['gender'];
      patientPhoneNumber.textContent = dme['patient_phone_number'];
      bestTimeToCall.textContent = dme['best_time_to_call'];
      streetAddress.textContent = dme['street_address'];
      streetAddress2.textContent = dme['street_address_2'];
      city.textContent = dme['city'];
      stateProvince.textContent = dme['state_province'];
      postalZipCode.textContent = dme['postal_zip_code'];
      country.textContent = dme['country'];
      patientIDPhoto.textContent = dme['patient_id_photo'];
      insuranceType.textContent = dme['insurance_type'];
      policyNumber.textContent = dme['medicare_medicaid_policy'];
      ppoHmoInformationMemID.textContent = dme['ppo_hmo_information_mem_id'];
      ppoHmoInformationPpoName.textContent = dme['ppo_hmo_information_ppo_name'];
      insuranceStatus.textContent = dme['insurance_status'];
      insuranceNotes.textContent = dme['location_of_pain'];
      insuranceCardPhotoFront.textContent = dme['insurance_card_photo'];
      insuranceCardPhotoBack.textContent = dme['insurance_card_photo'];
      additionalInsuranceCards.textContent = dme['insurance_card_photo'];
      locationOfBackPain.textContent = dme['level_of_pain'];
      locationOfShoulderPain.textContent = dme['level_of_pain'];
      locationOfKneePain.textContent = dme['level_of_pain'];
      locationOfAnklePain.textContent = dme['level_of_pain'];
      locationOfElbowPain.textContent = dme['level_of_pain'];
      locationOfWristPain.textContent = dme['level_of_pain'];
      height.textContent = dme['level_of_pain'];
      weight.textContent = dme['level_of_pain'];
      sizeOfBrace.textContent = dme['level_of_pain'];
      majorMedicalConditions.textContent = dme['level_of_pain'];
      causeOfPainDiscomfort.textContent = dme['level_of_pain'];
      levelOfPain.textContent = dme['level_of_pain'];
      experiencingDiscomfort.textContent = dme['discomfort'];
      frequencyOfPain.textContent = dme['feq_of_pain'];
      describePain.textContent = dme['prescribe_pain_cream'];
      painSymptoms.textContent = dme['prescribe_pain_cream'];
      painWorse.textContent = dme['prescribe_pain_cream'];
      treatmentsTried.textContent = dme['location_of_foot_issue'];
      seenDoctor.textContent = dme['describe_foot_issue'];
      surgeries.textContent = dme['order_status'];
      consentRecording.textContent = dme['consent_recording'];
      ip.textContent = dme['ip'];
      submissionID.textContent = dme['submission_id'];
      editLink.textContent = dme['ppo_card_photo'];
      dateCreated.textContent = dme['date_created'];
      createdBy.textContent = dme['created_by'];
      updatedBy.textContent = dme['updated_by'];
      userPromoCode.textContent = dme['user_promo_code'];

      tr.appendChild(submissionDate);
      tr.appendChild(firstName);
      tr.appendChild(lastName);
      tr.appendChild(agentsPromoCode);
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
      tr.appendChild(patientIDPhoto);
      tr.appendChild(insuranceType);
      tr.appendChild(policyNumber);
      tr.appendChild(ppoHmoInformationMemID);
      tr.appendChild(ppoHmoInformationPpoName);
      tr.appendChild(insuranceStatus);
      tr.appendChild(insuranceNotes);
      tr.appendChild(insuranceCardPhotoFront);
      tr.appendChild(insuranceCardPhotoBack);
      tr.appendChild(additionalInsuranceCards);
      tr.appendChild(locationOfBackPain);
      tr.appendChild(locationOfShoulderPain);
      tr.appendChild(locationOfKneePain);
      tr.appendChild(locationOfAnklePain);
      tr.appendChild(locationOfElbowPain);
      tr.appendChild(locationOfWristPain);
      tr.appendChild(height);
      tr.appendChild(weight);
      tr.appendChild(sizeOfBrace);
      tr.appendChild(majorMedicalConditions);
      tr.appendChild(causeOfPainDiscomfort);
      tr.appendChild(levelOfPain);
      tr.appendChild(experiencingDiscomfort);
      tr.appendChild(frequencyOfPain);
      tr.appendChild(describePain);
      tr.appendChild(painSymptoms);
      tr.appendChild(painWorse);
      tr.appendChild(treatmentsTried);
      tr.appendChild(seenDoctor);
      tr.appendChild(surgeries);
      tr.appendChild(consentRecording);
      tr.appendChild(ip);
      tr.appendChild(submissionID);
      tr.appendChild(editLink);
      tr.appendChild(dateCreated);
      tr.appendChild(createdBy);
      tr.appendChild(updatedBy);
      tr.appendChild(userPromoCode);

      return tr
    },
    generateExcelHeader: function() {
      let tr = document.createElement('tr');

      let submissionDate = document.createElement('th');
      let firstName = document.createElement('th');
      let lastName = document.createElement('th');
      let agentsPromoCode = document.createElement('th');
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
      let patientIDPhoto = document.createElement('th');
      let insuranceType = document.createElement('th');
      let policyNumber = document.createElement('th');
      let ppoHmoInformationMemID = document.createElement('th');
      let ppoHmoInformationPpoName = document.createElement('th');
      let insuranceStatus = document.createElement('th');
      let insuranceNotes = document.createElement('th');
      let insuranceCardPhotoFront = document.createElement('th');
      let insuranceCardPhotoBack = document.createElement('th');
      let additionalInsuranceCards = document.createElement('th');
      let locationOfBackPain = document.createElement('th');
      let locationOfShoulderPain = document.createElement('th');
      let locationOfKneePain = document.createElement('th');
      let locationOfAnklePain = document.createElement('th');
      let locationOfElbowPain = document.createElement('th');
      let locationOfWristPain = document.createElement('th');
      let height = document.createElement('th');
      let weight = document.createElement('th');
      let sizeOfBrace = document.createElement('th');
      let majorMedicalConditions = document.createElement('th');
      let causeOfPainDiscomfort = document.createElement('th');
      let levelOfPain = document.createElement('th');
      let experiencingDiscomfort = document.createElement('th');
      let frequencyOfPain = document.createElement('th');
      let describePain = document.createElement('th');
      let painSymptoms = document.createElement('th');
      let painWorse = document.createElement('th');
      let treatmentsTried = document.createElement('th');
      let seenDoctor = document.createElement('th');
      let surgeries = document.createElement('th');
      let consentRecording = document.createElement('th');
      let ip = document.createElement('th');
      let submissionID = document.createElement('th');
      let editLink = document.createElement('th');
      let dateCreated = document.createElement('th');
      let createdBy = document.createElement('th');
      let updatedBy = document.createElement('th');
      let userPromoCode = document.createElement('th');

      submissionDate.textContent = 'Submission Date';
      firstName.textContent = 'First Name';
      lastName.textContent = 'Last Name';
      agentsPromoCode.textContent = 'Agents Promo Code';
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
      patientIDPhoto.textContent = 'patient ID Photo';
      insuranceType.textContent = 'Insurance Type';
      policyNumber.textContent = 'Policy Number';
      ppoHmoInformationMemID.textContent = 'PPO HMO Information Mem ID';
      ppoHmoInformationPpoName.textContent = 'PPO HMO Information PPO Name';
      insuranceStatus.textContent = 'Insurance Status';
      insuranceNotes.textContent = 'Insurance Notes';
      insuranceCardPhotoFront.textContent = 'Insurance Card Photo Front';
      insuranceCardPhotoBack.textContent = 'Insurance Card Photo Back';
      additionalInsuranceCards.textContent = 'Additional Insurance Cards';
      locationOfBackPain.textContent = 'Location of Back Pain';
      locationOfShoulderPain.textContent = 'Location of Shoulder Pain';
      locationOfKneePain.textContent = 'Location of Knee Pain';
      locationOfAnklePain.textContent = 'Location of Ankle Pain';
      locationOfElbowPain.textContent = 'Location of Elbow Pain';
      locationOfWristPain.textContent = 'Location of Wrist Pain';
      height.textContent = 'Height';
      weight.textContent = 'Weight';
      sizeOfBrace.textContent = 'Size of Brace';
      majorMedicalConditions.textContent = 'Major Medical Conditions';
      causeOfPainDiscomfort.textContent = 'Cause of Pain/Discomfort';
      levelOfPain.textContent = 'Level of Pain';
      experiencingDiscomfort.textContent = 'Experiencing Discomfort';
      frequencyOfPain.textContent = 'Frequency of Pain';
      describePain.textContent = 'Describe Pain';
      painSymptoms.textContent = 'Pain Symptoms';
      painWorse.textContent = 'Pain Worse';
      treatmentsTried.textContent = 'Treatments Tried';
      seenDoctor.textContent = 'Seen Doctor';
      surgeries.textContent = 'Surgeries';
      consentRecording.textContent = 'Consent Recording';
      ip.textContent = 'IP';
      submissionID.textContent = 'Submission ID';
      editLink.textContent = 'Edit Link';
      dateCreated.textContent = 'Date Created';
      createdBy.textContent = 'Created by';
      updatedBy.textContent = 'Updated by';
      userPromoCode.textContent = 'User Promo Code';

      tr.appendChild(submissionDate);
      tr.appendChild(firstName);
      tr.appendChild(lastName);
      tr.appendChild(agentsPromoCode);
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
      tr.appendChild(patientIDPhoto);
      tr.appendChild(insuranceType);
      tr.appendChild(policyNumber);
      tr.appendChild(ppoHmoInformationMemID);
      tr.appendChild(ppoHmoInformationPpoName);
      tr.appendChild(insuranceStatus);
      tr.appendChild(insuranceNotes);
      tr.appendChild(insuranceCardPhotoFront);
      tr.appendChild(insuranceCardPhotoBack);
      tr.appendChild(additionalInsuranceCards);
      tr.appendChild(locationOfBackPain);
      tr.appendChild(locationOfShoulderPain);
      tr.appendChild(locationOfKneePain);
      tr.appendChild(locationOfAnklePain);
      tr.appendChild(locationOfElbowPain);
      tr.appendChild(locationOfWristPain);
      tr.appendChild(height);
      tr.appendChild(weight);
      tr.appendChild(sizeOfBrace);
      tr.appendChild(majorMedicalConditions);
      tr.appendChild(causeOfPainDiscomfort);
      tr.appendChild(levelOfPain);
      tr.appendChild(experiencingDiscomfort);
      tr.appendChild(frequencyOfPain);
      tr.appendChild(describePain);
      tr.appendChild(painSymptoms);
      tr.appendChild(painWorse);
      tr.appendChild(treatmentsTried);
      tr.appendChild(seenDoctor);
      tr.appendChild(surgeries);
      tr.appendChild(consentRecording);
      tr.appendChild(ip);
      tr.appendChild(submissionID);
      tr.appendChild(editLink);
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
