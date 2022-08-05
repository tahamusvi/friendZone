
/**
* Theme: Adminto Admin Template
* Author: Coderthemes
* Demo: Editable (Inline editing)
* 
*/


$(function(){

    //modify buttons style
    $.fn.editableform.buttons = 
    '<button type="submit" class="btn btn-primary editable-submit btn-sm waves-effect waves-light"><i class="zmdi zmdi-check"></i></button>' +
    '<button type="button" class="btn editable-cancel btn-sm waves-effect"><i class="zmdi zmdi-close"></i></button>';
    
    //editables 
    $('#username').editable({
     type: 'text',
     pk: 1,
     name: 'نام کاربری',
     title: 'نام کاربری خود را وارد کنید'
   });
    
    $('#firstname').editable({
      validate: function(value) {
       if($.trim(value) == '') return 'پر کردن این فیلد اجباریست';
     }
   });
    
    $('#sex').editable({
      prepend: "بدون انتخاب",
      source: [
      {value: 1, text: 'آقا'},
      {value: 2, text: 'بانو'}
      ],
      display: function(value, sourceData) {
       var colors = {"": "#98a6ad", 1: "#5fbeaa", 2: "#5d9cec"},
       elem = $.grep(sourceData, function(o){return o.value == value;});

       if(elem.length) {
         $(this).text(elem[0].text).css("color", colors[value]);
       } else {
         $(this).empty();
       }
     }
   });
    
    $('#status').editable();
    
    $('#group').editable({
      showbuttons: false
    });

    $('#dob').editable();

    $('#comments').editable({
      showbuttons: 'bottom'
    });

    //inline


  $('#inline-username').editable({
     type: 'text',
     pk: 1,
     name: 'username',
     title: 'Enter username',
     mode: 'inline'
   });
    
    $('#inline-firstname').editable({
      validate: function(value) {
       if($.trim(value) == '') return 'این فیلد اجباری است';
     },
     mode: 'inline'
   });
    
    $('#inline-sex').editable({
      prepend: "بدون انتخاب",
      mode: 'inline',
      source: [
      {value: 1, text: 'آقا'},
      {value: 2, text: 'بانو'}
      ],
      display: function(value, sourceData) {
       var colors = {"": "#98a6ad", 1: "#5fbeaa", 2: "#5d9cec"},
       elem = $.grep(sourceData, function(o){return o.value == value;});

       if(elem.length) {
         $(this).text(elem[0].text).css("color", colors[value]);
       } else {
         $(this).empty();
       }
     }
   });
    
    $('#inline-status').editable({mode: 'inline'});
    
    $('#inline-group').editable({
      showbuttons: false,
      mode: 'inline'
    });

    $('#inline-dob').editable({mode: 'inline'});

    $('#inline-comments').editable({
      showbuttons: 'bottom',
      mode: 'inline'
    });



  });