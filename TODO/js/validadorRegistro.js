function validarUsuario(params) { 
    var usuario = params.value;

    if (usuario.length > 0) {
      if (usuario.lenght > 2){
        $("#0").removeClass("text-danger").addClass("text-success");
        $("#usuario").removeClass("is-invalid").addClass("is-valid");
      }
      else {
        $("#0").removeClass("text-success").addClass("text-danger");
        $("#usuario").removeClass("is-valid").addClass("is-invalid");
      }
    }
}

function validarContraseña(params) {
    var contraseña1 = params.value;

    const regex_az = new RegExp("[a-z]");
    const regex_AZ = new RegExp("[A-Z]");
    const regex_num = new RegExp("[0-9]");

    if (contraseña1.length > 0) {
        // 1) Al menos una letra
        if (contraseña1.match(regex_az)) {
            $("#1").removeClass("text-danger").addClass("text-success");
            $("#contraseña-1").removeClass("is-invalid").addClass("is-valid");
        } else {
            $("#1").removeClass("text-success").addClass("text-danger");
            $("#contraseña-1").removeClass("is-valid").addClass("is-invalid");
        }

        // 2) Al menos una letra mayuscula
        if (contraseña1.match(regex_AZ)) {
            $("#2").removeClass("text-danger").addClass("text-success");
            $("#contraseña-1").removeClass("is-invalid").addClass("is-valid");
        } else {
            $("#2").removeClass("text-success").addClass("text-danger");
            $("#contraseña-1").removeClass("is-valid").addClass("is-invalid");
        }

        // 3) Al menos un nùmero
        if (contraseña1.match(regex_num)) {
            $("#3").removeClass("text-danger").addClass("text-success");
            $("#contraseña-1").removeClass("is-invalid").addClass("is-valid");
        } else {
            $("#3").removeClass("text-success").addClass("text-danger");
            $("#contraseña-1").removeClass("is-valid").addClass("is-invalid");
        }

        // 4) Al menos 10 caracteres
        if (contraseña1.length >= 10) {
            $("#4").removeClass("text-danger").addClass("text-success");
            $("#contraseña-1").removeClass("is-invalid").addClass("is-valid");
        } else {
            $("#4").removeClass("text-success").addClass("text-danger");
            $("#contraseña-1").removeClass("is-valid").addClass("is-invalid");
        }
    }
}

function validarContraseña2(params) {
    var contraseña1 = document.getElementById("contraseña-1").value;
    var contraseña2 = params.value;

    if (contraseña2.length > 0) {
        // 5) Las contraseñas deben coincidir
        if (contraseña1 == contraseña2) {
            $("#5").removeClass("text-danger").addClass("text-success");
            $("#contraseña-2").removeClass("is-invalid").addClass("is-valid");
        } else {
            $("#5").removeClass("text-success").addClass("text-danger");
            $("#contraseña-2").removeClass("is-valid").addClass("is-invalid");
        }
    } else {
        $("#contraseña-2").removeClass("is-invalid").removeClass("is-valid");
    }
}
