<template id="Close">
<bootstrapModal :title="title" :large=true @ok="addClosure()">

    <div class="modal-body">
        <form name="closeForm" class="form-horizontal">
            <div class="row">
			    <alert :show.sync="showError" type="danger">{{errorString}}</alert>
                <div class="form-group">
                    <div class="col-md-2">
                        <label for="open_cg_range_start">Closure start: </label>
                    </div>
                    <div class="col-md-4">
                        <div class='input-group date' :id='close_cg_range_start'>
                            <input  name="closure_start"  v-model="statusHistory.range_start" type='text' class="form-control" />
                            <span class="input-group-addon">
                                <span class="glyphicon glyphicon-calendar"></span>
                            </span>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <label for="open_cg_range_start_time"> Start time: </label>
                    </div>
                    <div class="col-md-3">
                        <div class="input-group date" :id='close_cg_range_start_time'>
                            <input name="closure_start_time" v-model="statusHistory.range_start_time" type='text' class="form-control" />
                            <span class="input-group-addon">
                                <span class="glyphicon glyphicon-time"> </span>
                            </span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="form-group">
                    <div class="col-md-2">
                        <label for="open_cg_range_start">Reopen: </label>
                    </div>
                    <div class="col-md-4">
                        <div class='input-group date' :id='close_cg_range_end'>
                            <input name="closure_end" v-model="statusHistory.range_end" type='text' class="form-control" />
                            <span class="input-group-addon">
                                <span class="glyphicon glyphicon-calendar"></span>
                            </span>
                        </div>
                    </div>
                    <div class="col-md-2">
                        <label for="open_cg_range_end_time"> End time: </label>
                    </div>
                    <div class="col-md-3">
                        <div class="input-group date" :id='close_cg_range_end_time'>
                            <input name="closure_end_time" v-model="statusHistory.range_end_time" type='text' class="form-control" />
                            <span class="input-group-addon">
                                <span class="glyphicon glyphicon-time"> </span>
                            </span>
                        </div>
                    </div>
                </div>
            </div>
            <reason type="close" v-model="statusHistory.closure_reason" ></reason>
            <div v-show="requireDetails" class="row">
                <div class="form-group">
                    <div class="col-md-2">
                        <label>Details: </label>
                    </div>
                    <div class="col-md-4">
                        <textarea name="closure_details" v-model="statusHistory.details" class="form-control" id="close_cg_details"></textarea>
                    </div>
                </div>
            </div>
        </form>
    </div>

</bootstrapModal>
</template>

