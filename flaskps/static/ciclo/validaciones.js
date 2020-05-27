function campoVacio(campo){
  if (campo.length == 0){
    return true;
  }
  return false;
}

function validarFechaMayorActual(date){

  var hoy = new Date();
  var dd = hoy.getDate();
  var mm = hoy.getMonth()+1;
  var yyyy = hoy.getFullYear();
  hoy = yyyy+'-'+mm+'-'+dd;

  if (date >= hoy){
    return true;
  }
    return false;   
}

function validarFechaMayorAIncio(date,inicio){

  if (date >= inicio){
    return true;
  }
    return false;   
}

function validarCiclo() {
	var fechaIni = document.getElementById("fecha_ini").value;
	var fechaFin = document.getElementById("fecha_fin").value;
	var semestre = document.getElementById("semestre").value;

  if(!validarInicio(fechaIni))
    return false;
  if(!validarFin(fechaFin,fechaIni))
    return false;
  if(!validarSemestre(semestre))
    return false;

  return true;
}

function validarInicio(fechaIni){
  if (campoVacio(fechaIni)){
    document.getElementById("error-fecha_ini-empty").style.display = "block";
    $('#error-fecha_ini-empty').delay(4000).fadeOut(400)
    return false;
  }
  if (!validarFechaMayorActual(fechaIni)) {
    document.getElementById("error-fecha_ini-menorActual").style.display = "block";
    $('#error-fecha_ini-menorActual').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function validarFin(fechaFin,inicio){ 
  if (campoVacio(fechaFin)){
    document.getElementById("error-fecha_fin-empty").style.display = "block";
    $('#error-fecha_fin-empty').delay(4000).fadeOut(400)
    return false;
  }
  if (!validarFechaMayorAIncio(fechaFin,inicio)) {
    document.getElementById("error-fecha_fin-menorIni").style.display = "block";
    $('#error-fecha_fin-menorIni').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function validarSemestre(semestre){
  var expr_num = new RegExp('^[0-9]*');
  if (campoVacio(semestre)){
    document.getElementById("error-semestre-empty").style.display = "block";
    $('#error-semestre-empty').delay(4000).fadeOut(400)
    return false;
  }
  if(!expr_num.test(semestre)){
    document.getElementById("error-semestre-condicion").style.display = "block";
    $('#error-semestre-condicion').delay(4000).fadeOut(400)
    return false;    
  }
  return true;
}