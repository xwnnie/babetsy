from app.models import db, Order, order


def seed_orders():
    order1 = Order(buyer_id=1, product_id=1, quantity=1,
                   order_number="ORDER_845963774787553", created_at="2022-06-06T16:43:04.543Z")
    order2 = Order(buyer_id=1, product_id=2, quantity=2,
                   order_number="ORDER_140168683659859", created_at="2022-06-05T16:43:04.543Z")
    db.session.add(order1)
    db.session.add(order2)

    db.session.commit()


def undo_orders():
    db.session.execute('TRUNCATE orders RESTART IDENTITY CASCADE;')
    db.session.commit()