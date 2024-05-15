from dataclasses import dataclass
from enum import Enum
from Data.base import db

@dataclass
class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id  = db.Column(db.String)
    data = db.Column(db.PickleType,nullable=False)
