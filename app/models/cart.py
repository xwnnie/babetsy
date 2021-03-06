from .db import db

class Cart(db.Model):
    __tablename__ = "carts"

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey(
        "products.id"), nullable=False)
    product = db.relationship("Product", back_populates="cart")

    buyer_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), nullable=False)
    buyer = db.relationship("User", back_populates="cart")

    def to_dict(self):
        return {
            "id": self.id,
            "quantity": self.quantity,
            "product_id": self.product_id,
            "buyer_id": self.buyer_id
        }
