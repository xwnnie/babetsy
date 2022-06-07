from app.models import db, Product

def seed_products():
    product1 = Product(
        name="Bunny Critter Plush Nursery Rocker", price=99.99, quantity=1000000, description="Rock-a-bye baby in a super-cute plush rocker. This sweet seat is just their size and will give them hours of entertainment. Hop to it!", image_url="https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202223/0003/img19o.jpg", category_id=6)

    product2 = Product(name="Laney Floral Organic Crib Fitted Sheet", price=39, quantity=1000000,
                       description="With garden-fresh florals printed on crisp white organic cotton, our Laney Crib Fitted Sheet creates a pretty place to lay their head. This sheeting's percale weave is cozy while keeping cool to the touch, plus it’s GOTS certified for a healthier night's sleep.", image_url="https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202211/0071/laney-floral-organic-crib-fitted-sheet-o.jpg", category_id=3)
    
    db.session.add(product1)
    db.session.add(product2)

    db.session.commit()


def undo_products():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()
