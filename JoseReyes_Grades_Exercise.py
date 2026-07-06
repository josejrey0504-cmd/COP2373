import csv

# This function collects student information and saves it to a CSV file
# so the data can be stored and used later.
def create_grades_file():

    # Ask the instructor how many student records need to be entered.
    num_students = int(input("How many students do you want to enter? "))

    # Open grades.csv in write mode. The newline argument prevents
    # blank lines from appearing between records on some operating systems.
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        # Add a header row so each column has a label.
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Repeat until information has been entered for every student.
        for i in range(num_students):

            print(f"\nStudent #{i + 1}")

            # Collect the student's name and exam grades.
            first = input("First Name: ")
            last = input("Last Name: ")

            exam1 = int(input("Exam 1 Grade: "))
            exam2 = int(input("Exam 2 Grade: "))
            exam3 = int(input("Exam 3 Grade: "))

            # Save the student's information as one row in the CSV file.
            writer.writerow([first, last, exam1, exam2, exam3])


# This function reads the CSV file and displays the information
# in a formatted table.
def display_grades_file():

    # Display column headings before printing the student records.
    print("\n{:<15}{:<15}{:<10}{:<10}{:<10}".format(
        "First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"))

    # Open the file in read mode so the stored information can be displayed.
    with open("grades.csv", "r", newline="") as file:
        reader = csv.reader(file)

        # Skip the header because it is already displayed above.
        next(reader)

        # Print each student's information in neatly aligned columns.
        for row in reader:
            print("{:<15}{:<15}{:<10}{:<10}{:<10}".format(
                row[0], row[1], row[2], row[3], row[4]))


# The main function controls the order the program runs in.
def main():

    # First create the CSV file using the instructor's input.
    create_grades_file()

    print("\nGrades have been saved to grades.csv")

    # Then read the file back and display its contents.
    display_grades_file()


# Call the main function to start the program.
main()