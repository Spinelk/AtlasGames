function agregarAlCarrito(nombre, foto, precio, slug) {
    console.log("TEST")

    // Crear un objeto que representa el producto
    var producto = {
        nombre: nombre,
        foto: foto,
        precio: precio,
        slug: slug,
    };

    // Verificar si ya existe un carrito en localStorage
    var carrito = localStorage.getItem("carrito");
    if (!carrito) {
        carrito = [];
    } else {
        carrito = JSON.parse(carrito);
    }

    // Verificar si el producto ya está en el carrito
    var productoExistente = carrito.find(function (item) {
        return item.slug === slug;
    });
    if (productoExistente) {
        alert("Este producto ya ha sido agregado al carrito.");
        return;
    }

    // Agregar el producto al carrito
    carrito.push(producto);

    // Guardar los datos actualizados del carrito en localStorage
    localStorage.setItem("carrito", JSON.stringify(carrito));

    // Fuerza una actualización del carrito
    mostrarProductosEnCarrito();
}


function mostrarProductosEnCarrito() {
    // Obtener el contenedor donde se mostrarán los productos
    var carritoProductos = $("#carritoProductos")[0]; // jQuery


    // Limpiar el contenido actual del contenedor
    carritoProductos.innerHTML = "";

    // Obtener los datos del carrito desde localStorage
    var carrito = localStorage.getItem("carrito");
    if (!carrito) {
        carrito = [];
    } else {
        carrito = JSON.parse(carrito);
    }

    // Generar el contenido HTML para cada producto en el carrito
    carrito.forEach(function (producto) {
        // Generar el elemento HTML para mostrar el producto
        var productoHTML = document.createElement("div");
        productoHTML.classList.add("producto-carrito");

        productoHTML.innerHTML = `
        <div class="card mb-3 bg-moradoClaro text-white border-0" style="max-width: 540px;">
            <div class="row g-0">
                <div class="col-md-3">
                    <img src="${producto.foto}" class="img-fluid rounded-start" alt="${producto.nombre}">
                    </div>
                <div class="col-md-7">
                    <div class="card-body">
                        <h5 class="card-title fw-bold fs-4">${producto.nombre}</h5>
                        <p class="card-text fw-semibold fs-4"><small class="text-body-secondary text-verdeBrillante">$${producto.precio}</small></p>
                    </div>
                </div>
                <div class="col-md-2">
                    <button type="button" class="btn btn-danger" onclick="eliminarDelCarrito('${producto.slug}')">
                        <svg xmlns="http://www.w3.org/2000/svg"
                        width="25" height="25" fill="currentColor"
                        class="bi bi-x" viewBox="0 0 16 16">
                        <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
        `;

        // Agregar el elemento del producto al contenedor
        carritoProductos.appendChild(productoHTML);
    });
}

function eliminarDelCarrito(slug) {
    // Obtener el carrito actual desde localStorage
    var carrito = localStorage.getItem("carrito");
    if (!carrito) {
        return; // No hay productos en el carrito
    }

    // Parsear el carrito a un array
    carrito = JSON.parse(carrito);

    // Buscar el índice del producto a eliminar
    var indice = -1;
    for (var i = 0; i < carrito.length; i++) {
        if (carrito[i].slug === slug) {
            indice = i;
            break;
        }
    }

    // Si se encontró el producto, eliminarlo del carrito
    if (indice !== -1) {
        carrito.splice(indice, 1);

        // Guardar el carrito actualizado en localStorage
        localStorage.setItem("carrito", JSON.stringify(carrito));

        // Actualizar la interfaz de usuario (opcional)
        mostrarProductosEnCarrito();
    }
}

document.addEventListener("DOMContentLoaded", mostrarProductosEnCarrito);


function obtenerCarritoDesdeLocalStorage() {
    var carrito = localStorage.getItem("carrito");
    if (carrito) {
        return JSON.parse(carrito);
    }
    return [];
}

function compraExitosa() {
    alert("Compra realizada con exito.");
    return;
}

function compraFallida() {
    alert("Error al realizar la compra");
    return;
}

function enviarCarrito() {
    var carrito = obtenerCarritoDesdeLocalStorage();

    // Enviar los datos del carrito al servidor mediante una solicitud AJAX
    $.ajax({
        type: "POST",
        url: "/guardar_carrito_en_servidor/", // URL de la vista en Django para guardar el carrito en el servidor
        data: { carrito: JSON.stringify(carrito) },
        success: function (response) {
            // Manejar la respuesta del servidor si es necesario
            localStorage.clear();
            mostrarProductosEnCarrito();
            compraExitosa();
        },
        error: function() {
            // Manejar el error de la solicitud AJAX
            compraFallida();
        }
    });
}
