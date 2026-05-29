day1_attendees = {3245, 8790, 6785, 9087, 7643, 5432, 6543}
day2_attendees = {3245, 6785, 5432, 7843, 8790, 1123, 9087}

attened_both = day1_attendees.intersection(day2_attendees)
total_students_joined = day1_attendees.union(day2_attendees)

print(f"Students attended both day of workshop: {attened_both}, total = {len(attened_both)}")
print(f"Students who joined to the tech workshop: {total_students_joined}, total = {len(total_students_joined)}")