from app.models import db, Review


def seed_reviews():
    review1 = Review(content="super adorable", author_id=1,
                     product_id=1, created_at="Tue Jun 07 2022 20:33:17 GMT-0700 (Pacific Daylight Time)", updated_at="Tue Jun 07 2022 20:33:17 GMT-0700 (Pacific Daylight Time)")

    review2 = Review(content="beautiful sheet", author_id=1,
                     product_id=2, created_at="Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)", updated_at="Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)")

    db.session.add(review1)
    db.session.add(review2)

    db.session.commit()


def undo_reviews():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY CASCADE;')
    db.session.commit()
