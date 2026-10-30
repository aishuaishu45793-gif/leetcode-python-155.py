try:
    numbers = list(map(
        int,
        input("Enter numbers separated by spaces: ").split()
    ))

    unique_numbers = sorted(set(numbers))

    if len(unique_numbers) < 2:
        print("There is no second-largest distinct number.")
    else:
        print("Second-largest number:", unique_numbers[-2])

except ValueError:
    print("Please enter integers only.")