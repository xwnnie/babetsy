from app.models import db, Review


def seed_reviews():
    review1 = Review(content="super adorable", author_id=1, product_id=1)

    db.session.add(review1)

    db.session.commit()


def undo_reviews():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY CASCADE;')
    db.session.commit()
