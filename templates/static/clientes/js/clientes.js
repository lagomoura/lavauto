function add_auto() {
	container = document.getElementById('form-auto');

	html =
		"<br> <div class='row'> <div class='col-md'> <input type='text' name='auto' placeholder='Modelo' class='form-control rounded'> <input type='text' name='patente' placeholder='Patente' class='form-control rounded my-2' > </div> <button id='btn-eliminar' class='btn btn-danger my-auto mx-auto py-4' onclick='eliminar_auto()'>Eliminar</button> </div>";

	container.innerHTML += html;
}

//todo  Agregar logica de eliminar un auto
