from app.models import db, Order, order


def seed_orders():
    order1 = Order(buyer_id=1, product_id=1, quantity=1, total=99.99, full_name="Demo User", phone="3022536253", address="60 N. Cardinal Drive Richmond Hill, NY 11418",
                   order_number="ORDER_845963774787553", created_at="Mon Jun 06 2022 18:01:35 GMT-0700 (Pacific Daylight Time)")
    order2 = Order(buyer_id=1, product_id=2, quantity=2, total=379.95, full_name="Demo User", phone="3022536253", address="562 Whitemarsh St. Bettendorf, IA 52722",
                   order_number="ORDER_140168683659859", created_at="Tue Jun 07 2022 20:33:17 GMT-0700 (Pacific Daylight Time)")
    order3 = Order(buyer_id=1, product_id=1, quantity=3, total=379.95, full_name="Demo User", phone="3022536253", address="562 Whitemarsh St. Bettendorf, IA 52722",
                   order_number="ORDER_140168683659859", created_at="Tue Jun 07 2022 20:33:17 GMT-0700 (Pacific Daylight Time)")
    db.session.add(order1)
    db.session.add(order2)
    db.session.add(order3)

    db.session.commit()


def undo_orders():
    db.session.execute('TRUNCATE orders RESTART IDENTITY CASCADE;')
    db.session.commit()
