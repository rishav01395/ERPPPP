from django.db import models
from accounts.models import User
from academics.models import Subject

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'role': 'TEACHER'})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.teacher:
            return f"{self.title} ({self.teacher.username})"
        return self.title