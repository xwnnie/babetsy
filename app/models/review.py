from .db import db


class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.String, nullable=False)
    updated_at = db.Column(db.String, nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey(
        "products.id"), nullable=False)
    product = db.relationship("Product", back_populates="reviews")

    author_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), nullable=False)
    author = db.relationship("User", back_populates="reviews")

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "product_id": self.product_id,
            "author_id": self.author_id,
            "author_name": self.author.username,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
