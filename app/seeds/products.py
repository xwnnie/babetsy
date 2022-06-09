from unicodedata import category
from app.models import db, Product


def seed_products():
    product1 = Product(
        name="Bunny Critter Plush Nursery Rocker", price=99.99, quantity=1000000, description="Rock-a-bye baby in a super-cute plush rocker. This sweet seat is just their size and will give them hours of entertainment. Hop to it!", image_url="https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202223/0003/img19o.jpg", category_id=6)

    product2 = Product(name="Laney Floral Organic Crib Fitted Sheet", price=39.99, quantity=1000000,
                       description="With garden-fresh florals printed on crisp white organic cotton, our Laney Crib Fitted Sheet creates a pretty place to lay their head. This sheeting's percale weave is cozy while keeping cool to the touch, plus it's GOTS certified for a healthier night's sleep.", image_url="https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202211/0071/laney-floral-organic-crib-fitted-sheet-o.jpg", category_id=3)

    product3 = Product(name="2-piece Cotton Set", price=29.99, quantity=1000000, description="Baby Exclusive. Set with overall shorts and T-shirt in soft, organic cotton. Overall shorts in woven, crêped fabric with straps with adjustable buttoning at front, covered elastic at waistband and hems, and soft lining in cotton poplin. T-shirt in jersey with ribbed trim at neckline.",
                       image_url="https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F6d%2Fd4%2F6dd4a826936b30747906af157ebd109cf124b2aa.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B1%5D&call=url[file:/product/main]", category_id=1)
    
    product4 = Product(name="Harper 4-in-1 Convertible Crib",
                       price=1298.99, quantity=1000000, description="Make space in your bedroom or in their nursery for our elegant and refined Harper 4-in-1 Convertible Crib. Expertly crafted from sustainably sourced wood, this sturdy piece offers everything baby needs for years of sweet dreams. What's more, this adaptable design easily converts into a cozy toddler bed with the optional conversion kit. We love it paired with the matching nightstand and nursery dresser.", image_url="https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202222/0163/harper-4-in-1-convertible-crib-o.jpg", category_id=2)
    
    product5 = Product(
        name="Super Soft Animal Baby Hooded Towel & Washcloth Set", price=45.99, quantity=1000000, description="Let their favorite animals join in on their clean routine with these animal-inspired sets. Made of pure cotton terry with a cotton sateen binding, these luxuriously soft bathtime pieces are delicate and smooth on their skin.", image_url="https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202205/0179/super-soft-animal-baby-hooded-towel-washcloth-set-2-o.jpg", category_id=4)
    
    product6 = Product(name="Baby Lion Framed Art",
                       price=59.99, quantity=1000000, description="Turn their nursery walls into a gallery of art that inspires the imagination. Awash is soft neutrals against a white background, this lion brings playful, classic style to their space.", image_url="https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202209/0116/baby-lion-framed-art-o.jpg", category_id=5)
    product7 = Product(name="6-piece Jersey Set",
                       price=34.99, quantity=1000000,  description="et with three wrap-front bodysuits and three pairs of shorts in soft, organic cotton jersey. Short-sleeved bodysuits with snap fasteners at sides and at gusset. Shorts with elasticized waistband.", image_url="https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2Fc9%2Fe0%2Fc9e064c94396c8f4e6754ecce6999e49229ca1ae.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_baby_boy_setsoutfits%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]", category_id=1)
    
    product8 = Product(name="2-pack Jumpsuits with Zip", price=19.99, quantity=1000000,
                       description="Jumpsuits in soft organic cotton jersey. Zip at front with chin guard, and extending along one leg. Ribbing at neckline, cuffs, and hems.", image_url="https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2Fa9%2F94%2Fa99487db54ee405d57c476152a7f7f25fcb81fa0.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_baby_boy_clothing_nightwear%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]", category_id=1)
    
    product9 = Product(name="2-piece Set", price=17.99, quantity=1000000,
                       description="Baby Exclusive. Two-piece set with a top and leggings in soft, organic cotton jersey. Top with snap fastener on one shoulder, long raglan sleeves, and overlocked edges at cuffs and hem. Leggings with soft, elasticized waistband and overlocked edges at hems.", image_url="https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F8e%2F0c%2F8e0c6f71aeb2170b791b9acf05b0252537a5ec97.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_baby_girl_setsoutfits%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]", category_id=1)
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.add(product5)
    db.session.add(product6)
    db.session.add(product7)
    db.session.add(product8)
    db.session.add(product9)

    db.session.commit()


def undo_products():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()
