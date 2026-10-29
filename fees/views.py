from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FeeStructure, StudentFeeAccount, PaymentTransaction
from .forms import FeeStructureForm

@login_required(login_url='login')
def manage_fees(request):
    if request.user.role != 'ADMIN':
        return redirect('admin_dashboard')
    
    fee_structure_form = FeeStructureForm()
    
    if request.method == 'POST':
        # 1. Agar naya Course Fee Structure add kiya ja raha hai
        if 'add_fee_structure' in request.POST:
            form = FeeStructureForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('manage_fees')
        
        # 2. Agar Student ki offline payment update ki ja rahi hai
        elif 'student_account_id' in request.POST:
            student_account_id = request.POST.get('student_account_id')
            amount_paid = float(request.POST.get('amount_paid', 0))
            payment_mode = request.POST.get('payment_mode', 'Cash')
            receipt_no = request.POST.get('receipt_no', '')

            account = get_object_or_404(StudentFeeAccount, id=student_account_id)
            
            PaymentTransaction.objects.create(
                student_account=account,
                amount=amount_paid,
                payment_mode=payment_mode,
                transaction_id=receipt_no,
                collected_by=request.user
            )

            account.paid_amount += amount_paid
            account.remaining_amount = account.total_fee - account.paid_amount
            account.save()

            return redirect('manage_fees')

    fee_structures = FeeStructure.objects.all()
    query = request.GET.get('q', '')
    students_accounts = StudentFeeAccount.objects.select_related('student').all()
    
    if query:
        students_accounts = students_accounts.filter(
            student__username__icontains=query
        ) | students_accounts.filter(
            student__first_name__icontains=query
        )

    context = {
        'fee_structure_form': fee_structure_form,
        'fee_structures': fee_structures,
        'students_accounts': students_accounts,
        'query': query,
    }
    return render(request, 'dashboards/manage_fees.html', context)