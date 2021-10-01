def main():
    elements = list(map(int, input("Enter the array of elements seperated by spaces to be sorted using bubble sort: ").split(" ")))
    for i in range(len(elements)):
        for j in range(0, len(elements) - i - 1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]

    print(f"Sorted array: ", end='')
    for element in elements:
        print(f"{element} ", end='')


if __name__ == "__main__":
    main()