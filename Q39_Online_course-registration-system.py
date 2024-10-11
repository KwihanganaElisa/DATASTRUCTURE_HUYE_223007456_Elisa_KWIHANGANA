from collections import deque

class StudentGradingSystem:
    def __init__(self):
        self.grade_stack = []   # Stack for undo operations (grades to undo)
        self.pending_queue = deque()  # Queue for pending grading submissions
        self.final_grades = []  # List to store all finalized student grades

    def add_submission(self, student_id):
        """Add a new submission to the queue of pending grades."""
        self.pending_queue.append(student_id)
        print(f"Submission added for student {student_id}.")

    def grade_next_submission(self, grade):
        """Grade the next student in the pending queue and add to stack for undo option."""
        if self.pending_queue:
            student_id = self.pending_queue.popleft()
            self.grade_stack.append((student_id, grade))  # Add grade to stack for potential undo
            self.final_grades.append((student_id, grade))
            print(f"Graded student {student_id} with grade {grade}.")
        else:
            print("No pending submissions to grade.")

    def undo_last_grade(self):
        """Undo the last graded submission."""
        if self.grade_stack:
            student_id, grade = self.grade_stack.pop()  # Undo the last grade
            self.final_grades.remove((student_id, grade))  # Remove from final grades list
            print(f"Undoing grade {grade} for student {student_id}.")
        else:
            print("No grades to undo.")

    def view_final_grades(self):
        """Display all finalized student grades."""
        if self.final_grades:
            print("Final Grades List:")
            for student_id, grade in self.final_grades:
                print(f"Student {student_id}: {grade}")
        else:
            print("No final grades to display.")

    def view_pending_submissions(self):
        """Display all pending submissions."""
        if self.pending_queue:
            print("Pending Submissions:")
            for student_id in self.pending_queue:
                print(f"Student {student_id}")
        else:
            print("No pending submissions.")
            
# Example usage:
grading_system = StudentGradingSystem()

# Add submissions
grading_system.add_submission(101)
grading_system.add_submission(102)
grading_system.add_submission(103)

# Grade the first two submissions
grading_system.grade_next_submission(90)  # Grades student 101
grading_system.grade_next_submission(85)  # Grades student 102

# Undo the last grading action
grading_system.undo_last_grade()

# View final grades and pending submissions
grading_system.view_final_grades()
grading_system.view_pending_submissions()

# Grade the remaining submissions
grading_system.grade_next_submission(75)  # Grades student 103

grading_system.view_final_grades()
