Vue.http.headers.common['X-CSRFToken'] = "{{ csrf_token }}";
new Vue({
    el: '#supplies-app',
    delimiters: ['[[', ']]'],
    data: {
        supplies: [],
        message: null,
        loading: false,
        currentSupplies: {},
        newSupplies: {
            'sale_rep_name': "",
            'sale_rep_number': "",
            'email': "",
            'shipping_labels_qty_req': "",
            'shipping_labels_qty_auth': "",
            'shipping_boxes_qty_req': "",
            'shipping_boxes_qty_auth': "",
            'shipping_bags_qty_req': "",
            'shipping_bags_qty_auth': "",
            'specimen_bags_qty_req': "",
            'specimen_bags_qty_auth': "",
            'tox_cups_qty_req': "",
            'tox_cups_qty_auth': "",
            'tox_req_forms_qty_req': "",
            'tox_req_forms_qty_auth': "",
            'pgx_swabs_qty_req': "",
            'pgx_swabs_qty_auth': "",
            'pgx_swabs_req_forms_qty_req': "",
            'pgx_swabs_req_forms_qty_auth': "",
            'pgx_medical_necessity_forms_qty_req': "",
            'pgx_medical_necessity_forms_qty_auth': "",
            'cgx_swabs_qty_req': "",
            'cgx_swabs_qty_auth': "",
            'cgx_req_forms_qty_req': "",
            'cgx_req_forms_qty_auth': "",
            'tubes_tiger_qty_req': "",
            'tubes_tiger_qty_auth': "",
            'tubes_lavender_qty_req': "",
            'tubes_lavender_qty_auth': "",
            'tubes_red_top_qty_req': "",
            'tubes_red_top_qty_auth': "",
            'tubes_blue_qty_req': "",
            'tubes_blue_qty_auth': "",
            'tubes_dark_blue_qty_req': "",
            'tubes_dark_blue_qty_auth': "",
            'tubes_violet_qty_req': "",
            'tubes_violet_qty_auth': "",
            'straight_needle_18_qty_req': "",
            'straight_needle_18_qty_auth': "",
            'straight_needle_20_qty_req': "",
            'straight_needle_20_qty_auth': "",
            'straight_needle_21_qty_req': "",
            'straight_needle_21_qty_auth': "",
            'straight_needle_22_qty_req': "",
            'straight_needle_22_qty_auth': "",
            'straight_needle_23_qty_req': "",
            'straight_needle_23_qty_auth': "",
            'butterfly_needle_18_qty_req': "",
            'butterfly_needle_18_qty_auth': "",
            'butterfly_needle_20_qty_req': "",
            'butterfly_needle_20_qty_auth': "",
            'butterfly_needle_21_qty_req': "",
            'butterfly_needle_21_qty_auth': "",
            'butterfly_needle_22_qty_req': "",
            'butterfly_needle_22_qty_auth': "",
            'butterfly_needle_23_qty_req': "",
            'butterfly_needle_23_qty_auth': "",
            'needle_vacuum_tubes_18_qty_req': "",
            'needle_vacuum_tubes_18_qty_auth': "",
            'uti_cups_qty_req': "",
            'uti_cups_qty_auth': "",
            'uti_urine_tubes_qty_req': "",
            'uti_urine_tubes_qty_auth': "",
            'culture_swabs_qty_req': "",
            'culture_swabs_qty_auth': "", 
            'tourniquets_qty_req': "",
            'tourniquets_qty_auth': "",
            'gauze_qty_req': "",
            'gauze_qty_auth': "",
            'bandages_qty_req': "",
            'bandages_qty_auth': "",
            'gel_pack_qty_req': "",
            'gel_pack_qty_auth': "",
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
    mounted: function () {
        this.getSupplies();
    },
    methods: {
        resetFields: function () {
            Object.keys(this.newSupplies).forEach(key => {
                this.newSupplies[key] = ''
            })
        },
        getSupplies: function () {
            let api_url = '/api/v1/supplies';
            /*if(this.search_term!==''||this.search_term!==null) {
               api_url = `/api/v1/pain-cream-and-foot-bath/?search=${this.search_term}`
             }*/
            this.loading = false;
            this.$http.get(api_url)
                .then((response) => {
                    this.supplies = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        // new code using axios
        addSupplies: function (event) {
            const formData = new FormData();
            Object.keys(this.newSupplies).forEach((key) => {
                let obj = this.newSupplies[key];
                if (obj instanceof File) {
                    formData.append(key, obj, obj.name)
                } else {
                    formData.append(key, obj);
                }
            });
            this.loading = true;
            this.$http.post('/api/v1/supplies/', formData).then((response) => {
                swal({
                    title: "TSG System",
                    text: "Request Successful, in the mean time we'll process your request as soon as we can. You'll receive an email regarding it. Thank you",
                    icon: "success",
                    buttons: "Ok",
                });
                this.loading = false;
                this.getSupplies();
                // reset form
                this.resetFields();
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
        viewSupplies: function (id) {
            this.loading = true;
            this.$http.get(`/api/v1/supplies/${id}/`)
                .then((response) => {
                    this.currentSupplies = response.data;
                    this.loading = false;
                })
                .catch((err) => {
                    this.loading = false;
                    console.log(err);
                })
        },
        getPaginatedRecords: function () {
            const startIndex = this.startIndex;
            this.paginatedRecords = this.pcfbs.slice().splice(startIndex, this.pageSize);
        },
        goToPage: function (page) {
            if (page < 1) {
                return this.currentPage = 1;
            }
            if (page > this.totalPages) {
                return this.currentPage = this.totalPages;
            }
            this.currentPage = page;
        },
        setPageGroup: function () {
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
        pcfbs: function (newPcFbsRecords, oldpcfbsRecords) {
            this.setPageGroup();
            this.getPaginatedRecords();
        },
        currentPage: function (newCurrentPage, oldCurrentPage) {
            this.setPageGroup();
            this.getPaginatedRecords();
        },
    },
    computed: {
        totalItems: function () {
            return this.pcfbs.length;
        },
        totalPages: function () {
            return Math.ceil(this.totalItems / this.pageSize);
        },
        startIndex: function () {
            return (this.currentPage - 1) * this.pageSize;
        },
        endIndex: function () {
            return Math.min(this.startIndex + this.pageSize - 1, this.totalItems - 1);
        },
        pages: function () {
            let pages = [];
            for (let i = this.startPage; i < this.endPage; i++) pages.push(i);
            return pages;
        },
    },
});
