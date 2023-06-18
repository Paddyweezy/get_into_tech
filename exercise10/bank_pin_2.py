def check_pin():

    supplied_pin = input("Enter your PIN")
    correct_pin = "1234"

Attempts = 3

while Attempts > 0:
    if supplied_pin == correct_pin:
        print("Success! Access Granted")
        break