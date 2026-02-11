# ============================================================
# SISTEMA TRADICIONAL - CÁLCULO DE NOTA FINAL
# Basado en fórmula matemática fija (no usa IA)
# ============================================================

import numpy as np

# ------------------------------------------------------------
# 1) Dataset de ejemplo
# X = [horas_estudio_semana, asistencia_pct, tareas_pct]
# y = nota real (solo para comparación si se desea)
# ------------------------------------------------------------

X = np.array([
    [2, 55, 40],
    [4, 60, 50],
    [5, 70, 65],
    [6, 75, 60],
    [8, 80, 70],
    [9, 85, 78],
    [10, 88, 82],
    [12, 90, 85],
    [14, 92, 88],
    [15, 95, 90]
], dtype=np.float32)


# ------------------------------------------------------------
# 2) Función del enfoque tradicional
# ------------------------------------------------------------

def nota_tradicional(horas: float, asistencia: float, tareas: float) -> float:
    # Examen estimado en base a horas
    examen_estimado = min(20.0, 5.0 + 0.6 * horas)

    # Cálculo ponderado
    nota = (
        0.4 * examen_estimado +
        0.3 * (tareas * 20.0 / 100.0) +
        0.3 * (asistencia * 20.0 / 100.0)
    )

    # Limitar entre 0 y 20
    return float(np.clip(nota, 0.0, 20.0))


def estado_aprobacion(nota: float) -> str:
    return "APRUEBA" if nota >= 11.0 else "DESAPRUEBA"


# ------------------------------------------------------------
# 3) Prueba con dataset
# ------------------------------------------------------------

print("========================================")
print("RESULTADOS SISTEMA TRADICIONAL")
print("========================================")

for i, (h, a, t) in enumerate(X):
    nota = nota_tradicional(h, a, t)
    estado = estado_aprobacion(nota)
    print(f"Alumno {i+1}: Nota = {nota:.2f} -> {estado}")


# ------------------------------------------------------------
# 4) Predicción manual por teclado
# ------------------------------------------------------------

print("\n========================================")
print("PREDICCIÓN MANUAL")
print("========================================")

while True:
    try:
        horas = float(input("\nHoras de estudio por semana: "))
        asistencia = float(input("Asistencia % (0-100): "))
        tareas = float(input("Tareas % (0-100): "))

        # Validaciones
        if horas < 0:
            print("Error: horas debe ser >= 0.")
            continue

        if not (0 <= asistencia <= 100):
            print("Error: asistencia debe estar entre 0 y 100.")
            continue

        if not (0 <= tareas <= 100):
            print("Error: tareas debe estar entre 0 y 100.")
            continue

        nota = nota_tradicional(horas, asistencia, tareas)
        estado = estado_aprobacion(nota)

        print("\n----- RESULTADO -----")
        print(f"Nota Final: {nota:.2f}")
        print(f"Estado: {estado}")

        seguir = input("\n¿Deseas ingresar otro alumno? (s/n): ").strip().lower()
        if seguir != "s":
            print("Fin del programa.")
            break

    except ValueError:
        print("Error: ingresa solo números.")

