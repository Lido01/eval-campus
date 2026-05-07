from .models import Department
from django.db.models import QuerySet
from typing import Optional

def get_all_departments() -> QuerySet:
    return Department.objects.all()

def get_department_by_id(department_id: int) -> Optional[Department]:
    try:
        return Department.objects.get(id=department_id)
    except Department.DoesNotExist:
        return None

def create_department(**kwargs) -> Department:
    department = Department.objects.create(**kwargs)
    return department

def update_department(department_id: int, **kwargs) -> Optional[Department]:
    department = get_department_by_id(department_id)
    if department:
        for key, value in kwargs.items():
            setattr(department, key, value)
        department.save()
        return department
    return None

def delete_department(department_id: int) -> bool:
    department = get_department_by_id(department_id)
    if department:
        department.delete()
        return True
    return False