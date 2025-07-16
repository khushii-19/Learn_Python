def switch_example(day):
    switch = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    # .get() returns value if key exists, else default "Invalid day"
    return switch.get(day, "Invalid day")

# Test
day_number = int(input("Enter day number (1-7): "))
print(switch_example(day_number))


def switch_example(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"

# Test
day_number = int(input("Enter day number (1-7): "))
print(switch_example(day_number))