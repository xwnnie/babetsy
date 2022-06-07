from .db import db
from .favorite import favorites

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    category = db.relationship("Category", back_populates="product")

    reviews = db.relationship("Review", back_populates="product")

    orders = db.relationship("Order", back_populates="product")

    favored_by = db.relationship(
        "User", back_populates="favorite_products", secondary=favorites)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity,
            "image_url": self.image_url,
            "category_id": self.category_id
        }