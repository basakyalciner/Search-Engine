$(document).ready(function(){
//TAB START
   $(".tab-container1[value='1']").css("display","block");
   $(".tab-button").click(function(){
       
       var indexnumber = $(this).index();
       if(indexnumber==$(".tab-container1[value='1']").index()){
           
           $(".tab-container1").css("display","none");
           $(".tab-container1[value='1']").attr("value","0");
       }
       else{ 
           $(".tab-container1[value='1']").slideToggle();
           $(".tab-container1[value='1']").attr("value","0");
           
           my_index = indexnumber+1;
           $(".tab-container1:nth-child("+my_index+")").attr("value","1");
           $(".tab-container1:nth-child("+my_index+")").slideToggle();
        }
         
   });    
//TAB END
//ACTIVE "li" START
    $(".tabs-li ul li:first-child").addClass("active-tab");
    $(".tabs-li ul li").click(function(){
        $(".tabs-li ul li").removeClass("active-tab");
        $(this).addClass("active-tab");
    });
//ACTIVE "li" END
});