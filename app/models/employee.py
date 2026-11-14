from sqlalchemy import Column, DateTime, Integer, Numeric, String
from app.database import Base
from sqlalchemy.sql import func

class Employee(Base):

    __tablename__ = "Employees"

    EmployeeId = Column(
        Integer,
        primary_key=True,
        index=True
    )

    EmployeeName = Column(
        String(100),
        nullable=False
    )

    Department = Column(
        String(100),
        nullable=False
    )

    Salary = Column(
        Numeric(18, 2),
        nullable=False
    )

    Email = Column(
        String(200),
        nullable=False
    )

    CreatedDate = Column(
        DateTime,
        nullable=False,
        server_default=func.sysutcdatetime()
    )
