"""
File: rating_stats.py
----------------------
This file defines a program that allows a user to calculate
baseline summary statistics about a datafile of professor review
data. 
"""


def calculate_rating_stats(filename):
    """
    This function analyzes the professor review data in the given
    file to calculate the percentage of reviews for both men and
    women that fall in the "high rating" bucket, which is a numerical
    rating that is greater than 3.5.

    The resulting information is printed to the console.
    """
    count_W = 0
    count_W_high = 0
    count_M = 0
    count_M_high = 0
    with open(filename) as file:
        line = next(file)
        print(line)
        for line in file:
            line = line.strip()
            # print(line)
            parts = line.split(',')
            rating = float(parts[0])
            gender = parts[1]
            if gender == 'W':
                count_W += 1
            else:
                count_M += 1
            
            if gender == 'W' and rating > 3.5:
                count_W_high += 1
            if gender == 'M' and rating > 3.5:
                count_M_high += 1

        percentage_W_high = (count_W_high / count_W) * 100
        percentage_M_high = (count_M_high / count_M) * 100
        # print(count_W)
        # print(count_M)

        print(round(percentage_W_high))
        print(round(percentage_M_high))

        print(str(round(percentage_W_high)) + '% of reviews for women in the dataset are high.')
        print(str(round(percentage_M_high)) + '% of reviews for men in the dataset are high.')

    # You fill this in.  Don't forget to remove the 'pass' statement above.


def main():
    # Ask the user to input the name of a file
    filename = input("Which data file would you like to load? ")

    # Calculate review distribution statistics by gender for
    # that file. This function should print out the results of
    # the analysis to the console.
    calculate_rating_stats(filename)


if __name__ == '__main__':
    main()
