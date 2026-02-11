function notaTradicional(horas, asistencia, tareas) {

    // Examen estimado
    let examen = Math.min(20, 5 + (0.6 * horas));

    // Cálculo ponderado
    let nota = (0.4 * examen) +
               (0.3 * (tareas * 20 / 100)) +
               (0.3 * (asistencia * 20 / 100));

    // Limitar entre 0 y 20
    nota = Math.max(0, Math.min(20, nota));

    return nota;
}

function estadoAprobacion(nota) {
    return nota >= 11 ? "APRUEBA" : "DESAPRUEBA";
}

function calcularNota() {

    let horas = parseFloat(document.getElementById("horas").value);
    let asistencia = parseFloat(document.getElementById("asistencia").value);
    let tareas = parseFloat(document.getElementById("tareas").value);
    let resultado = document.getElementById("resultado");

    if (isNaN(horas) || isNaN(asistencia) || isNaN(tareas)) {
        resultado.innerHTML = "Ingrese todos los datos correctamente.";
        return;
    }

    if (horas < 0 || asistencia < 0 || asistencia > 100 || tareas < 0 || tareas > 100) {
        resultado.innerHTML = "Valores fuera de rango.";
        return;
    }

    let nota = notaTradicional(horas, asistencia, tareas);
    let estado = estadoAprobacion(nota);

    resultado.innerHTML = `
        Nota Final: ${nota.toFixed(2)} <br>
        Estado: ${estado}
    `;
}
