function validar() {
	const table = document.getElementById('table') 
	const id = document.getElementById('id').value
	const type = document.getElementById('type').value
  const observations = document.getElementById('observations').value

	if(!id){
	   alert('El ID es un campo obligatorio.')
  	 return false
  }

  if(idExistente()){
    alert('El ID ya existe.')
    return false
  }

  if(validarSiNumero(document.getElementById('id').value)){
    alert('el id debe ser un numero')
    return false
  }

  if(observations.length > 255){
		  alert('La observacion no debe tener mas de 255 caracteres')
      return false
  }

  var fila="<tr><td name='id_tabla'>"+id+"</td><td>"+type+"</td><td>"+observations+"</td></tr>";

  var btn = document.createElement("tr");
  btn.innerHTML=fila;
  document.getElementById("table").appendChild(btn);
  return false
}

function idExistente(){
   max = document.getElementsByName('id_tabla').length
   id = document.getElementById('id').value
   if (max > 0) {
   console.log(max)
    for (var i = 0; i < max; i++) {
      j = document.getElementsByName('id_tabla')[i].innerText
      console.log(id)
      if (j == id) {
        return true
      }
    }
   }
   return false
}

function validarSiNumero(numero){
    if (!/^([0-9])*$/.test(numero))
      return true
  }


