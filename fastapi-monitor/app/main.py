from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import socket
from database import SessionLocal, engine
from models import Base, SystemMetric

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/api/metrics/")
async def submit_metrics(
    cpu: float,
    memory: float,
    hostname: str = socket.gethostname(),
    db: Session = Depends(get_db),
):
    metric = SystemMetric(hostname=hostname, cpu_usage=cpu, memory_usage=memory)
    db.add(metric)
    db.commit()
    return {"status": "ok"}
