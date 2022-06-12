from app.models import db, Cart


def seed_carts():
    cart1 = Cart(buyer_id=1, product_id=5, quantity=1)
    cart2 = Cart(buyer_id=1, product_id=10, quantity=2)
    cart3 = Cart(buyer_id=1, product_id=12, quantity=3)
    db.session.add(cart1)
    db.session.add(cart2)
    db.session.add(cart3)

    db.session.commit()


def undo_carts():
    db.session.execute('TRUNCATE carts RESTART IDENTITY CASCADE;')
    db.session.commit()
