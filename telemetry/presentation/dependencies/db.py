from fastapi import Depends
from sqlalchemy.orm import Session

from infrastructure.postgres.log import LogRepo
from infrastructure.postgres.device import DeviceInfoRepo
from infrastructure.postgres.session import SessionMaker


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


def get_log_repo(session: Session = Depends(get_session)):
    return LogRepo(session=session)

def get_device_info_repo(session: Session = Depends(get_session)):
    return DeviceInfoRepo(session=session)
