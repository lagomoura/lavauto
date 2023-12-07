function add_auto() {
	container = document.getElementById('form-auto');

	html =
		"<br> <div class='row'> <div class='col-md'> <input type='text' name='auto' placeholder='Modelo' class='form-control rounded'> <input type='text' name='patente' placeholder='Patente' class='form-control rounded my-2' > </div> <button id='btn-eliminar' class='btn btn-danger my-auto mx-auto py-4' onclick='eliminar_auto()'>Eliminar</button> </div>";

	container.innerHTML += html;
}

function mostrar_form(tipo) {
	add_cliente = document.getElementById('agregar-cliente');
	att_cliente = document.getElementById('actualizar-cliente');

	if (tipo == '1') {
		att_cliente.style.display = 'none';
		add_cliente.style.display = 'block';
	} else if (tipo == '2') {
		att_cliente.style.display = 'block';
		add_cliente.style.display = 'none';
	}
}

function datos_cliente() {
	cliente = document.getElementById('cliente-select');

	fetch("/clientes/actualiza_cliente/", {
		methodo: "POST"
	})

}

//todo  Agregar logica de eliminar un auto
