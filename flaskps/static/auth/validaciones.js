function campoVacio(campo){
  if (campo.length == 0){
    return true;
  }
  return false;
}

function validarIniciar(){

  var email = document.getElementById("email").value;
  var pass = document.getElementById("password").value;

  if (campoVacio(email)){
    document.getElementById("error-user").style.display = "block";
    $('#error-user').delay(4000).fadeOut(400)
    return false;
  }

  if (campoVacio(pass)){
    document.getElementById("error-pass").style.display = "block";
    $('#error-pass').delay(4000).fadeOut(400)
    return false;
  }

   return true;
}

