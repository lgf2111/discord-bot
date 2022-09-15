from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


engine = create_engine("sqlite:///db.sqlite3", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Guild(Base):
    __tablename__ = "Guilds"
    id = Column(Integer, primary_key=True)
    prefix = Column(String, default=".")

    def __repr__(self) -> str:
        return f"<Guild(id={self.id}, prefix={self.prefix}"


if __name__ == "__main__":
    Base.metadata.create_all(engine)
