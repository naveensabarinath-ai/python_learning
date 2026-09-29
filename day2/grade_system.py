# Convert a validated mark to its letter grade.
def grade_for_mark(mark: float) -> str:
	if mark >= 90:
		return "A"
	if mark >= 80:
		return "B"
	if mark >= 70:
		return "C"
	if mark >= 60:
		return "D"
	return "E"


# Read a positive whole-number student count.
def read_student_count() -> int:
	while True:
		try:
			student_count = int(input("Enter the number of students: "))
		except ValueError:
			print("Please enter a whole number greater than 0.")
			continue

		if student_count > 0:
			return student_count

		print("The number of students must be greater than 0.")


# Read a non-empty name for the current student.
def read_student_name(student_number: int) -> str:
	while True:
		name = input(f"Enter the name of student {student_number}: ").strip()
		if name:
			return name
		print("Name cannot be blank. Please enter a name.")


# Read a numeric mark within the valid 0-100 range.
def read_student_mark(name: str) -> float:
	while True:
		try:
			mark = float(input(f"Enter the mark for {name} (0-100): "))
		except ValueError:
			print("Please enter a numeric mark.")
			continue

		if 0 <= mark <= 100:
			return mark

		print("Mark must be between 0 and 100.")


# Collect student results and display them after all entries are valid.
def main() -> None:
	student_count = read_student_count()
	
	# list[...]: a list of items
    # tuple[str, float, str]: each item is a 3-value tuple: a student’s name (str), mark (float), and grade (str)

	results: list[tuple[str, float, str]] = []

	for student_number in range(1, student_count + 1):
		name = read_student_name(student_number)
		mark = read_student_mark(name)
		results.append((name, mark, grade_for_mark(mark)))

	print("\nStudent Results")
	print("Name | Mark | Grade")
	for name, mark, grade in results:
		print(f"{name} | {mark:g} | {grade}")

# Start the program when this file is run directly.
if __name__ == "__main__":
	main()
