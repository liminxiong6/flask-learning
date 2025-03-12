from db import db
from datetime import datetime


class TokenBlocklist(db.Model):
    __tablename__ = "token_blocklist"
    id = db.Column(db.Integer, primary_key=True, dump_only=True)
    jti = db.Column(db.String(36), unique=True, nullable=False, load_only=True)
    revoked_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
