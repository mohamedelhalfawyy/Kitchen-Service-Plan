from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from kitchen.models import Employee
from kitchen.serializers import EmployeeSerializer


class RemoveEmployeeView(APIView):
    def delete(self, request, employee_id):
        employee = get_object_or_404(Employee, id=employee_id)

        # Remove employee from all availability
        employee.available_days.clear()
        # Delete the employee
        employee.delete()

        return Response({'message': 'Employee removed successfully.'})


class AddEmployeeView(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Employee added successfully.'})
        else:
            return Response(serializer.errors, status=400)


class KitchenServicePlanView(APIView):
    def get(self, request, year, month, day):
        start_date = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
        end_date = start_date + timedelta(days=6)

        employees = Employee.objects.all()
        plan = {}

        for employee in employees:
            available_days = employee.available_days.filter(date__range=[start_date, end_date])
            vacation_days = employee.available_days.exclude(date__range=[start_date, end_date])

            if available_days:
                plan[employee.user.username] = [str(day) for day in available_days]

        vacation_plan = {
            'vacation_days': []
        }

        for employee in employees:
            vacation_days = employee.available_days.exclude(date__range=[start_date, end_date])
            if vacation_days:
                vacation_plan['vacation_days'].append({
                    'employee': employee.user.username,
                    'days': [str(day) for day in vacation_days]
                })

        response = {
            'plan_of_week': plan,
            'vacation_plan': vacation_plan
        }

        return Response(response)
