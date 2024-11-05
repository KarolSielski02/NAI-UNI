import random
from time import sleep
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def map_acceleration_to_string(acceleration_value):
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
'''
	•	speed: Range from 0 to 150 km/h (increment by 1). This is the range of possible vehicle speeds.
	•	distance: Range from 0 to 200 m (increment by 1). Represents the distance to the vehicle in front.
	•	weather: Range from 0 to 100 (increment by 1). This may indicate weather conditions, such as dry, wet, or slippery, where 0 is very dry and 100 is extremely humid.
	•	acceleration: Range from -50 to 50 (increment by 1). This is the system’s output, defining the change in vehicle speed:
	 positive values indicate acceleration, and negative values indicate braking.
	 
	 it's set to value+1 because it never reaches the max value
'''

speed = ctrl.Antecedent(np.arange(0, 151, 1), 'speed')
distance = ctrl.Antecedent(np.arange(0, 201, 1), 'distance')
weather = ctrl.Antecedent(np.arange(0, 101, 1), 'weather')
acceleration = ctrl.Consequent(np.arange(-50, 51, 1), 'acceleration')

# Prędkość
speed['low'] = fuzz.trimf(speed.universe, [0, 0, 60])
speed['medium'] = fuzz.trimf(speed.universe, [40, 90, 140])
speed['high'] = fuzz.trimf(speed.universe, [100, 150, 150])

# Odległość
distance['very_close'] = fuzz.trimf(distance.universe, [0, 0, 50])
distance['close'] = fuzz.trimf(distance.universe, [25, 75, 125])
distance['far'] = fuzz.trimf(distance.universe, [100, 150, 200])
distance['very_far'] = fuzz.trimf(distance.universe, [150, 200, 200])

# Pogoda
weather['dry'] = fuzz.trimf(weather.universe, [0, 0, 50])
weather['wet'] = fuzz.trimf(weather.universe, [30, 50, 70])
weather['foggy'] = fuzz.trimf(weather.universe, [40, 70, 100])
weather['slippery'] = fuzz.trimf(weather.universe, [60, 100, 100])

# Wyjście
acceleration['harsh_decelerate'] = fuzz.trimf(acceleration.universe, [-50, -50, -25])
acceleration['decelerate'] = fuzz.trimf(acceleration.universe, [-50, -25, 0])
acceleration['maintain'] = fuzz.trimf(acceleration.universe, [-10, 0, 10])
acceleration['accelerate'] = fuzz.trimf(acceleration.universe, [0, 25, 50])
acceleration['harsh_accelerate'] = fuzz.trimf(acceleration.universe, [25, 50, 50])

rules = [
    # Harsh Deceleration
    ctrl.Rule(speed['high'] & distance['close'] & (weather['slippery'] | weather['foggy']), acceleration['harsh_decelerate']),
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
    # Build the control system
    control_system = ctrl.ControlSystem(rules)
    controller = ctrl.ControlSystemSimulation(control_system)

    # Initial values (set once)
    spd = random.randrange(0, 151, 1)    # Speed between 0 and 150
    dis = random.randrange(0, 201, 1)    # Distance between 0 and 200
    wthr = random.randrange(0, 101, 1)   # Weather between 0 and 100

    for seconds in range(sos):
        # Adjust values by a random number in the range of -5 to 5
        spd += random.randint(-5, 5)   # Add random number between -5 and 5
        dis += random.randint(-5, 5)   # Add random number between -5 and 5
        wthr += random.randint(-5, 5)  # Add random number between -5 and 5

        # Ensure the values stay within valid ranges
        spd = max(0, min(spd, 150))    # Speed should remain between 0 and 150
        dis = max(0, min(dis, 200))    # Distance should remain between 0 and 200
        wthr = max(0, min(wthr, 100))  # Weather should remain between 0 and 100

        # Set the adjusted input values for the controller
        controller.input['speed'] = spd
        controller.input['distance'] = dis
        controller.input['weather'] = wthr

        try:
            # Compute the output
            controller.compute()

            # Map the output to a string
            acceleration_value = controller.output['acceleration']
            acceleration_str = map_acceleration_to_string(acceleration_value)

            # Print the output as a string
            print(f"Second: {seconds + 1} | Acceleration: {acceleration_str} (Value: {acceleration_value})")
            print(f"Input - Speed: {spd}, Distance: {dis}, Weather: {wthr}")

        except KeyError as ke:
            # Handle KeyError if the output key is missing
            print(f"KeyError: {ke}")
            print(f"Input values: Speed: {spd}, Distance: {dis}, Weather: {wthr}")
        except Exception as e:
            # General exception handler to catch other unexpected errors
            print(f"Error: {e}")
            print(f"Input values: Speed: {spd}, Distance: {dis}, Weather: {wthr}")
        sleep(1)

if __name__ == '__main__':
    #the input is number of seconds the simulation is running for sos = seconds of simulation
    runSimulation(30)

