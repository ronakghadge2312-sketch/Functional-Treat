
# 1. Data Input & Initialization

marks = [21, 35, 38, 40, 45, 50, 52, 55, 58, 60,
         62, 70, 72, 75, 80, 82, 85, 90, 96, 98]


# 2. Basic Analysis

total_students = len(marks)
highest = max(marks)
lowest = min(marks)
total_marks = sum(marks)
average = total_marks / total_students


# Count Passed and Failed Students

passed = 0
failed = 0

for mark in marks:
    if mark >= 40:
        passed = passed + 1
    else:
        failed = failed + 1
        
# Students who scored exactly 100

hundred = marks.count(100)

# Pass Percentage

pass_percentage = (passed / total_students) * 100

print("Total Students:", total_students)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Passed:", passed)
print("Failed:", failed)
print("Students Scored 100:", hundred)
print("Pass Percentage:", pass_percentage)

# 3. Advanced Built-in Function Usage

ascending = sorted(marks)

descending = sorted(marks, reverse=True)

print("Sorted Marks:", ascending)
print("Descending Marks:", descending)

# Second Highest and Second Lowest

second_highest = descending[1]
second_lowest = ascending[1]

print("Second Highest:", second_highest)
print("Second Lowest:", second_lowest)

# Check all students passed

all_passed = all(mark >= 40 for mark in marks)

# Check if any student failed

any_failed = any(mark < 40 for mark in marks)

print("All Students Passed:", all_passed)
print("Any Student Failed:", any_failed)


# 4. Optional Task

search = int(input("Enter a mark to search: "))

if search in marks:
    print("Mark exists in the list.")
else:
    print("Mark does not exist in the list.")


# 5. Grade Distribution

A = 0
B = 0
C = 0
D = 0
E = 0
F = 0

for mark in marks:

    if mark >= 90:
        A = A + 1

    elif mark >= 80:
        B = B + 1

    elif mark >= 70:
        C = C + 1

    elif mark >= 60:
        D = D + 1

    elif mark >= 40:
        E = E + 1

    else:
        F = F + 1


print("Grade A:", A, "Students")
print("Grade B:", B, "Students")
print("Grade C:", C, "Students")
print("Grade D:", D, "Students")
print("Grade E:", E, "Students")
print("Grade F:", F, "Students")
