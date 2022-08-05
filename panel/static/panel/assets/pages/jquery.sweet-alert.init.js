/**
 * Theme: Adminto Admin Template
 * Author: Coderthemes
 * SweetAlert
 */

!function ($) {
    "use strict";

    var SweetAlert = function () {
    };

    //examples 
    SweetAlert.prototype.init = function () {

        //Basic
        $('#sa-basic').click(function () {
            swal("این یک پیغام است");
        });

        //A title with a text under
        $('#sa-title').click(function () {
            swal("سربرگ یک پیغام!", "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.")
        });

        //Success Message
        $('#sa-success').click(function () {
            swal("کارت عالی بود!", "لورم ایپسوم متن ساختگی با تولید سادگی نامفهوم از صنعت چاپ و با استفاده از طراحان گرافیک است.", "success")
        });

        //Warning Message
        $('#sa-warning').click(function () {
            swal({
                title: "مطمئنی ؟؟",
                text: "میخوای این فایل رو پاک کنی؟؟",
                type: "warning",
                showCancelButton: true,
                confirmButtonClass: 'btn-warning',
                confirmButtonText: "بله . پاکش کن !",
                closeOnConfirm: false
            }, function () {
                swal("پاک شد!", "فایل با موفقیت پاک شد", "success");
            });
        });

        //Parameter
        $('#sa-params').click(function () {
            swal({
                title: "مطمئنی ؟؟",
                text: "میخوای این فایل رو پاک کنی؟؟",
                type: "warning",
                showCancelButton: true,
                confirmButtonColor: "#DD6B55",
                confirmButtonText: "بله . پاکش کن!",
                cancelButtonText: "نه  . بیخیال!",
                closeOnConfirm: false,
                closeOnCancel: false
            }, function (isConfirm) {
                if (isConfirm) {
                    swal("پاک شد!", "فایل با موفقیت پاک شد", "success");
                } else {
                    swal("لغو شد", "ممنون که این کارو نکردی :)", "error");
                }
            });
        });

        //Custom Image
        $('#sa-image').click(function () {
            swal({
                title: "عالیه!",
                text: "کارت واقعا حرف نداره",
                imageUrl: "assets/plugins/bootstrap-sweetalert/thumbs-up.jpg"
            });
        });

        //Auto Close Timer
        $('#sa-close').click(function () {
            swal({
                title: "پیغام خود به خود بسته میشود",
                text: "بعد از 2 ثانیه",
                timer: 2000,
                showConfirmButton: false
            });
        });

        //Primary
        $('#primary-alert').click(function () {
            swal({
                title: "آیا مطمئنی ؟",
                text: "برای برگردوندن فایل پاک شده آماده ای؟؟",
                type: "info",
                showCancelButton: true,
                cancelButtonClass: 'btn-success waves-effect waves-light',
                confirmButtonClass: 'btn-primary waves-effect waves-light',
                confirmButtonText: 'اولیه!'
            });
        });

        //Info
        $('#info-alert').click(function () {
            swal({
                title: "آیا مطمئنی ؟",
                text: "این کار مورد قبول شماست یا نه ؟؟",
                type: "info",
                showCancelButton: true,
                confirmButtonClass: 'btn-info waves-effect waves-light',
                confirmButtonText: 'اعلانها!'
            });
        });
		

        //Success
        $('#success-alert').click(function () {
            swal({
                title: "مطمئنی ؟؟",
                text: "برای برگردوندن فایل پاک شده آماده ای؟؟",
                type: "success",
                showCancelButton: true,
                confirmButtonClass: 'btn-success waves-effect waves-light',
                confirmButtonText: 'قبول!'
            });
        });

        //Warning
        $('#warning-alert').click(function () {
            swal({
                title: "مطمئنی ؟؟",
                text: "برای برگردوندن فایل پاک شده آماده ای؟؟",
                type: "warning",
                showCancelButton: true,
                confirmButtonClass: 'btn-warning waves-effect waves-light',
                confirmButtonText: 'خطا!'
            });
        });

        //Danger
        $('#danger-alert').click(function () {
            swal({
                title: "مطمئنی ؟؟",
                text: "برای برگردوندن فایل پاک شده آماده ای؟؟",
                type: "error",
                showCancelButton: true,
                confirmButtonClass: 'btn-danger waves-effect waves-light',
                confirmButtonText: 'خطر!'
            });
        });


    },
        //init
        $.SweetAlert = new SweetAlert, $.SweetAlert.Constructor = SweetAlert
}(window.jQuery),

//initializing 
    function ($) {
        "use strict";
        $.SweetAlert.init()
    }(window.jQuery);