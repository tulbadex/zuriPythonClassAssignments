# children because its inheriting from parent Exception
# inherentance
class CustomException(Exception):
    pass

# branch children
class ValueTooSmallException(CustomException):
    pass

class ValueTooBigException(CustomException):
    pass

number_value = 20

while True:
    try:
        input_number = int(input("Enter a number: "))
        if input_number < number_value:
            raise ValueTooSmallException
        elif input_number > number_value:
            raise ValueTooBigException
        break
    except ValueTooSmallException as _:
        print("Value too small")
    except ValueTooBigException as _:
        print("Value too big")
    except Exception as _:
        print(_.__str__())

print("Hey you got it correctly")