<script>
import bootstrapModal from '../bootstrap-modal.vue'
import { $, datetimepicker,api_endpoints, validate, helpers, bus } from '../../../hooks'
import alert from '../alert.vue'
import reason from '../reasons.vue'
module.exports = {
    name: 'Close',
    props: {
        statusHistory: {
            type: Object,
            required: true
        },
        title: {
            type: String,
            required: true
        }
    },
    data: function() {
        let vm = this;
        return {
            id:'',
            current_closure: '',
            closeStartPicker: '',
            closeStartTimePicker: '',
            showDetails:false,
            closeEndPicker: '',
            closeEndTimePicker: '',
            errors: false,
            errorString: '',
            form: '',
            isOpen: false,
            reasons: [],
            close_cg_range_start: 'close_cg_range_start'+vm._uid,
            close_cg_range_start_time: 'close_cg_range_start_time'+vm.id,
            close_cg_range_end: 'close_cg_range_end'+vm._uid,
            close_cg_range_end_time: 'close_cg_range_end_time'+vm.id,
        }
    },
    computed: {
        showError: function() {
            var vm = this;
            return vm.errors;
        },
        isModalOpen: function() {
            return this.isOpen;
        },
        closure_id: function() {
            return this.statusHistory.id ? this.statusHistory.id : '';
        },
        requireDetails: function() {
            let vm = this;
            var check = this.statusHistory.closure_reason
            for (var i = 0; i < vm.reasons.length; i++){
                if (vm.reasons[i].id == check){
                    return vm.reasons[i].detailRequired;
                }
            }
        },
    },
    components: {
        bootstrapModal,
        alert,
        reason
    },
    methods: {
        close: function() {
            this.errors = false;
            this.errorString = '';
            this.isOpen = false;
            this.statusHistory.id = '';
            this.statusHistory.range_start= '';
            this.statusHistory.range_start_time= '';
            this.statusHistory.range_end= '';
            this.statusHistory.range_end_time= '';
            this.statusHistory.status= '1';
            this.statusHistory.details= '';
            this.statusHistory.reason = '';
            this.statusHistory.closure_reason = '';
            var today = new Date();
            this.closeEndPicker.data('DateTimePicker').clear();
            this.closeStartPicker.data('DateTimePicker').clear();
        },
        addClosure: function() {
            if (this.form.valid()){
                if (!this.closure_id){
                    this.$emit('closeRange');
                }else {
                    this.$emit('updateRange');
                }
            }
        },
        addFormValidations: function() {
            let vm = this;
            vm.form.validate({
                rules: {
                    closure_start: "required",
                    closure_start_time: "required",
                    closure_end: "required",
                    closure_end_time: "required",
                    closure_status: "required",
                    closure_details: {
                        required: {
                            depends: function(el){
                                var check = vm.statusHistory.closure_reason
                                for (var i = 0; i < vm.reasons.length; i++){
                                    if (vm.reasons[i].id == check){
                                        return vm.reasons[i].detailRequired;
                                    }
                                }
                            }
                        }
                    }
                },
                messages: {
                    closure_start: "Enter a start date",
                    closure_start_time: "Enter a start time",
                    closure_end: "Enter a end date",
                    closure_end_time: "Enter a end time",
                    closure_status: "Select a closure reason from the options",
                    closure_details: "Details required if Other reason is selected"
                },
                showErrors: function(errorMap, errorList) {

                    $.each(this.validElements(), function(index, element) {
                        var $element = $(element);
                        $element.attr("data-original-title", "").parents('.form-group').removeClass('has-error');
                    });

                    // destroy tooltips on valid elements
                    $("." + this.settings.validClass).tooltip("destroy");

                    // add or update tooltips
                    for (var i = 0; i < errorList.length; i++) {
                        var error = errorList[i];
                        $(error.element)
                            .tooltip({
                                trigger: "focus"
                            })
                            .attr("data-original-title", error.message)
                            .parents('.form-group').addClass('has-error');
                    }
                }
            });
       }
    },
    mounted: function() {
        var vm = this;
        vm.statusHistory.status=1;
        vm.statusHistory.reason='';
        vm.closeEndPicker = $('#'+vm.close_cg_range_end);
        vm.closeStartPicker = $('#'+vm.close_cg_range_start).datetimepicker({
            format: 'DD/MM/YYYY',
            minDate: new Date()
        });
        vm.closeStartTimePicker = $('#'+vm.close_cg_range_start_time).datetimepicker({
            format: 'HH:mm',
        });
        vm.closeEndPicker.datetimepicker({
            format: 'DD/MM/YYYY',
            useCurrent: false
        });
        vm.closeEndTimePicker = $('#'+vm.close_cg_range_end_time).datetimepicker({
            format: 'HH:mm',
        })
        vm.closeStartPicker.on('dp.change', function(e){
            vm.statusHistory.range_start = vm.closeStartPicker.data('DateTimePicker').date() != null ? vm.closeStartPicker.data('DateTimePicker').date().format('DD/MM/YYYY') : '';
            e.date != null ? vm.closeEndPicker.data("DateTimePicker").minDate(e.date): '';
        });
        vm.closeStartTimePicker.on('dp.change', function(e){
            vm.statusHistory.range_start_time = vm.closeStartTimePicker.data('DateTimePicker').date().format('HH:mm');
        });
        vm.closeEndPicker.on('dp.change', function(e){
            vm.statusHistory.range_end = vm.closeEndPicker.data('DateTimePicker').date() != null  ? vm.closeEndPicker.data('DateTimePicker').date().format('DD/MM/YYYY') : '';
        });
        vm.closeEndTimePicker.on('dp.change', function(e){
            vm.statusHistory.range_end_time = vm.closeEndTimePicker.data('DateTimePicker').date().format('HH:mm');
        });
        vm.form = $(document.forms.closeForm);
        vm.addFormValidations();
        bus.$once('closeReasons',setReasons => {
            vm.reasons = setReasons;
        });
    },
};
</script>
