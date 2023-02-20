let contador = 1;
document.getElementById("radio1").checked = true;

setInterval( function(){
    ProximaImg();
}, 4000)

function ProximaImg(){
    contador++;
    if (contador>4){
        contador = 1;
    }


    document.getElementById("radio"+contador).checked = true;
}

