def DistanceConversion(input):
    length = float(input[:-2])
    unit = input[-2:]
    if unit == "km":
        converted_length = round(length / 1.6)
        converted_Unit = "mi"
        result = str(converted_length) + converted_Unit
    elif unit == "mi":
        converted_length = round(length * 1.6)
        converted_Unit = "km"
        result = str(converted_length) + converted_Unit
    return result

distance = input("Enter a distance (in km or mi): ")
result = DistanceConversion(distance)
print(f'{distance} is equal to {result}.')
