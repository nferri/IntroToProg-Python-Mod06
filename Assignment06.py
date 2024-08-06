# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions with structured error handling
# Change Log: (Who, When, What)
#   Natalie Ferri, 08/01/2024, Reviewing script
#   Natalie Ferri, 08/03/2024, Modifying Assignment05 with class and functions
#   Natalie Ferri, 08/04/2024, Defining classes for presenting data section
#   Natalie Ferri, 08/05/2024, Trying to resolve str int error
# ------------------------------------------------------------------------------------------ #


import json

# Define the Data Constants
FILE_NAME: str = "Enrollments.json"
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a student for a course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the Data Variables
menu_choice: str = "" # choice made by the user
students: list = [] # a table of student data

# Process the data  --------------------------------------------------------- #

class FileProcessor:

    '''
    This class reads and writes to JSON files.
    '''

    # Open the JSON
    @staticmethod
    def read_data_from_file (file_name: str, student_data: list):

        '''
        This function loads data from a JSON to a dictionary. Error prints if file
            does not exist or issue reading.
            
        Change Log:
            Natalie Ferri, 08/03/2024, incorporate IO error
        '''

        try:
            file = open (file_name, "r")
            student_data = json.load (file)
            file.close()
            
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
            
        except Exception as e:
            IO.output_error_messages (message= "Error: Issue reading the file. \n", error=e)

        finally:
            if file.closed == False:
                file.close()
                
        return student_data

    # Save the data to JSON
    @staticmethod
    def write_data_to_file (file_name: str, student_data: list):
        '''
        This function writes data to a JSON with data from a list of rows. Error prints if
            file does not write.
            
        ChangeLog:
            Natalie Ferri, 08/03/2024, created function to write to JSON
        '''
    
        try: 
            file = open (file_name, "w")
            json.dump (student_data, file)
            file.close()
            
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
            
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
            
        finally:
            if file.closed == False:
                file.close()

    ### Print students

                
# Present the data   --------------------------------------------------------- #
class IO:
    '''
    This class inlcudes functions that display a mentu with choices, accepts user input,
        present user input, and has error handling.
    '''
    pass

    # Error message
    @staticmethod
    def output_error_messages (message: str, error: Exception = None):
        '''
        This functions handles built-in errors.
            
        ChangeLog:
            Natalie Ferri, 08/03/2024, created function to present errors
        '''
        
        print (message)
        if error is not None:
            print ("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    # Print menu
    @staticmethod
    def output_menu (menu: str):
        '''
        This function shows the menu
            
        ChangeLog:
            Natalie Ferri, 08/04/2024, created function to present menu
        '''  

        print (menu, "\n")

    # Menu choice    
    @staticmethod
    def input_menu_choice():
        '''
        This function allows for menu choice to be selected by user.
            
        ChangeLog:
            Natalie Ferri, 08/04/2024, created function accepts user input
        '''
    
        choice = "0"

        try:
            choice = input ("Enter menu item: ")
            if choice not in ("1","2","3","4"):
                raise Exception ("\nInput not understood.")

        except Exception as e:
            IO.output_error_messages (e.__str__())
            
        return choice

    # User input of student data
    @staticmethod
    def input_student_data (student_data: list):
        '''
        This function allows user to input student data.
            
        ChangeLog:
            Natalie Ferri, 08/04/2024, created function for user input 
        '''

        try:
            student_first_name = input ("Enter the student's first name in all caps: ")
            if not student_first_name.isupper():
                raise AttributeError ("Error: The first name should be in all caps.\n")

            student_last_name = input ("Enter the student's last name in all caps: ")        
            if not student_last_name.isupper():
                raise AttributeError ("Error: The last name should be in all caps.\n")

            course_name = input ("Enter course name: ") 
            
            # Dictionary for JSON
            student_data = {
                            "FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name,
                            }


            students.append(student_data)
            
            print (f"You have registered {student_first_name} {student_last_name} for {course_name}. \n")
            
        except AttributeError as e:
            IO.output_error_messages (message="\nERROR", error=e)
            
        except Exception as e:
            IO.output_error_messages (message="\nError: There was a problem with your entered data.", error=e)
            
        return student_data
    

    # Print user input
    @staticmethod
    def output_student_courses(student_data: list):
        '''
        This function displays the collected student data to the user.

        ChangeLog:
        Natalie Ferri, 08/04/2024, created function printing data
        '''
            
        for student in students:
            print({student['FirstName']}, {student['LastName']}, {student['CourseName']})
 
# Extract the data from the file
students = FileProcessor.read_data_from_file (file_name=FILE_NAME, student_data=students)


# Present and Process the data
'''
This code defines the menu choices to choose from
    Change log:
        Natalie Ferri, 08/04/2024, defining menu_choice items
'''
while (True):

    # Present the menu of choices
    IO.output_menu (menu=MENU)
    menu_choice = IO.input_menu_choice()

    # 1. Register a student for a course.
    if menu_choice == "1":
        students = IO.input_student_data (student_data=students)
        continue

    # 2. Show current data.  
    elif menu_choice == "2":
        students = IO.output_student_courses (student_data=students) 
        continue

    # 3. Save data to a file.
    elif menu_choice == "3":
        FileProcessor.write_data_to_file (file_name=FILE_NAME, student_data=students)
        continue


    # 4. Exit the program.
    elif menu_choice == "4":
        break  # Out of the loop

    else:
        print ("Please only choose option 1, 2, 3, or 4.")

# Signifies end of program
print ("Thank you for your input. Goodbye. \n")
