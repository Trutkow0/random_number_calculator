# Timothy Rutkowski 04/04/2024 timothyRutkowski_lab6-1.py

# This program will generate random numbers in the range of 1-500. The amount
# of numbers to be generated will be entered by the user. The program will total
# all the numbers generated, average them, and display the highest and lowest
# numbers.
import random

# Main function of the program
def main():
    count = get_count()
    get_rand_nums(count)
    num_list = read_file()
    total = get_total(num_list)
    average = get_average(num_list, total)
    high, low = get_high_low(num_list)
    print_results(num_list, total, average, high, low)
    
# Function to get how many numbers will be generated from the user
def get_count():
    count = int(input('How many random numbers would you like to generate? '))
    return count

# Function to get random numbers
def get_rand_nums(count):
    # Open the myRandomNumbers.txt file to write
    my_rand_nums_w = open('myRandomNumbers.txt', 'w')
    # Get random numbers for the count entered by the user
    for count in range(count):
        num = random.randint(1, 500)
        my_rand_nums_w.write(f'{num} ')
    # Close the file
    my_rand_nums_w.close()

# Function to read the file.
def read_file():
    # Open the file to read
    my_rand_nums_r = open('myRandomNumbers.txt', 'r')
    num_str = my_rand_nums_r.readline()
    num_list = [int(num) for num in num_str.split()]
    # Close the file
    my_rand_nums_r.close()
    return num_list
    
# Function to total the numbers in the file        
def get_total(num_list):
    total = sum(num_list)
    return total
    
# Function to average the numbers in the file
def get_average(num_list, total):
    average = total / len(num_list)
    return average

# Function to determine highest and lowest numbers in the file
def get_high_low(num_list):
    high = max(num_list)
    low = min(num_list)
    return high, low

# Function to display results
def print_results(num_list, total, average, high, low):
    print(f'\nNumbers Generated: {num_list}')
    print(f'\nAverage: {average:.2f}')
    print(f'\nHighest Number: {high}')
    print(f'\nLowest Number: {low}')
    
    
# Call the main function
if __name__ == '__main__':
    main()
    