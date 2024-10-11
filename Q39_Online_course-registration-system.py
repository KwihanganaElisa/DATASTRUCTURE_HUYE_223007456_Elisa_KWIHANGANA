from collections import deque


class CourseRegistrationSystem:
    
    def __init__(self):
        self.available_courses = [] 
        self.registration_requests = deque()  
        self.undo_stack = [] 

    def add_course(self, course_name):
        self.available_courses.append(course_name)
        print(f"Course '{course_name}' added to available courses.")

    def show_available_courses(self):
        if self.available_courses:
            print("\nAvailable Courses:")
            for idx, course in enumerate(self.available_courses, 1):
                print(f"{idx}. {course}")
        else:
            print("\nNo courses available.")

    def register_course(self, course_name):
        if course_name in self.available_courses:
            self.registration_requests.append(course_name)
            self.undo_stack.append(course_name)
            print(f"Course '{course_name}' registered successfully.")
        else:
            print(f"Course '{course_name}' is not available for registration.")

    def process_registration(self):
        if self.registration_requests:
            course_name = self.registration_requests.popleft()
            print(f"Processing registration for '{course_name}'...")
        else:
            print("No registration requests to process.")

    def undo_registration(self):
        if self.undo_stack:
            last_registered_course = self.undo_stack.pop()
            print(f"Undo registration for '{last_registered_course}'.")
        else:
            print("No registrations to undo.")

# Interactive menu
def menu():
    registration_system = CourseRegistrationSystem()

    while True:
        print("\n1. Add Course")
        print("2. Show Available Courses")
        print("3. Register for a Course")
        print("4. Process Registration")
        print("5. Undo Last Registration")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            course_name = input("Enter course name to add: ")
            registration_system.add_course(course_name)

        elif choice == '2':
            registration_system.show_available_courses()

        elif choice == '3':
            course_name = input("Enter course name to register: ")
            registration_system.register_course(course_name)

        elif choice == '4':
            registration_system.process_registration()

        elif choice == '5':
            registration_system.undo_registration()

        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")
menu()
