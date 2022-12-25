//  for page 500

$(".full-screen").mousemove(function(event) {
    var eye = $(".eye");
    var x = (eye.offset().left) + (eye.width() / 2);
    var y = (eye.offset().top) + (eye.height() / 2);
    var rad = Math.atan2(event.pageX - x, event.pageY - y);
    var rot = (rad * (180 / Math.PI) * -1) + 180;
    eye.css({
      '-webkit-transform': 'rotate(' + rot + 'deg)',
      '-moz-transform': 'rotate(' + rot + 'deg)',
      '-ms-transform': 'rotate(' + rot + 'deg)',
      'transform': 'rotate(' + rot + 'deg)'
    });
  });
  

  // corousel multi items


  // donate




  $('#show_honor_fields').click(function(){
    if (this.checked) {
        $('.honor-form').show();
        $('#donately_form').remove();
    } else{
        $('.honor-form').hide();
        $('#donately_form_with_codes').remove();
      $("#honor_name").text('someone special');
        $('.donation-container').append( '<div id="donately_form"><script  class="donately-donation-form" src="https://s3-us-west-1.amazonaws.com/static-dntly-com/form.js"  async="async" type="text/javascript" data-donately-ssl="true" data-donately-id="198" data-donately-address="true" data-donately-comment="true" data-donately-phone="true"/></div>' );
    }
});


//PLEDGE FORM ON /DONATE/PLEDGE
//We have to load form.js after submit so we can untilize the tracking codes feature
$('#updateform').click(function(){

$('.honor-form').hide();
// $('#show_honor_fields').attr('disabled', 'disabled');


var show_honor_fields = 'Honor Field: ' + $('#show_honor_fields').val(), 
gift_type = 'Gift Type: ' + $('#gift_type').val(), 
honoree_first_name = 'Honoree Name: ' + $('#honoree_name').val(), 
notify_recip_name = 'Notify Name: ' + $('#notify_recip_name').val(), 
notify_recip_street1 = 'Address: ' + $('#notify_recip_street1').val() + ' ' + $('#notify_recip_street2').val() + ' ' + $('#notify_recip_city').val() + ' ' + $('#notify_recip_state').val() + ' ' + $('#notify_recip_zip').val() + ' ' + $('#notify_recip_country').val(), 


codes = show_honor_fields + ' ' + gift_type + ' ' + honoree_first_name + ' ' + notify_recip_name + ' ' + notify_recip_street1;

$("#honor_name").text($('#honoree_name').val());

$('#donately_form').remove();

$(".donation-container").append( '<div id="donately_form_with_codes"><script class="donately-donation-form" src="https://s3-us-west-1.amazonaws.com/static-dntly-com/form.js"  async="async" type="text/javascript" data-donately-ssl="true" data-donately-tracking-codes="' + codes + '" data-donately-id="198" data-donately-address="true" data-donately-comment="true" data-donately-phone="true"/></div>' );

return false;
});


// 403 page
var root = document.documentElement;
var eyef = document.getElementById('eyef');
var cx = document.getElementById("eyef").getAttribute("cx");
var cy = document.getElementById("eyef").getAttribute("cy");

document.addEventListener("mousemove", evt => {
  let x = evt.clientX / innerWidth;
  let y = evt.clientY / innerHeight;

  root.style.setProperty("--mouse-x", x);
  root.style.setProperty("--mouse-y", y);
  
  cx = 115 + 30 * x;
  cy = 50 + 30 * y;
  eyef.setAttribute("cx", cx);
  eyef.setAttribute("cy", cy);
  
});

document.addEventListener("touchmove", touchHandler => {
  let x = touchHandler.touches[0].clientX / innerWidth;
  let y = touchHandler.touches[0].clientY / innerHeight;

  root.style.setProperty("--mouse-x", x);
  root.style.setProperty("--mouse-y", y);
});

// 408 page

$(function() {
  var intervalID = setInterval(function(){
    document.getElementById('requestText').innerHTML += '.'
  }, 500)
  var animationTime = 5000;
  setTimeout(main(), 250);
  function main(){
    $('#hh1').animate({scrollTop:$("#hh1-main").offset().top}, animationTime, 'swing', function() {
  });
    setTimeout(function(){
      $('#hh2').animate({scrollTop:$("#hh2-main").offset().top}, animationTime, 'swing', function() { 
  });
    }, 100);
    setTimeout(function(){
      $('#symbol').animate({scrollTop:$("#symbol-main").offset().top}, animationTime, 'swing', function() { 
  });
    }, 200);
    setTimeout(function(){
      $('#mm1').animate({scrollTop:$("#mm1-main").offset().top}, animationTime, 'swing', function() { 
  });
    }, 300);
    setTimeout(function(){
      $('#mm2').animate({scrollTop:$("#mm2-main").offset().top}, animationTime, 'swing', function() {
  });
    }, 400);
    setTimeout(function(){
      $('#requestText').addClass('fade-out');
        clearInterval(intervalID);
        setTimeout(function(){
        document.getElementById('requestText').innerHTML = 'Request Timed Out!' ;
          $('#requestText').addClass('fade-in');
        }, 1001)
    },animationTime-1250)
  }
});
