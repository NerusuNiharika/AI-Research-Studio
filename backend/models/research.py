from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.database import Base


class Research(Base):

    __tablename__ = "research"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        nullable=False
    )

    topic = Column(
        String,
        nullable=False
    )

    report_path = Column(
        String,
        nullable=False
    )

    ppt_path = Column(
        String,
        nullable=False
    )