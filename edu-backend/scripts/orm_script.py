from course.models import *
from student.models import *
from django.utils import timezone
from django.db.models import F, Max, Q, Avg, Sum, Count, Subquery, OuterRef, Case, When, Value, CharField, Exists
from django.db import connection
from django.db.models.functions import Coalesce


def run():

    hsc_batch = AcademicYear.objects.filter(pk=2).first()


    student = Student.objects.filter(
        hsc_batch=hsc_batch).order_by('-id').first()

    student_roll = None
    if student:
        last_roll = student.student_roll
        student_roll = last_roll+1
    else:
        print("else")
        student_roll = int(str(hsc_batch.year % 100)+str("0001"))

    print(student_roll)

    ## Important#
    # payment = Payment.objects.filter(student=OuterRef('pk')).values('student').annotate(
    #     total=Sum('payment_amount')).values('total')

    # discount = Discount.objects.filter(student=OuterRef('pk')).values('student').annotate(
    #     total=Sum('discount_amount')).values('total')

    # bill = StudentEnroll.objects.filter(student=OuterRef('pk')).values('student').annotate(
    #     total=Sum('course_fee')).values('total')

    # students = Student.objects.values('batch').annotate(
    #     total_payment=Subquery(payment),
    #     total_bill=Subquery(bill),
    #     total_discount=Subquery(discount),
    #     yes_no=Case(
    #         When(Exists(payment), then=Subquery(payment)),
    #         default=Value(-1)
    #     ),

    #     y_n=Coalesce(Subquery(payment), Value(0)),
    # ).values('id', 'total_bill', 'total_payment', 'total_discount')

    # t = Student.objects.filter(batch=1).annotate(
    #     total_payment=Subquery(payment),
    #     total_bill=Coalesce(Subquery(bill), Value(0)),
    #     total_discount=Subquery(discount),
    #     yes_no=Case(
    #         When(Exists(payment), then=Subquery(payment)),
    #         default=Value(-1)
    #     ),

    #     y_n=Coalesce(Subquery(payment), Value(0)),
    # ).values('total_payment', 'total_bill', 'total_discount').aggregate(all_payment=Sum('total_payment'), all_bill=Sum('total_bill'), all_discount=Sum('total_discount'))

    # allp = Payment.objects.aggregate(total_payment=Sum('payment_amount'))
    # alld = Discount.objects.aggregate(
    #     total_discount=Sum('discount_amount'))
    # print(allp, alld)
    # print(t)

    # s = Student.objects.filter(batch__isnull=True).values('id')
    # b = StudentBilling.objects.all().values('student')

    ## Important#

    # print(s)
    # print(b)
    # for i in students:
    #     print(
    #         f"{i['id']}--{i['total_bill']}--{i['total_payment']}--{i['total_discount']}")

    # print(connection.queries)

    # for i in student:
    #     print(i.id, '---', i.y_n)

    # print(connection.queries)

    # batch = Batch.objects.prefetch_related('days').all()

    # data = []
    # for i in batch:
    #     day_name = ''
    #     for j in i.days.all():
    #         day_name += j.name+"-"

    #     day_name = f"{day_name}{i.start_time.strftime('%H:%M')} to {i.end_time.strftime('%H:%M')}"
    #     data.append({"id": i.id, "day_name": day_name})
    # print(data)
    # print(dict(Day.DAYS_CHOICES))
    # print(batch[0].days.all()[0].name)

    # current_month = timezone.now().replace(
    #     day=1)

    # current_month_payment_exists = Payment.objects.filter(
    #     student=OuterRef('pk'),
    #     payment_date__month=current_month.month,
    #     payment_date__year=current_month.year
    # ).values('id')

    # students = Student.objects.select_related('hsc_batch').annotate(
    #     total_course_amount=Subquery(
    #         StudentBilling.objects.filter(student=OuterRef('pk')).values('student').annotate(
    #             total=Sum('course_fee', default=0)
    #         ).values('total')
    #     ),
    #     total_discount=Subquery(
    #         StudentBilling.objects.filter(student=OuterRef('pk')).values('student').annotate(
    #             total=Sum('discount', default=0)
    #         ).values('total')
    #     ),
    #     total_payment=Subquery(
    #         Payment.objects.filter(student=OuterRef('pk')).values('student').annotate(
    #             total=Sum('payment_amount', default=0)
    #         ).values('total')
    #     ),
    #     paid_current_month=Case(
    #         When(Exists(current_month_payment_exists), then=Value('Yes')),
    #         default=Value('No')
    #     ),
    #     due_amount=F('total_course_amount') -
    #     F('total_discount') - F('total_payment')

    # ).values('id', 'name', 'hsc_batch__year', 'total_course_amount', 'total_discount', 'total_payment', 'paid_current_month', 'due_amount')

    # print(students)
    # for i in students:
    #     print(f"{i.id} --- {i.name} --- {i.total_course_amount} ---- {i.total_discount} --- {i.total_payment}")

    # Query for annotating student data
    # students = Student.objects.annotate(
    #     total_course_amount=Subquery(
    #         StudentBilling.objects.filter(student=OuterRef('pk')).values('student').annotate(
    #             total=Sum('course_fee')
    #         ).values('total')
    #     ),
    #     total_discount=Subquery(
    #         StudentBilling.objects.filter(student=OuterRef('pk')).values('student').annotate(
    #             total=Sum('discount')
    #         ).values('total')
    #     ),
    #     total_payment=Subquery(
    #         Payment.objects.filter(student=OuterRef('pk')).values('student').annotate(
    #             total=Sum('payment_amount')
    #         ).values('total')
    #     ),
    #     paid_current_month=Case(
    #         When(Exists(current_month_payment_exists), then=Value('Yes')),
    #         default=Value('No'),
    #     )
    # )

    # print(students)

    # current_month = timezone.now().replace(
    #     day=1, hour=0, minute=0, second=0, microsecond=0)

    # students = Student.objects.annotate(
    #     total_course_amount=Sum('billing__course_amount'),
    #     total_discount=Sum('billing__discount'),
    #     total_payment=Sum('payments__amount_payment'),
    #     current_month=Max(Case(
    #         When(
    #             Q(payments__payment_date__gte=current_month), then=Value('Yes'),
    #         ),
    #         default=Value('No')

    #     ))
    # )
    # students2 = Student.objects.annotate(
    #     total_course_amount=Sum('billing__course_amount', distinct=True),
    #     total_discount=Sum('billing__discount',  distinct=True),
    #     total_payment=Sum('payments__amount_payment',  distinct=True),
    #     current_month=Max(Case(
    #         When(
    #             Q(payments__payment_date__gte=current_month), then=Value('Yes'),
    #         ),
    #         default=Value('No')

    #     ))
    # )

    # print(students2)

    # for i in students2:
    #     print(
    #         f"{i.name} -- {i.total_course_amount} -- {i.total_discount} -- {i.total_payment} -- {i.current_month}")

    # print(students[0].total_payment)

    # current_month = timezone.now().replace(
    #     day=1, hour=0, minute=0, second=0, microsecond=0)

    # current_month_start = timezone.now().replace(
    #     day=1)  # Start of the current month

    # students = Student.objects.annotate(
    #     total_discounts=Sum('payments__discount'),
    #     total_payments=Sum('payments__payment'),
    #     total_course_amount=Sum('payments__course_amount'),
    #     paid_current_month=Case(
    #         When(
    #             Q(payments__created_at__gte=current_month_start) &
    #             Q(payments__payment__gt=0),
    #             then=Value('Yes')
    #         ),
    #         default=Value('No'),
    #         output_field=CharField()
    #     )
    # ).distinct()

    # print(students)
    # for i in students:
    #     print(
    #         f"{i.id} -- {i.total_discounts} -- {i.total_payments} -- {i.total_course_amount}")

