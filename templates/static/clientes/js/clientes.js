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
	//. Con eso capturamos el ID del cliente seleccionado
	cliente = document.getElementById('cliente-select');
	csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value; //. Aca si no pongo el ".value" me traz el objeto entero
	id_cliente = cliente.value;

	//! Prueba de captacion de la informacion
	// console.log(id_cliente);

	data = new FormData();
	data.append('id_cliente', id_cliente);

	//. Enviamos ese ID al backend
	//. Necesistamos envia el header con en token del input y el body con el id del cliente
	fetch('/clientes/actualiza_cliente/', {
		method: 'POST',
		headers: {
			'X-CSRFToken': csrf_token,
		},
		body: data,
	})
		.then(function (result) {
			if (!result.ok) {
				throw new Error('La solicitud no ha sido exitosa: ' + result.status);
			}
			return result.json();
		})
		.then(function (data) {
			document.querySelector('.info_cliente').style.display = 'block';

			nombre = document.getElementById('nombre');
			nombre.value = data['nombre'];

			apellido = document.getElementById('apellido');
			apellido.value = data['apellido'];

			email = document.getElementById('email');
			email.value = data['email'];

			dni = document.getElementById('dni');
			dni.value = data['dni'];

		})
		.catch(function (error) {
			console.error('Error en la solicitud', error);
		});
}

// todo  Agregar logica de eliminar un auto
