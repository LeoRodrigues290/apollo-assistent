from datetime import datetime
from .models import Task, Schedule, Routine, Exercise, Finance
from sqlalchemy.orm import Session

class ChatbotService:
    def __init__(self, db: Session):
        self.db = db

    def get_weekly_meetings(self, user_id: str):
        today = datetime.now()
        end_of_week = today + timedelta(days=7)
        meetings = self.db.query(Schedule).filter(
            Schedule.user_id == user_id,
            Schedule.start_time.between(today, end_of_week)
        ).all()
        return meetings

    # Outras funções para interagir com as tabelas...
