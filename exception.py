# in python exception handle by try except

try:
    list = [12, 0, 23]
    result = list[0] / list[1]
    print(result);
    print("DONE")
except ZeroDivisionError:
    print("Zero Division Error is not possible.")

# Multiple Error handle

try:
    list = [12, 0, 23]
    result = list[0] / list[3]
    print(result);
    print("DONE")
except ZeroDivisionError:
    print("Zero Division Error is not possible.")
except IndexError as e:
    print(e)
finally:  # exception caught or not, Must Work Block
    print("Successfull.")


# Raise Exception Handle

def voter(age):
    if age < 18:
        raise ValueError("Age Is Low.")
    return "you are allowed for vote."

print(voter(19))
print(voter(17))
