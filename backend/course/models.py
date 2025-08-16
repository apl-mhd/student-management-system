from django.conf import settings
from django.db import models
from student.models import Student
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator

# # Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    course_fee = models.IntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}--{self.course_fee}"


class StudentEnroll(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_fee = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return f"{self.student.name}-{self.course.name}--{self.course_fee}"


class Fee(models.Model):

    FEE_TYPES = [
        ('tuition', 'Tuition Fee'),
        ('course', 'Course Fee'),
        ('exam', 'Exam Fee'),
        ('material', 'Material Fee'),
        ('other', 'Other'),
    ]

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='billing')
    fee_type = models.CharField(
        max_length=100, choices=FEE_TYPES, null=True, blank=True)
    course = models.ForeignKey(
        Course, null=True, blank=True, on_delete=models.CASCADE)
    course_fee = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    remark = models.TextField(null=True, blank=True)
    # created_by = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return f"{self.student.name}-{self.course}-{self.course_fee}"


class Discount(models.Model):
    Discount_TYPES = [
        ('poor', 'Poor'),
        ('meritorious', 'Meritorious'),
        ('ralative', 'Relatives'),
        ('friend', 'Friends'),
        ('other', 'Other'),
    ]

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='discounts')
    discount_amount = models.IntegerField(validators=[MinValueValidator(1)])
    discount_type = models.CharField(
        max_length=20, choices=Discount_TYPES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.student.name} -- {self.discount_amount} -- {self.discount_type}"


class Payment(models.Model):
    PAYMENT_TYPES = [
        ('tuition', 'Tuition Fee'),
        ('exam', 'Exam Fee'),
        ('material', 'Material Fee'),
        ('other', 'Other'),
    ]

    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('mobile', 'Mobile Payment'),
        ('bank', 'Bank Transfer'),
    ]

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name='payments')
    payment_amount = models.IntegerField(validators=[MinValueValidator(1)])
    payment_date = models.DateTimeField(default=timezone.now)
    payment_type = models.CharField(
        max_length=20, choices=PAYMENT_TYPES, null=True, blank=True, default='tuition')
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHODS, null=True, blank=True)
    status = models.CharField(max_length=20, default='completed')
    reference_number = models.CharField(max_length=250, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.student} - {self.payment_amount} on {self.payment_date}"
