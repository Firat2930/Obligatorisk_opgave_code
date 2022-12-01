class Course:
   def __init__(self , c_code, c_name, c_level, room):
        self.kursus_id=c_code
        self.kursus_name=c_name
        self.kursus_level=c_level
        self.students = []
        self.lectures = []
        self.obj_room=room
   def assign_student(self, student_obj):

       self.students.append(student_obj)

   def remove_student(self, email):

        for stu in self.students:
            if (email==stu.email):
                return self.students.remove(stu)
            print("Student removed succesfully removed")

   def assign_lecture(self, lecture_obj):

        self.lectures.append(lecture_obj)
   def remove_lecture(self, lecture_id):

       for lec in self.lectures:
           if (lec.lecture_id == id):
               self.lectures.remove(lec)
               print("Lecture removed succesfully removed")
   def get_all_students(self):

       return self.students
   def get_all_lectures(self):

        return self.lectures