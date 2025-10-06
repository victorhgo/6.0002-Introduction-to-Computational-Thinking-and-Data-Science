import time

def car_simulation():
    """
    Using the formula distance = velocity * time to simulate how much distance
    a car will move given the velocity and the time running.
    """
    # Get user input
    try:
        velocity = float(input("Enter the velocity of the car (in m/s): "))
        timeTravel = float(input("Enter the time traveled (in seconds): "))
    except ValueError:
        print("Please enter valid numbers!")
        return

    # Distance formula: d = v * t
    distance = velocity * timeTravel

    print("\nStarting simulation...\n")
    distance = 0.0
    step_time = 1  # seconds

    for t in range(1, int(timeTravel) + 1):
        distance = velocity * t
        print(f"Time: {t:2d}s | Distance covered: {distance:.2f} m")
        time.sleep(0.3)  # slow down the simulation

    print(f"Total (approximated) distance covered: {distance:.2f} meters\n")

if __name__ == "__main__":
    print("Car's movement simulation:\n")
    car_simulation()
