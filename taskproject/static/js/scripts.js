
console.log('OK!')



function MessagesCarga(){

    let confirmation = confirm('[Alerta!] - Deseja Realmente Carregar Planilhas?');
    let id_href = document.getElementById('call-pl')
    console.log(id_href)


    if (confirmation == true){
        alert("Atualização de carga será realizada.");
        setTimeout(function() {
        
            window.location.href = `http://127.0.0.1:8000/CreatePL/?xxxxxx`
        }, 1000);

    }

    else{
        alert("Ok, as planilhas não serão caerregadas.");
    }

}




function MessagesCotation(){

    let confirmation = confirm('[Alerta!] - Deseja Realmente Carregar Cotação');
    let id_href = document.getElementsByTagName('radio')
    console.log(id_href)
    alert("-------", id_href);


    if (confirmation == true){
        alert("Atualização de carga será realizada.");
        setTimeout(function() {
        
            window.location.href = `http://127.0.0.1:8000/CreateCota/`
        }, 1000);

    }

    else{
        alert("Ok, A planilhas não serão caerregada.");
    }

}

document.getElementById('cota_show').style.display = 'none';

function Mudarestado(el) {
    
    let display = document.getElementById(el).style.display;

    if(display == "none")
        document.getElementById(el).style.display = 'block';
    else
        document.getElementById(el).style.display = 'none';
}


