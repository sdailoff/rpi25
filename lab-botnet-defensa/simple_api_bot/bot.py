import time
import random
from datetime import datetime

def tarea_principal():
    while True:
        ahora = datetime.now().strftime("%H:%M:%S")
        print(f"[{ahora}] ¡Soy un bot de X! Estoy vivo.")
        # Jitter aleatorio entre 10 y 30 segundos
        time.sleep(random.randint(10, 30))

if __name__ == "_main_":
    tarea_principal()