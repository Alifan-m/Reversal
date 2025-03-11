#program to reverse a list of given digits
#input staring and ending digits
start_digit = int(input("Enter the starting digit: "))
end_digit = int(input("Enter the ending digit: "))
#define function for numbers that will reverse the list
def reverse_list(numbers):
    return numbers[::-1]
#define function for the starting and ending values
def value(start, end):
    #then you list the values as list so that they can be arranged as a list
  numbers = list(range(start + 1 , end ))
  reversed_numbers = reverse_list(numbers)
  return reversed_numbers
#calculate the results of the in between digits in reversal
result = value(start_digit, end_digit)
print("Reversed List:", result)
