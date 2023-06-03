import random
from datetime import date, timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction

from kitchen.models import Employee, Day


class Command(BaseCommand):
    help = 'Populates the kitchen tables with random data'

    def handle(self, *args, **options):
        # Generate random employees
        employee_count = 10  # Number of employees to generate
        employees = []

        for i in range(employee_count):
            username = f'employee{i + 1}'
            password = 'password'
            user = User.objects.create_user(username=username, password=password)
            employee = Employee.objects.create(user=user)
            employees.append(employee)

        # Generate random days
        start_date = date.today() - timedelta(days=30)  # Start date for generating days
        end_date = date.today() + timedelta(days=30)  # End date for generating days
        days = []

        current_date = start_date
        while current_date <= end_date:
            day = Day.objects.create(date=current_date)
            days.append(day)
            current_date += timedelta(days=1)

        # Assign random availability for employees
        with transaction.atomic():
            for employee in employees:
                # Randomly select available days for the employee
                available_days = random.sample(days, k=random.randint(0, len(days)))
                employee.available_days.set(available_days)

        self.stdout.write(self.style.SUCCESS('Data population completed.'))
