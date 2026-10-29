from django.db import models
from accounts.models import User
from academics.models import Subject

class AttendanceSession(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'TEACHER'})
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject.name} - {self.date} ({self.teacher.username})"

class AttendanceRecord(models.Model):
    session = models.ForeignKey(AttendanceSession, on_delete=models.CASCADE, related_name='records')
    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'STUDENT'})
    status = models.CharField(
        max_length=10, 
        choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave')], 
        default='Present'
    )

    def __str__(self):
        return f"{self.student.username} - {self.status}"