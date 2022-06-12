from .db import db
from .favorite import favorites
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)

    reviews = db.relationship("Review", back_populates="author")

    orders = db.relationship("Order", back_populates="buyer")
    cart = db.relationship("Cart", back_populates="buyer")

    favorite_products = db.relationship(
        "Product", back_populates="favored_by", secondary=favorites)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'address': self.address,
            'full_name': self.full_name,
            'phone': self.phone,
            'reviews': {review.id: review.to_dict() for review in self.reviews},
            'orders': {},
            'favorite_products': [product.id for product in self.favorite_products]
        }
