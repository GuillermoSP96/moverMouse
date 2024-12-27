import pyautogui
import keyboard
import math

# Obtener el tamaño de la pantalla
screen_width, screen_height = pyautogui.size()

# Calcular el centro de la pantalla
center_x = screen_width // 2
center_y = screen_height // 2

# Definir el radio y la velocidad del movimiento
radius = 200
speed = 10

# Variable para rastrear el número de vueltas completas
completed_turns = 0

# Ángulo inicial
angle = 0

try:
    # Bucle hasta que se presione Ctrl + C
    while True:
        # Calcular la posición actual en el círculo
        x = center_x + int(math.cos(math.radians(angle)) * radius)
        y = center_y + int(math.sin(math.radians(angle)) * radius)
        # Mover el mouse a la posición actual
        pyautogui.moveTo(x, y)
        # Actualizar el ángulo para el siguiente paso del círculo
        angle += speed
        # Verificar si se ha completado una vuelta completa
        if angle >= 360:
            completed_turns += 1
            angle = 0
            # Realizar un clic al completar una vuelta
            # pyautogui.click()
        # Verificar si se ha presionado Ctrl + C para detener el proceso
        if keyboard.is_pressed('ctrl+c'):
            raise KeyboardInterrupt

except KeyboardInterrupt:
    print("Proceso detenido.")
