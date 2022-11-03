from new_app import db
from datetime import datetime

def dt_now():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

class Board(db.Model):
    __tablename__ = 'boards'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    created_date = db.Column(db.DateTime(timezone=True), default=dt_now())
    modification_date = db.Column(db.DateTime(timezone=True), default=dt_now(), onupdate=dt_now())
    status = db.Column(db.String(300), default='OPEN', nullable=False)
    task = db.relationship("Task", back_populates="board", uselist=False, cascade="all, delete")

    def __repr__(self):
        info: str = f'id: {self.id}\n' \
                    f'created_date: {self.created_date}\n' \
                    f'modification_date: {self.modification_date}\n' \
                    f'status: {self.status}\n'
        return info


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    created_date = db.Column(db.DateTime(timezone=True), default=dt_now())
    modification_date = db.Column(db.DateTime(timezone=True), default=dt_now(), onupdate=dt_now())
    execution_status = db.Column(db.Boolean, default=False, nullable=False)
    text = db.Column(db.String(300), nullable=False)
    board_fk = db.Column(db.Integer, db.ForeignKey('boards.id', ondelete='CASCADE'))
    board = db.relationship('Board', back_populates='task')

    def __repr__(self):
        info: str = f'id: {self.id}\n' \
                    f'created_date: {self.created_date}\n' \
                    f'modification_date: {self.modification_date}\n' \
                    f'execution_status: {self.execution_status}\n' \
                    f'text: {self.text}\n'
        return info
