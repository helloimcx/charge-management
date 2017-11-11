# coding: utf-8
from .models import Phone, Worker
from .utils.exceptions import LogInWithoutAuthentication

PHONE = 'auth_phone'
WORKER = 'auth_worker'


def authenticate(phone, password):
    if phone is not None:
        try:
            phone_account = Phone.objects.get(phone=phone)
            if phone_account.check_user_password(password):
                phone_account.auth = True
                return phone_account, True
            else:
                return phone_account, False
        except Phone.DoesNotExist:
            return None, 'DoesNotExist'
        except Exception as e:
            return None, str(e)


def authenticate_worker(worker_id, password):
    if worker_id is not None:
        try:
            worker = Worker.objects.get(worker_id=worker_id)
            if worker.password == password:
                return worker, True
            else:
                return worker, False
        except Worker.DoesNotExist:
            return None, 'DoesNotExist'
        except Exception as e:
            return None, str(e)


def login(request, phone_account):
    if not hasattr(phone_account, 'auth'):
        raise LogInWithoutAuthentication

    if PHONE in request.session:
        request.session.flush()
    else:
        request.session.cycle_key()

    request.session[PHONE] = phone_account.phone
    phone_account.save()
    request.user = phone_account


def login_worker(request, worker):
    if WORKER in request.session:
        request.session.flush()
    else:
        request.session.cycle_key()

    request.session[WORKER] = worker.worker_id
    worker.save()
    request.user = worker


def logout(request):
    request.session.flush()


def is_login(request):
    return PHONE in request.session


def is_login_work(request):
    return WORKER in request.session
