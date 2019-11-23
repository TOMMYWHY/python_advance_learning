	$(function  () {
		var sestion_h=$('.section').height();
//		alert(sestion_h);
		$('.section1').height(sestion_h);
		$('.section2').height(sestion_h);
		$('.section3').height(sestion_h);
//		$('.section4').height(sestion_h);
		$('.section5').height(sestion_h);
		$('.section6').height(sestion_h);
		
		//  ========== 
		//  = section3 = 
		//  ========== 
		
		$(".icon_each").mouseover(function() {
		$(this).siblings().stop().fadeTo("fast", 0.2);//return
	});
	$(".icon_each").mouseout(function() {
		$(this).siblings().stop().fadeTo("fast", 1);
	});
		
//  ========== 
//  = section5 = 
//  ========== 
//$('source_p2').mouseover(function  () {
//		$(this).css()
//})


	})