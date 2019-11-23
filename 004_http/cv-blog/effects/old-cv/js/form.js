$(function() {

    $('.mform').ajaxForm();
  
}); 
function sendmail (btn) {
	
//alert('aa');
	var $name= $("#f_name");
	var $email= $("#f_email");
	var $message= $("#f_message");
	var $send_m= $("#send_message");
//	$send_m.val($name.val() +'<br/>'+$email.val()+'<br/>'+ $message.val());
	$send_m.val('Name:'+$name.val() +'<br/>'+'Email:'+$email.val()+'<br/>'+ $message.val());
	
   }
function aa() {
//	alert('cc');
	var sb = document.getElementById("f_subject");
	var cn = document.getElementById("send_message");
	if(sb.value==''||cn.value==''){
	return false;
	}else{
		 alert('sucess!');
		 
		
	}
}
