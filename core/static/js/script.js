const contenedor = document.querySelector('.slider-contenedor');
const slides = document.querySelectorAll('.slide');

function moverSlider() {
    // Si no existe el slider en esta página, no hacemos nada
    if (!contenedor) return;

    // Obtenemos el ancho de una diapositiva
    const ancho = contenedor.clientWidth;
    
    // Calculamos en qué slide estamos actualmente
    let slideActual = Math.round(contenedor.scrollLeft / ancho);
    
    // Calculamos el siguiente
    let siguiente = slideActual + 1;
    
    // Si llegamos al final, volvemos al primero
    if (siguiente >= slides.length) {
        siguiente = 0;
    }
    
    // Movemos el scroll suavemente
    contenedor.scrollTo({
        left: siguiente * ancho,
        behavior: 'smooth'
    });
}

// Ejecutar cada 5 segundos (5000 milisegundos)
setInterval(moverSlider, 5000);