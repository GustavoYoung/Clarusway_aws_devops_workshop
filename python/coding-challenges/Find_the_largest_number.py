print("### This program finds the largest number in an inputted numbers list###")

number = list(map(int, input("Please enter 5 numbers separated with commas: ").split(',')))

def max_number(number):
    max_value = number[0]
    for i in number:
        if max_value < i:
            max_value = i
    return max_value

print('The largest number is ' + str(max_number(number)))
