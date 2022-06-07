from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', address='60 N. Cardinal Drive Richmond Hill, NY 11418')
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password', address='52 Brown Ave. Bensalem, PA 19020')
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password', address='37 E. Princess Rd. Evans, GA 30809')

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
