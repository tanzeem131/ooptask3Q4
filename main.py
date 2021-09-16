class student:
    def __init__(self,student_name,USN,marks):
        self.student_name = student_name
        self.USN = USN
        self.marks = marks

    def displayDetails(self):
        print("student_name:", self.student_name, "USN:", self.USN, "marks:", self.marks)

    #marks in three subjects
    sub1,sub2,sub3 = int(input()),int(input()),int(input())


st_1 = student('tanzeem',2345617278,450)

st_1.displayDetails()