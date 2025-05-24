from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# SQLAlchemy Base class for model definitions
Base = declarative_base()


class SystemMetric(Base):
    __tablename__ = "system_metrics"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(
        String, default=datetime.now(tz=datetime.timezone.utc).isoformat()
    )
    hostname = Column(String, nullable=False)
    cpu_usage = Column(Float, nullable=False)
    memory_usage = Column(Float, nullable=False)
