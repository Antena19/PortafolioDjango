//Función que oculta o muestra el menu
function mostrarOcultarMenu() {
    var navResponsive = document.getElementById("nav");
    if (navResponsive.classList.contains("responsive")) {
        navResponsive.classList.remove("responsive");
    } else {
        navResponsive.classList.add("responsive");
    }
}
function seleccionar(){
    //oculto el menu una vez que selecciono una opcion
    document.getElementById("nav").classList = "";
    menuVisible = false;
}

// Función para abrir el modal
function openModal(id) {
    // Obtiene el modal por su ID
    var modal = document.getElementById(id);
    // Muestra el modal
    modal.style.display = "block";
}

// Función para cerrar el modal
function closeModal(id) {
    // Obtiene el modal por su ID
    var modal = document.getElementById(id);
    // Oculta el modal
    modal.style.display = "none";
}

// Cierra el modal haciendo clic fuera del contenido
window.onclick = function(event) {
    // Si se hace clic fuera del modal, se cierra
    if (event.target.classList.contains('modal')) {
        event.target.style.display = "none";
    }
}


// Función para validar el formulario JQUERY
document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    var forms = document.querySelectorAll('.needs-validation');

    Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }

            form.classList.add('was-validated');
            
            // Añadir clases de validación a los campos de entrada
            Array.prototype.slice.call(form.elements).forEach(function(element) {
                if (element.checkValidity()) {
                    element.classList.remove('is-invalid');
                    element.classList.add('is-valid');
                } else {
                    element.classList.remove('is-valid');
                    element.classList.add('is-invalid');
                }
            });
        }, false);
    });
});






