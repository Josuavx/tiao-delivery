$(document).ready(function(){

    $('.redirect-btn').click(function(){
        $.ajax({
            url: 'http://127.0.0.1:5000/',
            type: 'get',
            contentType: 'application/json',
            data: {
                button: $(this).text()
            },
            success: function(response){
                alert(response);
                location.replace(response);
            }
        })
    })
})
