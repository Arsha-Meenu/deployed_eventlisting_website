$(document).ready(function(){
    


// like 
           console.log("working set");

       
    $('.like-form').submit(function(e){
        e.preventDefault()
       const event_id=$(".like-btn").val()
       const token=$('input[name=csrfmiddlewaretoken]').val() 
       const url =$(this).attr('action') 
          $.ajax({
               method:"POST",
               url:url,
               headers:{"X-CSRFToken": token},
               data:{
                   'event_id':event_id
               },
               success:function(response){
                   console.log(response)
                   if(response.disliked ===true){
                       $(".like-icon").addClass("text-primary")
                   }else{
                       $(".like-icon").removeClass("text-primary")
                   }
               
                   likes=$("#like-count").text(response.like_count)
                   parseInt(likes)
                   
               },
               error:function(response){
                   console.log('failed', response)
               }
           }) 
   
   })
           
    //dislike ajax call

    $('.dislike-form').submit(function(e){
           e.preventDefault()
          const event_id=$(".dislike-btn").val()
          const token=$('input[name=csrfmiddlewaretoken]').val() 
          const url =$(this).attr('action') 
             $.ajax({
                  method:"POST",
                  url:url,
                  headers:{"X-CSRFToken": token},
                  data:{
                      'event_id':event_id
                  },
                  success:function(response){
                      console.log(response)
                      if(response.disliked ===true){
                          $(".dislike-icon").addClass("text-primary")
                      }else{
                          $(".dislike-icon").removeClass("text-primary")
                      }
                  
                      dislikes=$("#dislike-count").text(response.dislike_count)
                      parseInt(dislikes)
                      
                  },
                  error:function(response){
                      console.log('failed', response)
                  }
              }) 
      
      })
   


});