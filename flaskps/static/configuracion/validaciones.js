function campoVacio(campo){
  if (campo.length == 0){
    return true;
  }
  return false;
}

function validar(){

  var titulo = document.getElementById("titulo").value;
  var descripcion = document.getElementById("descripcion").value;
  var email = document.getElementById("email").value;
  var paginacion = document.getElementById("paginacion").value;

  var expr_num = new RegExp('^[0-9]+');

  if (campoVacio(titulo)){
    document.getElementById("error-titulo").style.display = "block";
    $('#error-titlo').delay(4000).fadeOut(400)
    return false;
  }

  if (campoVacio(descripcion)){
    document.getElementById("error-descripcion").style.display = "block";
    $('#error-descripcion').delay(4000).fadeOut(400)
    return false;
  }

  if (campoVacio(email)){
    document.getElementById("error-email").style.display = "block";
    $('#error-email').delay(4000).fadeOut(400)
    return false;
  }

  if (campoVacio(paginacion)){
    document.getElementById("error-paginacion").style.display = "block";
    $('#error-paginacion').delay(4000).fadeOut(400)
    return false;
  }

  if (!expr_num.test(paginacion)){
    document.getElementById("error-paginacion-only-numbers").style.display = "block";
    $('#error-paginacion-only-numbers').delay(4000).fadeOut(400)
    return false;
  }



  return true;
}
