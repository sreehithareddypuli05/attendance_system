from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.roll_no} - {self.user.username}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('Present','Present'), ('Absent','Absent')])

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
