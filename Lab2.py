# Function 1: Calculate the height of the ball after time t
# This function should take the initial height h0 and time t as inputs, and return the height at time t.
# Round up to one decimal point
def calculate_height(h0, t):
    # TODO: Implement this function
    pass  # Replace with your code

# Function 2: Calculate the distance traveled by the car
# This function should take the time t as input and return the distance traveled by the car.
def calculate_car_distance(t):
    # TODO: Implement this function
    #pass  # Replace with your code
    def calculate_car_distance(time):
    speed = 20  # in meters/seconds
    distance = speed * time
    return distance
    time = float(input("Enter time for car (in seconds): "))
    distance = calculate_car_distance(time)
    print(“The car will travel”, distance, “meters in”, time, “seconds.")


