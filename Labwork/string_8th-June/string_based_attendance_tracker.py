#  String-Based Attendance Tracker
# Problem Statement
# Attendance of a student for 15 days is represented as:
# PPAPPPAAPPPPAPP
# Where:
# • P = Present
# • A = Absent
# Tasks
# Write a program to:
# 1. Count Present and Absent days.
# 2. Calculate attendance percentage.
# 3. Find the longest consecutive streak of Presence.
# 4. Find the longest consecutive streak of Absence.
# 5. Determine whether attendance is below 75%

# String-Based Attendance Tracker

attendance = "PPAPPPAAPPPPAPP"

print("Attendance Record:", attendance)

# Count Present and Absent days
present_days = attendance.count('P')
absent_days = attendance.count('A')

# Attendance percentage
attendance_percentage = (present_days / len(attendance)) * 100

# Longest consecutive Present streak
current_present = 0
longest_present = 0

# Longest consecutive Absent streak
current_absent = 0
longest_absent = 0

for status in attendance:

    if status == 'P':
        current_present += 1
        current_absent = 0

        if current_present > longest_present:
            longest_present = current_present

    else:
        current_absent += 1
        current_present = 0

        if current_absent > longest_absent:
            longest_absent = current_absent

# Display results
print("\nPresent Days:", present_days)
print("Absent Days:", absent_days)

print(f"\nAttendance Percentage: {attendance_percentage:.2f}%")

print("\nLongest Present Streak:", longest_present)
print("Longest Absent Streak:", longest_absent)

# Check attendance eligibility
if attendance_percentage < 75:
    print("\nStatus: Attendance Below 75%")
else:
    print("\nStatus: Attendance Above 75%")