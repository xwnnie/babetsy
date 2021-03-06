from .db import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    order_number = db.Column(db.String(100), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.String, nullable=False)
    total = db.Column(db.String(20), nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey(
        "products.id"), nullable=False)
    product = db.relationship("Product", back_populates="orders")

    buyer_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), nullable=False)
    buyer = db.relationship("User", back_populates="orders") 

    def to_dict(self):
        return {
            "id": self.id,
            "quantity": self.quantity,
            "product_id": self.product_id,
            "buyer_id": self.buyer_id,
            "order_number": self.order_number,
            "created_at": self.created_at,
            'phone': self.phone,
            'full_name': self.full_name,
            'address': self.address,
            'total': self.total
        }
