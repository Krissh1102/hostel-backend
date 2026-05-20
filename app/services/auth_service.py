from sqlalchemy.orm import Session

from app.database.models import Student

from app.schemas.auth_schema import StudentSignup

from app.utils.security import(
    hash_password,
    verify_password,
    create_access_token
)


def signup(
    db:Session,
    user:StudentSignup
):

    existing=db.query(Student).filter(
        Student.email==user.email
    ).first()

    if existing:
        return None

    new_user=Student(

        full_name=user.full_name,

        email=user.email,

        password=hash_password(
            user.password
        ),

        college=user.college,

        phone=user.phone
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user


def login(
    db:Session,
    email:str,
    password:str
):

    student=db.query(Student).filter(
        Student.email==email
    ).first()

    if not student:
        return None

    if not verify_password(
        password,
        student.password
    ):
        return None

    token=create_access_token(
        {"sub":student.email}
    )

    return token