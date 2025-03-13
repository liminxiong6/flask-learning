from datetime import datetime

from db import db


class TokenBlocklist(db.Model):
    __tablename__ = "token_blocklist"
    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    jti = db.Column(
        db.String(36),
        unique=True,
    )
    revoked_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
    expires_at = db.Column(db.DateTime, nullable=False)
