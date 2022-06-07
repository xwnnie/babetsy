from app.models import db, Category

def seed_categories():
    clothing = Category(name="Clothing")
    furniture = Category(name="Furniture")
    toy = Category(name="Toy")
    bedding = Category(name="Bedding")
    bath = Category(name="Bath")
    decor = Category(name="Decor")

    db.session.add(clothing)
    db.session.add(furniture)
    db.session.add(bedding)
    db.session.add(bath)
    db.session.add(decor)
    db.session.add(toy)

    db.session.commit()


def undo_categories():
    db.session.execute('TRUNCATE categories RESTART IDENTITY CASCADE;')
    db.session.commit()
