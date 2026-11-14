from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.repositories.employee import EmployeeRepository
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeResponse
)
from app.services.employee import EmployeeService


router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


def get_employee_service(
    db: Session = Depends(get_db)
):

    repository = EmployeeRepository(db)

    return EmployeeService(repository)


@router.get(
    "/",
    response_model=list[EmployeeResponse]
)
def get_employees(
    service: EmployeeService = Depends(
        get_employee_service
    )
):

    return service.get_all()


@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee(
    employee_id: int,
    service: EmployeeService = Depends(
        get_employee_service
    )
):

    return service.get_by_id(employee_id)


@router.post(
    "/",
    response_model=EmployeeResponse
)
def create_employee(
    request: EmployeeCreate,
    service: EmployeeService = Depends(
        get_employee_service
    )
):

    return service.create(request)


@router.delete("/{employee_id}")
def delete_employee(
    employee_id: int,
    service: EmployeeService = Depends(
        get_employee_service
    )
):

    return service.delete(employee_id)

@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee(
    employee_id: int,
    request: EmployeeCreate,
    service: EmployeeService = Depends(
        get_employee_service
    )
):

    return service.update(
        employee_id,
        request
    )
