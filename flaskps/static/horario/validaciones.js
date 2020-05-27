function campoVacio(campo){
  if (campo.length == 0){
    return true;
  }
  return false;
}

function validarHorario(){
	var hora_ini = document.getElementById("hora_ini").value;
	var hora_fin = document.getElementById("hora_fin").value;

	if (!validarHoraIni(hora_ini,hora_fin))
		return false;
	if (!validarHoraFin(hora_fin, hora_ini))
		return false;

	return true;
}

function validarHoraIni(horaIni, horaFin){
  if (campoVacio(horaIni)){
    document.getElementById("error-hora_inicial-empty").style.display = "block";
    $('#error-hora_inicial-empty').delay(4000).fadeOut(400)
    return false;
  }
  if (!validarHoraMenorAFinal(horaIni,horaFin)) {
    document.getElementById("error-hora_inicial-mayor").style.display = "block";
    $('#error-hora_inicial-mayor').delay(4000).fadeOut(400)
    return false;
  }
  return true;
}

function validarHoraMenorAFinal(horaIni, horaFin){
	var ini = obtenerMinutos(horaIni)
	var fin = obtenerMinutos (horaFin)
	if (ini > fin)
		return false;
	return true;
}

function validarHoraFin(horaFin, horaIni){
  if (campoVacio(horaFin)){
    document.getElementById("error-hora_final-empty").style.display = "block";
    $('#error-hora_final-empty').delay(4000).fadeOut(400)
    return false;
  }

  return true;
}

function obtenerMinutos(hora){
	var spl = hora.split(":");
	return parseInt(spl[0])*60+parseInt(spl[1]);
}