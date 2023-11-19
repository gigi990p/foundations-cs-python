def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key.lower() < arr[j].lower():
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def main():
    # Get input from the user
    user_input = input("Enter a list of elements separated by commas: ")

    # Convert the input string to a list
    input_list = user_input.split(',')

    # Remove leading and trailing whitespaces from each element
    input_list = [element.strip() for element in input_list]

    # Perform insertion sort
    insertion_sort(input_list)

    # Display the sorted list
    print("Sorted List:", input_list)


if __name__ == "__main__":
    main()