# payment = Payment.objects.annotate(
#     current_month_payement=Case(
#         When(Q(created_at__gte=current_month) &
#              Q(payment__gt=0), then=Value('Yes')),
#         default=Value('No')
#     )
# ).values('student_id').distinct()

# stu_payment = Student.objects.annotate(
#     current_month_payment=Case(
#         When(
#             Q(payments__created_at__gte=current_month) &
#             Q(payments__payment__gt=0), then=Value('Yes')
#         ),
#         # default=Value("No"),
#         output_field=CharField()
#     )
# ).distinct()

# .annotate(
#     current_month_payement=Case(
#         When(Q(created_at__gte=current_month) &
#              Q(payment__gt=0), then=Value('Yes')),
#         default=Value('No')
#     )
# ).values('student_id').distinct()

# for i in payment:
#     print(f"{i['id']}---{i['current_month_payement']}")

# payment = Payment.objects.values('student_id').filter(
#     Q(created_at__gte=current_month) & Q(payment__gt=0)
# )
# payment = Payment.objects.filter(
#     Q(created_at__gte=current_month) & Q(payment__gt=0)
# ).values('student_id').distinct()

# sub = Payment.objects.filter(Q(student_id__in=Subquery(
#     payment))).annotate(total_payment=Sum('payment'))

# Payment.objects.annotate(a=Sum('payment'))

# print(connection.queries)
