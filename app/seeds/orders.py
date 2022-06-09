from app.models import db, Order, order


def seed_orders():
    order1 = Order(buyer_id=1, product_id=1, quantity=1,
                   order_number="ORDER_845963774787553", created_at="Mon Jun 06 2022 18:01:35 GMT-0700 (Pacific Daylight Time)")
    order2 = Order(buyer_id=1, product_id=2, quantity=2,
                   order_number="ORDER_140168683659859", created_at="Tue Jun 07 2022 20:33:17 GMT-0700 (Pacific Daylight Time)")
    order3 = Order(buyer_id=1, product_id=1, quantity=3,
                   order_number="ORDER_140168683659859", created_at="Tue Jun 07 2022 20:33:17 GMT-0700 (Pacific Daylight Time)")
    db.session.add(order1)
    db.session.add(order2)
    db.session.add(order3)

    db.session.commit()


def undo_orders():
    db.session.execute('TRUNCATE orders RESTART IDENTITY CASCADE;')
    db.session.commit()
