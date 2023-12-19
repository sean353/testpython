from comp import sum_of_digits , ispal
from col import myzip
from simp import add_num, substract_num


def main():
    
    

    result =add_num(0,1 )
    print("sum:",result)

    result = substract_num(0,1)
    print("sum:",result)



    number = 12345
    result = sum_of_digits(number)
    print(f"The sum of digits in {number} is: {result}")

    # Example usage of ispal numbers

    
    number1 = 3443
    number2 = 3223

    result1 = ispal(number1)
    result2 = ispal(number2)

    print(result1)  # This should print True
    print(result2)  # This should print True as well

list1 = [1, 2, 3]
tuple1 = ('a', 'b', 'c')
result_myzip = myzip(list1, tuple1)
print("Result of myzip:", list(result_myzip))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


if __name__ == '__main__':
    main()
