from .db import db

favorites = db.Table(
    "favorites",
    db.Column("product_id", db.Integer, db.ForeignKey(
        "products.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey(
        "users.id"), primary_key=True)
)
