from app.models import db, User, Product


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', full_name='Demo User', phone='3022536253', address='60 N. Cardinal Drive Richmond Hill, NY 11418')
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password', full_name='Marnie White', phone='3022536253', address='52 Brown Ave. Bensalem, PA 19020')
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password', full_name='Bobbie Brown', phone='3022536253',  address='37 E. Princess Rd. Evans, GA 30809')
    john = User(username='john', email='john@aa.io', password='password', full_name='John Smith',
                phone='3022536253',  address='37 E. Princess Rd. Evans, GA 30809')
    austin = User(username='austin', email='austin@aa.io', password='password', full_name='Austin Wang',
                  phone='3022536253',  address='37 E. Princess Rd. Evans, GA 30809')


    product1 = Product.query.get(1)
    product2 = Product.query.get(2)
    demo.favorite_products.append(product1)
    demo.favorite_products.append(product2)

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)    
    db.session.add(john)
    db.session.add(austin)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
