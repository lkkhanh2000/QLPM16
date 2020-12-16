import hashlib
from app.models import UserRole, TaiKhoan
from app import db


def check_login(username, password, role=UserRole.ADMIN):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    user = TaiKhoan.query.filter(TaiKhoan.username == username,
                                 TaiKhoan.password == password,
                                 TaiKhoan.user_role == role).first()

    return user


def check_login_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    user = TaiKhoan.query.filter(TaiKhoan.username == username,
                                 TaiKhoan.password == password).first()

    return user


def get_user_by_id(user_id):
    return TaiKhoan.query.get(user_id)


def add_user(name, username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = TaiKhoan(name=name, username=username, password=password)
    try:
        db.session.add(u)
        db.session.commit()
        return True
    except Exception as ex:
        print(ex)
        return False

