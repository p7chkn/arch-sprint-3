from fastapi import Depends
from sqlalchemy.orm import Session

from application.device.usecases.interfaces import DeviceRegisterRepoInterface
from infrastructure.postgres.devices import DeviceRepo
from infrastructure.postgres.session import SessionMaker, engine


def get_session() -> Session:
    db = SessionMaker()

    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def get_device_repo(session: Session = Depends(get_session)):
    return DeviceRepo(session=session)