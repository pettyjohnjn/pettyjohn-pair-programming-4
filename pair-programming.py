import numpy as np

# Define a function to convert feet and inches to meters
def convert_to_meters(feet, inches):
    """
    This function converts feet and inches to meters.
    Parameters:
    feet (float): The length in feet.
    inches (float): The length in inches.
    Returns:
    float: The length in meters.
    Example:
    >>> convert_to_meters(5, 3)
    1.6002
    >>> convert_to_meters(np.array([5, 6]), np.array([3, 2]))
    array([1.6002, 1.8796])
    """
    # Comment: I have a good understanding of what this function does by just reading the documentation. It's good that you included parameters and what data types are accepted. It's good that you included what the function returns and what data type the return is. I also like that you included examples. One thing you could do is included in the description that your return is rounded, but that might not be necessary. ~Emily Pearson

    # Assert that feet is an integer, a float, or a numpy array
    assert isinstance(feet, (int, float, np.ndarray)), "feet should be an integer, a float, or a numpy array"

    # Assert that inches is an integer, a float, or a numpy array
    assert isinstance(inches, (int, float, np.ndarray)), "inches should be an integer, a float, or a numpy array"

    # Constants for conversion
    # Here we define a local constant that represents the number of meters in a foot
    FEET_TO_METERS = 0.3048

    # Here we define a local constant that represents the number of meters in an inch
    INCHES_TO_METERS = 0.0254

    # Convert feet to meters
    # We multiply the number of feet by the number of meters in a foot
    feet_in_meters = feet * FEET_TO_METERS

    # Convert inches to meters
    # We multiply the number of inches by the number of meters in an inch
    inches_in_meters = inches * INCHES_TO_METERS

    # Total length in meters
    # We add the number of meters from the feet and the inches together
    total_meters = feet_in_meters + inches_in_meters

    # We return the total number of meters rounded to 4 decimal places
    return np.round(total_meters,4)

# Test the function
# We define a global variable for the number of feet
feet = 5

# We define a global variable for the number of inches
inches = 3

# We call our function with the number of feet and inches
# and store the result in a variable called meters
meters = convert_to_meters(feet, inches)

# We print out the result in a formatted string
print(f"{feet} feet {inches} inches is equal to {meters} meters.")

# Test the function with numpy arrays
# We define a global variable for the number of feet
feet = np.array([5, 6])

# We define a global variable for the number of inches
inches = np.array([3, 2])

# We call our function with the number of feet and inches
# and store the result in a variable called meters
meters = convert_to_meters(feet, inches)

# We print out the result in a formatted string
for i in range(len(feet)):
    print(f"{feet[i]} feet {inches[i]} inches is equal to {meters[i]} meters.")

    
    
## Test the function ~Emily Pearson
print("Tests done by Emily Pearson:")
#test for integers
inches = 1  #global variable for inches
feet = 1  #global variable for feet
meters = convert_to_meters(inches, feet)  #make variable to store what the function returns
print(f"{feet} feet {inches} inches is 0.3302 meters. The function returns {meters} meters.")

#test for floats
inches = 1.5  #global variable for inches
feet = 1.5  #global variable for feet
meters = convert_to_meters(inches, feet)  #make variable to store what the function returns
print(f"{feet} feet {inches} inches is 0.4953 meters. The function returns {meters} meters.")

#test for arrays, using google to check values in meters
feet = np.array([1,2])  #global variable for feet
inches = np.array([3,4])  #global variable for inches
meters = convert_to_meters(feet, inches)  #make variable to store what the function returns
#make a loop that iterates for each value in the inches array
for i in range(len(inches)):
    print(f"The function converts {feet[i]} feet {inches[i]} inches to {meters[i]} meters.")