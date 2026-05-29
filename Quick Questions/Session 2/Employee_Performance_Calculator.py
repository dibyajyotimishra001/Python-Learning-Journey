def calculate_average_ratings(employee_data):
    sum_dict = {}
    
    # Using .items() to access both the employee name (key) and their ratings list (value)
    for name, ratings in employee_data.items():
        # Calculating the sum using list indices
        total_sum = ratings[0] + ratings[1] + ratings[2]
        value_avg = total_sum / 3
        
        # Dynamically adding the new key-value pair to our result dictionary
        sum_dict[name] = value_avg
        
    return sum_dict

employee = {
    "Liam": [7, 8, 5],
    "Emma": [6, 7, 8],
    "Noah": [9, 8, 7],
}

print(f"Here are the average ratings: {calculate_average_ratings(employee)}")