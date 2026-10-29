from django.db import models
from accounts.models import StudentProfile

class FeeStructure(models.Model):
    course = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    academic_year = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    development_fee = models.DecimalField(max_digits=10, decimal_places=2)
    hostel_fee = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.course} ({self.branch}) - {self.academic_year}"


class StudentFeeAccount(models.Model):
    student = models.OneToOneField(StudentProfile, on_delete=models.CASCADE, related_name='fee_account')
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE)
    total_payable = models.DecimalField(max_digits=10, decimal_places=2)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_fully_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Fee Account: {self.student.enrollment_id}"


class PaymentTransaction(models.Model):
    PAYMENT_MODES = [
        ('ONLINE', 'Online Gateway (Razorpay)'),
        ('OFFLINE', 'Offline Cash/Cheque'),
    ]
    fee_account = models.ForeignKey(StudentFeeAccount, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODES, default='ONLINE')
    transaction_id = models.CharField(max_length=100, unique=True)
    receipt_number = models.CharField(max_length=50, unique=True)
    is_successful = models.BooleanField(default=False)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Receipt #{self.receipt_number} - Rs. {self.amount}"