import random
from time import sleep
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


def map_acceleration_to_string(acceleration_value):
    """
    Mapuje wartość przyspieszenia na odpowiednią akcję (napis).

    Parametry:
    - acceleration_value (float): Wartość przyspieszenia w przedziale -50 do 50.

    Zwraca:
    - string: Akcja odpowiadająca danej wartości przyspieszenia.
        - "Harsh Decelerate" dla przyspieszenia ≤ -25.
        - "Decelerate" dla przyspieszenia w zakresie (-25, 0).
        - "Maintain" dla przyspieszenia w zakresie (0, 10).
        - "Accelerate" dla przyspieszenia w zakresie (10, 50).
        - "Harsh Accelerate" dla przyspieszenia > 50.
    """
    if acceleration_value <= -25:
        return "Harsh Decelerate"
    elif acceleration_value <= 0:
        return "Decelerate"
    elif acceleration_value <= 10:
        return "Maintain"
    elif acceleration_value <= 50:
        return "Accelerate"
    else:
        return "Harsh Accelerate"


# Definiowanie zakresów
"""
Zakresy wejściowe i wyjściowe dla systemu sterowania fuzzy:
- speed: prędkość pojazdu w km/h (0 - 150 km/h)
- distance: odległość od pojazdu z przodu w metrach (0 - 200 m)
- weather: warunki pogodowe (0 - 100) gdzie 0 oznacza suche, a 100 bardzo śliskie warunki
- acceleration: zmiana prędkości pojazdu (-50 do 50) oznaczająca przyspieszenie lub hamowanie
"""

# Tworzenie zmiennych wejściowych i wyjściowych
speed = ctrl.Antecedent(np.arange(0, 151, 1), 'speed')
distance = ctrl.Antecedent(np.arange(0, 201, 1), 'distance')
weather = ctrl.Antecedent(np.arange(0, 101, 1), 'weather')
acceleration = ctrl.Consequent(np.arange(-50, 51, 1), 'acceleration')

# Definiowanie funkcji przynależności dla zmiennych wejściowych i wyjściowych
speed['low'] = fuzz.trimf(speed.universe, [0, 0, 60])
speed['medium'] = fuzz.trimf(speed.universe, [40, 90, 140])
speed['high'] = fuzz.trimf(speed.universe, [100, 150, 150])

distance['very_close'] = fuzz.trimf(distance.universe, [0, 0, 50])
distance['close'] = fuzz.trimf(distance.universe, [25, 75, 125])
distance['far'] = fuzz.trimf(distance.universe, [100, 150, 200])
distance['very_far'] = fuzz.trimf(distance.universe, [150, 200, 200])

weather['dry'] = fuzz.trimf(weather.universe, [0, 0, 50])
weather['wet'] = fuzz.trimf(weather.universe, [30, 50, 70])
weather['foggy'] = fuzz.trimf(weather.universe, [40, 70, 100])
weather['slippery'] = fuzz.trimf(weather.universe, [60, 100, 100])

acceleration['harsh_decelerate'] = fuzz.trimf(acceleration.universe, [-50, -50, -25])
acceleration['decelerate'] = fuzz.trimf(acceleration.universe, [-50, -25, 0])
acceleration['maintain'] = fuzz.trimf(acceleration.universe, [-10, 0, 10])
acceleration['accelerate'] = fuzz.trimf(acceleration.universe, [0, 25, 50])
acceleration['harsh_accelerate'] = fuzz.trimf(acceleration.universe, [25, 50, 50])

