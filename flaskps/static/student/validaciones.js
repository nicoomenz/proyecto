function campoVacio(campo){
  if (campo.length == 0){
    return true;
  }
  return false;
}

function validarFechaMenorActual(date){

  var hoy = new Date();
  var dd = hoy.getDate();
  var mm = hoy.getMonth()+1;
  var yyyy = hoy.getFullYear();
  hoy = yyyy+'-'+mm+'-'+dd;

  if (date <= hoy){
    return true;
  }
  return false;   
}

function validarRegistrarEstudiante(){
  var nombreO = document.getElementById("first_name").value;
  var apellidoO = document.getElementById("last_name").value;
  var fecha_nacO = document.getElementById("fecha_nac").value;
  var numero_docO = document.getElementById("numero_doc").value;
  var domicilioO = document.getElementById("domicilio").value;
  var barrioO = document.getElementById("barrio").value;
  var escuelaO = document.getElementById("escuela").value;
  
  var expr_texto = new RegExp('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$');
  var expr_num = new RegExp('^[0-9]+');
  var expr_email = new RegExp('^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,4})+$');
  var expr_pass = new RegExp('^(?!^[0-9]*$)(?!^[a-zA-Z]*$)^([a-zA-Z0-9]{8,10})$');

  if(!validarNombre(nombreO))
    return false;
  if(!validarApellido(apellidoO))
    return false;
  if(!validarFecha_nac(fecha_nacO))
    return false;
  if(!validarNumero_doc(numero_docO))
    return false;
  if(!validarDomicilio(domicilioO))
    return false;
  if(!validarBarrio(barrioO))
    return false;
  if(!validarEscuela(escuelaO))
    return false;

  return true;
}

function validarNombre(nombre){
  var expr_texto = new RegExp('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$');
  if (campoVacio(nombre)){
    document.getElementById("error-first_name-empty").style.display = "block";
    $('#error-first_name-empty').delay(4000).fadeOut(400)
    return false;
  }

  if (!expr_texto.test(nombre)){
    document.getElementById("error-first_name-only-letters").style.display = "block";
    $('#error-first_name-only-letters').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function validarApellido(apellido){
  var expr_texto = new RegExp('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$');
  if (campoVacio(apellido)){
    document.getElementById("error-last_name-empty").style.display = "block";
    $('#error-last_name-empty').delay(4000).fadeOut(400)
    return false;
  }

  if (!expr_texto.test(apellido)){
    document.getElementById("error-last_name-only-letters").style.display = "block";
    $('#error-last_name-only-letters').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function validarFecha_nac(fecha_nac){
  if (campoVacio(fecha_nac)) {
    document.getElementById("error-fecha_nac-empty").style.display = "block";
    $('#error-fecha_nac-empty').delay(4000).fadeOut(400)
     return false;
  }
  if (!validarFechaMenorActual(fecha_nac)) {
    document.getElementById("error-fecha_nac-condicion").style.display = "block";
    $('#error-fecha_nac-condicion').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function validarNumero_doc(numero_doc){
  if (campoVacio(numero_doc)) {
    document.getElementById("error-numero_doc-empty").style.display = "block";
    $('#error-numero_doc-empty').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function validarDomicilio(domicilio){
  if (campoVacio(domicilio)) {
    document.getElementById("error-domicilio-empty").style.display = "block";
    $('#error-domicilio-empty').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function validarTelefono(telefono){
  var expr_num = new RegExp('^[0-9]+');
  if (!expr_num.test(telefono)){
    document.getElementById("error-telefono-only-numbers").style.display = "block";
    $('#error-telefono-only-numbers').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function validarBarrio(barrioO){
  if (campoVacio(barrioO)) {
    document.getElementById("error-barrio-empty").style.display = "block";
    $('#error-barrio-empty').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function validarEscuela(escuelaO){
  if (campoVacio(escuelaO)) {
    document.getElementById("error-escuela-empty").style.display = "block";
    $('#error-escuela-empty').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}