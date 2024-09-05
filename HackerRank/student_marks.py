if __name__ == '__main__':
    # Read the number of students
    n = int(input("Enter the number of students: ").strip())
    
    student_marks = {}
    
    # Read each student's data
    for _ in range(n):
        line = input("Enter student data: ").strip().split()
        name = line[0]
        scores = list(map(float, line[1:]))
        student_marks[name] = scores
    
    # Read the query name
    query_name = input("Enter the name to query: ").strip()
    
    # Retrieve the scores for the query name
    scores = student_marks[query_name]
    
    # Calculate the average of the scores
    average = sum(scores) / len(scores)
    
    # Print the average rounded to 2 decimal places
    print(f"{average:.2f}")
