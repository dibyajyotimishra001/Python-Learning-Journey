class EngineeringCollege:
    university_name = "Technical University"

    def __init__(self, student_name, programming_language):
        self.student_name = student_name
        self.programming_language = programming_language
        
student_1 = EngineeringCollege("Yuji Itadori", "JavaScript")
print(student_1.student_name, student_1.university_name, EngineeringCollege.university_name)

student_2 = EngineeringCollege("Aoi Todo", "Python")
print(student_2.student_name, student_2.university_name, EngineeringCollege.university_name)