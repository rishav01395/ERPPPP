from django.db import models
from accounts.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='branches')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.course.name} - {self.name}"

class Semester(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='semesters')
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.branch.course.name} {self.branch.name} ({self.name})"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='subjects')

    def __str__(self):
        return f"{self.name} - {self.semester.branch.name} ({self.semester.name})"

class TeacherSubjectAllotment(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'TEACHER'})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.teacher.username} -> {self.subject.name}"
class InternalMark(models.Model):
    EXAM_TYPE_CHOICES = [
        ('Sessional 1', 'Sessional 1'),
        ('Sessional 2', 'Sessional 2'),
        ('Assignment', 'Assignment'),
        ('Practical', 'Practical'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'STUDENT'}, related_name='internal_marks')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    exam_type = models.CharField(max_length=50, choices=EXAM_TYPE_CHOICES)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    max_marks = models.DecimalField(max_digits=5, decimal_places=2, default=100.00)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'subject', 'exam_type')

    def __str__(self):
        return f"{self.student.username} - {self.subject.code} - {self.exam_type}: {self.marks_obtained}/{self.max_marks}"