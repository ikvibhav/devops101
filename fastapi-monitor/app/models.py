from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

# SQLAlchemy Base class for model definitions
Base = declarative_base()


def get_current_time() -> datetime:
    """Returns the current time in ISO format with UTC timezone."""
    return datetime.now(tz=timezone.utc)


class SystemMetric(Base):
    __tablename__ = "system_metrics"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(
        DateTime(timezone=True), default=get_current_time, nullable=False
    )
    hostname = Column(String, nullable=False)
    cpu_usage = Column(Float, nullable=False)
    memory_usage = Column(Float, nullable=False)
