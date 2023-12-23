function add_auto() {
	container = document.getElementById('form-auto');

	html =
		"<br> <div class='row'> <div class='col-md'> <input type='text' name='auto' placeholder='Modelo' class='form-control rounded'> <input type='text' name='patente' placeholder='Patente' class='form-control rounded my-2' > </div> <button id='btn-eliminar' class='btn btn-danger my-auto mx-auto py-4'>Eliminar</button> </div>";

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

			id = document.getElementById('id');
			id.value = data['id_cliente'];

			nombre = document.getElementById('nombre');
			nombre.value = data['cliente']['nombre'];

			apellido = document.getElementById('apellido');
			apellido.value = data['cliente']['apellido'];

			email = document.getElementById('email');
			email.value = data['cliente']['email'];

			dni = document.getElementById('dni');
			dni.value = data['cliente']['dni'];

			autos_div = document.getElementById('autos');
			autos_div.innerHTML = ''; //. Limpiamos la pantalla de los autos al momento de cambiar a otro cliente.

			//. Prueba
			// console.log(data)

			//. Capturamos cada auto guardado en cada cliente
			for (i = 0; i < data['autos'].length; i++) {
				console.log(data['autos'][i]['fields']['auto']);

				autos_div.innerHTML += `<div>\
					<form action= '/clientes/update_auto/${data['autos'][i]['id']}' method='POST'>\
						<div class='row'>\
							<div class='col-md'>\
								<p class='pt-2'>Vehiculo</p>\
								<input class='form-control' type='text' name='auto' value='${data['autos'][i]['fields']['auto']}'>\
						</div>\
						<div class='col-md'>\
								<p class='pt-2'>Patente</p>\
								<input class='form-control' type='text' name='patente' value='${data['autos'][i]['fields']['patente']}'>\
						</div>\
						<input class='btn btn-success mt-5' type='submit' value='Guardar')>\
					</form>\
					<div class='col-md-3'>\
						<a class='btn btn-danger mt-5' href='/clientes/eliminar_auto/${data['autos'][i]['id']}'>Eliminar</a>\
					</div>\
				</div>`;
			}
		})
		.catch(function (error) {
			console.error('Error en la solicitud', error);
		});
}

// todo  Agregar logica de eliminar un auto

function update_cliente() {
	id = document.getElementById('id').value;
	nombre = document.getElementById('nombre').value;
	apellido = document.getElementById('apellido').value;
	email = document.getElementById('email').value;
	dni = document.getElementById('dni').value;

	fetch('/clientes/update_cliente/' + id, {
		method: 'POST',
		headers: {
			'X-CSRFToken': csrf_token,
		},
		body: JSON.stringify({
			nombre: nombre,
			apellido: apellido,
			email: email,
			dni: dni,
		}),
	})
		.then(function (result) {
			return result.json();
		})
		.then(function (data) {
			//. Prueba ver datos
			console.log(data);

			if (data['status'] == '200') {
				nombre = data['nombre'];
				apellido = data['apellido'];
				email = data['apellido'];
				dni = data['dni'];

				console.log('Datos modificados con suceso!');
			} else {
				console.log('Error!');
			}
		});
}
