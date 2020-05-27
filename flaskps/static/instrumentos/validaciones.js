function campoVacio(campo){
  if (campo.length == 0){
    return true;
  }
  return false;
}

function validarRegistrarInstrumento() {
	var nombre= document.getElementById("nombre").value;
	var codigo= document.getElementById("descripcionDeEstado").value; 
	
	if(!validarNombre(nombre))
    	return false;

    if(!validarCodigo(codigo))
    	return false;

  	return true;
}

function validarNombre(nombre){
  
  if (campoVacio(nombre)){
    document.getElementById("error-nombre-empty").style.display = "block";
    $('#error-nombre-empty').delay(4000).fadeOut(400)
    return false;
  }
  return true
}

function validarCodigo(codigo){
  
  if (campoVacio(codigo)){
    document.getElementById("error-codigo-empty").style.display = "block";
    $('#error-codigo-empty').delay(4000).fadeOut(400)
    return false;
  }
  return true
}