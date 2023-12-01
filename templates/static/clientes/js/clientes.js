function add_auto() {
	container = document.getElementById('form-auto');

	html =
		"<br> <div class='row'>  <div class='col-md'> <input type='text' placeholder='Modelo auto' class='form-control rounded p-2' name='auto'</div>  <input type='text' placeholder='Patente' class='form-control rounded p-2 my-2'><button id='btn-eliminar' class='btn btn-outline-danger' onclick='eliminar_auto()'>Eliminar</button></div>";

	container.innerHTML += html;

}

//! Agregar logica de eliminar un auto 