# Definiowanie reguł sterowania fuzzy
rules = [
    # Reguły dotyczące deceleracji, utrzymania prędkości i przyspieszania
    ctrl.Rule(speed['high'] & distance['close'] & (weather['slippery'] | weather['foggy']),
              acceleration['harsh_decelerate']),
    ctrl.Rule(speed['high'] & distance['very_close'] & weather['dry'], acceleration['harsh_decelerate']),
    ctrl.Rule(speed['low'] & distance['very_close'] & weather['slippery'], acceleration['harsh_decelerate']),
    ctrl.Rule(speed['medium'] & distance['very_close'] & weather['wet'], acceleration['harsh_decelerate']),

    # Deceleration
    ctrl.Rule(speed['high'] & distance['close'] & (weather['wet'] | weather['dry']), acceleration['decelerate']),
    ctrl.Rule(speed['medium'] & distance['close'] & (weather['wet'] | weather['foggy']), acceleration['decelerate']),
    ctrl.Rule(speed['high'] & distance['far'] & weather['foggy'], acceleration['decelerate']),
    ctrl.Rule(speed['medium'] & distance['close'] & weather['dry'], acceleration['decelerate']),

    # Maintain Speed
    ctrl.Rule(speed['medium'] & distance['close'] & weather['dry'], acceleration['maintain']),
    ctrl.Rule(speed['low'] & distance['close'] & weather['dry'], acceleration['maintain']),
    ctrl.Rule(speed['medium'] & distance['far'] & (weather['wet'] | weather['slippery']), acceleration['maintain']),
    ctrl.Rule(speed['high'] & distance['very_far'] & weather['dry'], acceleration['maintain']),
    ctrl.Rule(speed['low'] & distance['far'] & weather['slippery'], acceleration['maintain']),
    ctrl.Rule(speed['medium'] & distance['far'] & weather['slippery'], acceleration['maintain']),

    # Accelerate
    ctrl.Rule(speed['low'] & distance['far'] & weather['dry'], acceleration['harsh_accelerate']),
    ctrl.Rule(speed['medium'] & distance['very_far'] & weather['wet'], acceleration['accelerate']),
    ctrl.Rule(speed['high'] & distance['far'] & weather['dry'], acceleration['accelerate']),
    ctrl.Rule(speed['low'] & distance['very_far'] & weather['slippery'], acceleration['accelerate']),

    # Harsh Accelerate
    ctrl.Rule(speed['low'] & distance['far'] & weather['dry'], acceleration['harsh_accelerate']),
    ctrl.Rule(speed['low'] & distance['very_far'] & weather['wet'], acceleration['harsh_accelerate']),
    ctrl.Rule(speed['medium'] & distance['very_far'] & weather['dry'], acceleration['harsh_accelerate']),
    ctrl.Rule(speed['low'] & distance['very_far'] & weather['wet'], acceleration['harsh_accelerate'])
]

def runSimulation(sos):
    """
    Uruchamia symulację sterowania przyspieszeniem pojazdu na podstawie danych wejściowych (prędkość, odległość, pogoda).

    Parametry:
    - sos (int): Czas trwania symulacji w sekundach.

    Działanie:
    - Generuje losowe dane wejściowe (prędkość, odległość, pogoda).
    - Oblicza przyspieszenie w oparciu o reguły systemu fuzzy.
    - Drukuje wyniki symulacji w każdej sekundzie.
    """
    control_system = ctrl.ControlSystem(rules)
    controller = ctrl.ControlSystemSimulation(control_system)

    # Inicjalizacja zmiennych (prędkość, odległość, pogoda)
    spd = random.randrange(0, 151, 1)
    dis = random.randrange(0, 201, 1)
    wthr = random.randrange(0, 101, 1)

    for seconds in range(sos):
        spd += random.randint(-5, 5)
        dis += random.randint(-5, 5)
        wthr += random.randint(-5, 5)

        spd = max(0, min(spd, 150))
        dis = max(0, min(dis, 200))
        wthr = max(0, min(wthr, 100))

        controller.input['speed'] = spd
        controller.input['distance'] = dis
        controller.input['weather'] = wthr

        try:
            controller.compute()
            acceleration_value = controller.output['acceleration']
            acceleration_str = map_acceleration_to_string(acceleration_value)

            print(f"Second: {seconds + 1} | Acceleration: {acceleration_str} (Value: {acceleration_value})")
            print(f"Input - Speed: {spd}, Distance: {dis}, Weather: {wthr}")
        except KeyError as ke:
            print(f"KeyError: {ke}")
            print(f"Input values: Speed: {spd}, Distance: {dis}, Weather: {wthr}")
        except Exception as e:
            print(f"Error: {e}")
            print(f"Input values: Speed: {spd}, Distance: {dis}, Weather: {wthr}")
        sleep(1)


if __name__ == '__main__':
    # Symulacja na 30 sekund
    runSimulation(30)
