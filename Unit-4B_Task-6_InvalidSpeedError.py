class InvalidSpeedError(Exception):
    pass

try:
    speed = int(input("Enter vehicle speed: "))

    if speed < 0 or speed > 120:
        raise InvalidSpeedError("Invalid speed")

    print("Valid speed")

except InvalidSpeedError as e:
    print(e)