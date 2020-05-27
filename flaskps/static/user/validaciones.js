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

function validarRegistrar(){
  var nombre = document.getElementById("first_name").value;
  var apellido = document.getElementById("last_name").value;
  var fecha_nac = document.getElementById("fecha_nac").value;
  var tipo_doc = document.getElementById("tipo_doc").value;
  var numero_doc = document.getElementById("numero_doc").value;
  var domicilio = document.getElementById("domicilio").value;
  var telefono = document.getElementById("telefono").value;
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;
  var rol = document.getElementById("rol").value;

  var expr_texto = new RegExp('^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$');
  var expr_num = new RegExp('^[0-9]+');
  var expr_pass = new RegExp('^(?!^[0-9]*$)(?!^[a-zA-Z]*$)^([a-zA-Z0-9]{8,10})$');

  if(!validarNombre(nombre))
    return false;
  if(!validarApellido(apellido))
    return false;
  if(!validarFecha_nac(fecha_nac))
    return false;
  if(!validarNumero_doc(numero_doc))
    return false;
  if(!validarDomicilio(domicilio))
    return false;
  if(!validarTelefono(telefono))
    return false;
  if(!validarEmail(email))
    return false;
  if(!validarPassword(password))
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

function validarLocalidad(localidad){
  if (campoVacio(localidad)) {
    document.getElementById("error-localidad-empty").style.display = "block";
    $('#error-localidad-empty').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function validarTelefono(telefono){
  var expr_num = new RegExp('^[0-9]+');
  if (campoVacio(telefono)) {
    document.getElementById("error-telefono-empty").style.display = "block";
    $('#error-telefono-empty').delay(4000).fadeOut(400)
    return false;
  }

  if (!expr_num.test(telefono)){
    document.getElementById("error-telefono-only-numbers").style.display = "block";
    $('#error-telefono-only-numbers').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function validarEmail(email){
  var expr_email = new RegExp('^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,4})+$');
  if (campoVacio(email)){

    document.getElementById("error-email-empty").style.display = "block";
    $('#error-email-empty').delay(4000).fadeOut(400)
    return false;
  }

  if (!expr_email.test(email)){
    document.getElementById("error-email-condition").style.display = "block";
    $('#error-email-condition').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function validarPassword(password){
  var expr_pass = new RegExp('^(?!^[0-9]*$)(?!^[a-zA-Z]*$)^([a-zA-Z0-9]{8,10})$');
  if (campoVacio(password)){
    document.getElementById("error-password-empty").style.display = "block";
    $('#error-password-empty').delay(4000).fadeOut(400)
    return false;
  }

  if (!expr_pass.test(password)){
    document.getElementById("error-password-condition").style.display = "block";
    $('#error-password-condition').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function valoresPredeterminadosModificar(){
   document.ready = document.getElementById("tipo_doc").value = document.getElementById('tipoDocOculto').value;
}