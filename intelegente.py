
# ============================================================
# SISTEMA INTELIGENTE
# Red Neuronal con TensorFlow
# ============================================================

import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

np.random.seed(42)
tf.random.set_seed(42)

# -----------------------------
# Dataset
# -----------------------------
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
    [15, 95, 90],
    [3, 50, 45],
    [7, 72, 68],
    [11, 89, 84],
    [13, 91, 87],
    [16, 96, 92],
    [1, 45, 30],
    [18, 98, 95],
    [17, 97, 94],
    [6, 65, 58],
    [9, 78, 74],
], dtype=np.float32)

y = np.array([
    8.0, 9.2, 11.0, 11.3, 12.8, 13.9, 14.6, 15.4, 16.2, 17.0,
    8.5, 11.7, 15.0, 15.8, 17.8, 6.8, 18.6, 18.2, 10.7, 13.4
], dtype=np.float32)

# -----------------------------
# Split y escalado
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

x_scaler = MinMaxScaler()
y_scaler = MinMaxScaler()

X_train_s = x_scaler.fit_transform(X_train)
X_test_s = x_scaler.transform(X_test)

y_train_s = y_scaler.fit_transform(y_train.reshape(-1, 1))

# -----------------------------
# Modelo
# -----------------------------
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(3,)),
    tf.keras.layers.Dense(4, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mse')

# -----------------------------
# Entrenamiento
# -----------------------------
model.fit(X_train_s, y_train_s, epochs=500, verbose=0)

# -----------------------------
# Evaluación
# -----------------------------
y_pred_s = model.predict(X_test_s)
y_pred = y_scaler.inverse_transform(y_pred_s).flatten()

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("===================================")
print("SISTEMA INTELIGENTE (IA)")
print("===================================")
print(f"MAE: {mae:.3f}")
print(f"RMSE: {rmse:.3f}")

# -----------------------------
# Predicción manual
# -----------------------------
while True:
    try:
        horas = float(input("\nHoras de estudio: "))
        asistencia = float(input("Asistencia (%): "))
        tareas = float(input("Tareas (%): "))

        nuevo = np.array([[horas, asistencia, tareas]])
        nuevo_s = x_scaler.transform(nuevo)

        pred_s = model.predict(nuevo_s)
        pred = y_scaler.inverse_transform(pred_s)[0][0]

        estado = "APRUEBA" if pred >= 11 else "DESAPRUEBA"

        print(f"\nNota Predicha (IA): {pred:.2f}")
        print(f"Estado: {estado}")

        if input("¿Continuar? (s/n): ").lower() != "s":
            break

    except:
        print("Error en datos.")
