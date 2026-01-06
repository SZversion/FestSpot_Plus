from sqlmodel import SQLModel, create_engine, Session

MYSQL_URL = "mysql://root:1q2w3e4r!@localhost:3306/festspot_db"

engine = create_engine(
    MYSQL_URL,
    echo=True,  # 개발용 — 쿼리 확인 가능
)


def get_session():
    with Session(engine) as session:
        yield session
