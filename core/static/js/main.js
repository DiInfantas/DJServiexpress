function mostrarDatos(event) {
    event.preventDefault();

    var fecha = document.getElementById('fecha').value;
    var hora = document.getElementById('hora').value;
    var servicio = document.getElementById('servicio').value;

    
    alert(`Su reserva ha sido efectuada correctamente 🫡:\nFecha: ${fecha}\nHora: ${hora}\nServicio: ${servicio}`);
}

function msglogin(event) {
    event.preventDefault();
    var nombre = document.getElementById('nombre').value;

    alert(`Ha ingresado correctamente. \nBienvenido ${nombre}`);
}