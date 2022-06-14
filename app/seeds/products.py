from app.models import db, Product


def seed_products():
    products = [
        {
            "name": "Bunny Critter Plush Nursery Rocker", 
            "price": 99.99, 
            "quantity": 2, 
            "description": "Rock-a-bye baby in a super-cute plush rocker. This sweet seat is just their size and will give them hours of entertainment. Hop to it!", 
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202223/0003/img19o.jpg", 
            "category_id": 6     
        },
        {
            "name": "Laney Floral Organic Crib Fitted Sheet",
            "price": 39.99,
            "quantity": 1000,
            "description": "With garden-fresh florals printed on crisp white organic cotton, our Laney Crib Fitted Sheet creates a pretty place to lay their head. This sheeting's percale weave is cozy while keeping cool to the touch, plus it's GOTS certified for a healthier night's sleep.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202211/0071/laney-floral-organic-crib-fitted-sheet-o.jpg",
            "category_id": 3
        },
        {
            "name": "2-piece Cotton Set",
            "price": 29.99,
            "quantity": 1000,
            "description": "Baby Exclusive. Set with overall shorts and T-shirt in soft, organic cotton. Overall shorts in woven, crêped fabric with straps with adjustable buttoning at front, covered elastic at waistband and hems, and soft lining in cotton poplin. T-shirt in jersey with ribbed trim at neckline.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F6d%2Fd4%2F6dd4a826936b30747906af157ebd109cf124b2aa.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B1%5D&call=url[file:/product/main]",
            "category_id": 1
        },
        {
            "name": "Harper 4-in-1 Convertible Crib",
            "price": 1298.99,
            "quantity": 1000,
            "description": "Make space in your bedroom or in their nursery for our elegant and refined Harper 4-in-1 Convertible Crib. Expertly crafted from sustainably sourced wood, this sturdy piece offers everything baby needs for years of sweet dreams. What's more, this adaptable design easily converts into a cozy toddler bed with the optional conversion kit. We love it paired with the matching nightstand and nursery dresser.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202222/0163/harper-4-in-1-convertible-crib-o.jpg",
            "category_id": 2
        },
        {
            "name": "Baby Lion Framed Art",
            "price": 59.99,
            "quantity": 1000,
            "description": "Turn their nursery walls into a gallery of art that inspires the imagination. Awash is soft neutrals against a white background, this lion brings playful, classic style to their space.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202209/0116/baby-lion-framed-art-o.jpg",
            "category_id": 5
        },
        {
            "name": "6-piece Jersey Set",
            "price": 34.99,
            "quantity": 1000,
            "description": "Set with three wrap-front bodysuits and three pairs of shorts in soft, organic cotton jersey. Short-sleeved bodysuits with snap fasteners at sides and at gusset. Shorts with elasticized waistband.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2Fc9%2Fe0%2Fc9e064c94396c8f4e6754ecce6999e49229ca1ae.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_baby_boy_setsoutfits%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 1
        },
        {
            "name": "2-piece Set",
            "price": 17.99,
            "quantity": 1000,
            "description": "Baby Exclusive. Two-piece set with a top and leggings in soft, organic cotton jersey. Top with snap fastener on one shoulder, long raglan sleeves, and overlocked edges at cuffs and hem. Leggings with soft, elasticized waistband and overlocked edges at hems.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F8e%2F0c%2F8e0c6f71aeb2170b791b9acf05b0252537a5ec97.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_baby_girl_setsoutfits%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 1
        },
        {
            "name": "Storage Step Stools",
            "price": 109.99,
            "quantity": 1000,
            "description": "Kids feel more independent when they can reach counters, sinks and shelves on their own—and our step stool helps get them there. Built for sturdiness and smartly designed with hidden storage, our multifunctional stool is made to withstand years of use.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202222/0011/storage-step-stools-o.jpg",
            "category_id": 4
        },
        {
            "name": "Pat the Bunny Boxed Set",
            "price": 29.99,
            "quantity": 1000,
            "description": "Somebunny's going to love this sweet book collection! This boxed set includes the children’s classic Pat the Bunny, Pat the Puppy and Pat the Cat. Touch and feel elements and pull tabs invite children to explore these books on their own or to snuggle up and read along with you!",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202219/0141/pat-the-bunny-boxed-set-o.jpg",
            "category_id": 6
        },
        {
            "name": "Monique Lhuillier Blush Petal Canopy",
            "price": 199.99,
            "quantity": 1000,
            "description": "This canopy is inspired by voluminous ball gown skirts for a truly ethereal accent. Imagined with world-renowned fashion designer Monique Lhuillier, it brings her contemporary, whimsical and magical design aesthetic to your little one's space.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0243/monique-lhuillier-blush-petal-canopy-o.jpg",
            "category_id": 5
        },
        {
            "name": "Candlewick Dino Comforter & Shams",
            "price": 278.99,
            "quantity": 1000,
            "description": "With a parade of friendly dinosaur designs, our comforter and shams are a roaring good time. Created using a candlewick embroidery technique, the fluffy dinos add soft texture to the crisp cotton poplin's silky surface.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202209/0033/img64o.jpg",
            "category_id": 3
        },
        {
            "name": "Monique Lhuillier Tulle Tiny Dot Crib Skirt",
            "price": 129.99,
            "quantity": 1000,
            "description": "When only the most ethereal sleep space will do, this crib skirt is the ideal choice. It offers a soft, delicate touch with its dotted tulle drop and pure cotton lining. Mix and match it with other pieces from our Monique Lhuillier collaboration for an enchanting sleep space.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202221/0018/monique-lhuillier-tulle-tiny-dot-crib-skirt-o.jpg",
            "category_id": 3
        },
        {
            "name": "Muir Rocking Chair",
            "price": 999.99,
            "quantity": 1000,
            "description": "Cuddle time gets even cozier with our Muir Rocker, where elegant design elements combine in one extraordinarily relaxing chair. The deep seat, barrel back silhouette and supportive cushions make the experience all the more welcoming. Built of solid wood, the arched runners rock gently in an undulating movement that helps you relax and gets baby to drift off to sleep.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202213/0069/muir-rocker-o.jpg",
            "category_id": 2
        },
        {
            "name": "west elm x pbk Mid-Century Bassinet & Mattress Pad Set",
            "price": 449.99,
            "quantity": 1000,
            "description": "Keep your newborn nearby in this beautifully constructed bassinet made from solid eucalyptus wood. Featuring rounded spindles and angled legs, the frame is a nod to Mid-Century modern style.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202150/0403/west-elm-x-pbk-mid-century-bassinet-mattress-pad-set-o.jpg",
            "category_id": 2
        },
        {
            "name": "Dawson Scoop Convertible Crib",
            "price": 699.99,
            "quantity": 1000,
            "description": "Our Dawson Scoop Crib is a modern take on a classic style. Designed with curved railings to allow easy in-and-out accessibility, this versatile piece easily adapts from crib to cozy toddler bed. Most importantly, it was constructed from made-to-last materials to ensure safety, stability and longevity.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202222/0283/dawson-scoop-convertible-crib-o.jpg",
            "category_id": 2
        },
        {
            "name": "Sloan Tall Bookcase",
            "price": 399.99,
            "quantity": 1000,
            "description": "Our mid-century-inspired Sloan Collection successfully blends vintage and contemporary style to give their playroom a beautiful, timeless look. It features three sturdy shelves to hold their favorite stories and trinkets and boasts a two-toned element that ups the cool factor of their space for a sleek, modern look. Plus, it’s crafted with quality materials so it’s a stylish piece that lasts.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0131/sloan-tall-bookcase-o.jpg",
            "category_id": 2
        },
        {
            "name": "Wooden Nativity Set",
            "price": 59.99,
            "quantity": 1000,
            "description": "A charming take on the classic nativity scene, our 12-piece set is carefully crafted of sustainably sourced wood and kid-safe finishes. The stable doors open and close, making it great for both play and display.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202209/0026/wooden-nativity-set-1-o.jpg",
            "category_id": 6
        },
        {
            "name": "Activity Walker",
            "price": 89.99,
            "quantity": 1000,
            "description": "Toddlers will appreciate the extra stability of our sturdy wooden walker, with its wide handle and smooth wheels. When they get to their destination, it will keep them busy turning beads, rotating blocks and twirling the mirror until they’re ready to get up and go again.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202207/0016/activity-walker-o.jpg",
            "category_id": 6
        },
        {
            "name": "Plan Toys x pbk Bunny Sorting Bus",
            "price": 59.99,
            "quantity": 1000,
            "description": "All aboard the shape sorter school bus! With a bunny bus driver and a rope to pull it along, this whimsical toy from Plan Toys® introduces early math skills and problem-solving. Plan Toys® is the first company in the world to manufacture toys from reclaimed rubberwood to provide a more sustainable solution for playtime.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0169/plan-toys-x-pbk-bunny-sorting-bus-o.jpg",
            "category_id": 6
        },
        {
            "name": "Labradoodle Plush Play Mat",
            "price": 79.99,
            "quantity": 1000,
            "description": "At home or on the go, this cozy animal-inspired playmat provides the ultimate soft and safe tummy time for your baby. Made with a sweet face, huggable body and floppy ears, it'll keep them warm and secure all year round.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202210/0011/labradoodle-plush-play-mat-o.jpg",
            "category_id": 6
        },
        {
            "name": "PBK Learning Blocks",
            "price": 59.99,
            "quantity": 1000,
            "description": "One of our original products, these wooden blocks have the same rich character as the ones we had as kids.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0144/pbk-learning-blocks-o.jpg",
            "category_id": 6
        },
        {
            "name": "Alligator Safari Bath Set - Towels, Shower Curtain, Bath Mat",
            "price": 155.99,
            "quantity": 1000,
            "description": "Your animal fan will love spending bath time surrounded by the cool alligator motifs of this coordinated bath set.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202210/0010/alligator-safari-bath-set-towels-shower-curtain-bath-mat-o.jpg",
            "category_id": 4
        },
        {
            "name": "Disney Mickey Mouse Bath Mat",
            "price": 45.99,
            "quantity": 1000,
            "description": "Put a little magic under their feet with our Disney's Mickey Mouse bath mat. The iconic design is crafted of looped and tufted cotton for a super-plush feel with great absorbency and backed in nonslip latex for safety.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202224/0027/disney-mickey-mouse-bath-mat-o.jpg",
            "category_id": 4
        },
        {
            "name": "Shark Towel Collection",
            "price": 45.99,
            "quantity": 1000,
            "description": "Chomp! Add animal-inspired fun to their clean routine with this Shark Towel Collection. Crafted from pure cotton, they’re super absorbent and gentle on the skin.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0155/shark-towel-collection-o.jpg",
            "category_id": 4
        },
        {
            "name": "Birch Shelf",
            "price": 189.99,
            "quantity": 1000,
            "description": "With an element of forested fantasy, our woodsy, birch-inspired shelf is finished in a pretty white wash and looks great tucked in a corner of their playroom filled with their favorite tales, toys and treasures.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0028/birch-shelf-o.jpg",
            "category_id": 5
        },
        {
            "name": "Toy Ledge",
            "price": 79.99,
            "quantity": 1000,
            "description": "Simple lines and clean details lend contemporary and crisp style to their space. Organization will be a breeze with our sturdily constructed ledge perfect for storing their favorite books, games, and plush toys.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0043/toy-ledge-o.jpg",
            "category_id": 5
        },
        {
            "name": "White Campaign Pinboard",
            "price": 199.99,
            "quantity": 1000,
            "description": "Display all their favorite moments and memories with our classic White Campaign Pinboard. Perfect when hung above the dresser or by the bed, this pinboard is a smart addition to any space.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0058/white-campaign-pinboard-o.jpg",
            "category_id": 5
        },
        {
            "name": "Starry Night Carousel Nightlight",
            "price": 79.99,
            "quantity": 1000,
            "description": "Turn out the lights and watch the stars come to life. This adorable Starry Night Carousel Nightlight will usher them into sweet dreams and help them feel safe and secure if they wake up in the middle of the night. It also features music and eight different songs so they can rest easy.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202150/0023/starry-night-carousel-nightlight-o.jpg",
            "category_id": 5
        },
        {
            "name": "Disney Princess Cinderella Tabletop Night Light",
            "price": 99.99,
            "quantity": 1000,
            "description": "Give your little one a lamp fit for royalty. This delicate linen light features their favorite Disney Princess character Cinderella, beautifully embroidered and adorned with glistening beads. Super simple legs allow you to easily prop the piece on any surface in their room.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202207/0014/disney-princess-cinderella-tabletop-night-light-o.jpg",
            "category_id": 5
        },
        {
            "name": "Little Lights Train Lamp",
            "price": 240.99,
            "quantity": 1000,
            "description": "Help your little conductor get some rest after a hard day with this super cute Little Lights Train Lamp handmade from durable 100% natural pinewood.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202152/0009/little-lights-train-lamp-o.jpg",
            "category_id": 5
        },
        {
            "name": "Printed Baseball Jacket",
            "price": 24.99,
            "quantity": 1000,
            "description": "Baseball sweatshirt jacket in lightweight cotton fabric with a printed motif on chest and at back. Stand-up collar, snap fasteners at front, and contrasting sleeves with cuffs. Striped ribbing at collar and hem",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2Fac%2Fb5%2Facb50af6539a73ce6acd15b530029d47c5f85bba.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_newbornbaby_clothing_jumperssweatshirts_cardigans%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 1
        },
        {
            "name": "Disney Winnie the Pooh Organic Muslin Swaddle Set",
            "price": 64.99,
            "quantity": 1000,
            "description": "Bundle baby up with this cozy swaddle set, inspired by Disney Winnie the Pooh. Each blanket is made from breathable pure organic cotton muslin in charming prints inspired by Winnie the Pooh. Plus, they're OEKO-TEX® certified, which means they're verified to be safe from over 300 harmful substances, for a healthier naptime.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202222/0003/disney-winnie-the-pooh-organic-muslin-swaddle-set-1-o.jpg",
            "category_id": 3
        },
        {
            "name": "Flora Baby Bedding",
            "price": 164.99,
            "quantity": 1000,
            "description": "Make the nursery bloom with the cheerful colors of springtime flowers. Featuring painterly patterns and handstitched details, this coordinated bedding keeps them warm and cozy.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202204/0243/flora-baby-bedding-1-o.jpg",
            "category_id": 3
        },
        {
            "name": "Fuzzy Luxe Cable Knit Baby Blanket",
            "price": 39.99,
            "quantity": 1000,
            "description": "Always ready for sweater weather, our fuzzy luxe blanket is cute, cozy and classic. Perfect for snuggles, it’s made with a nylon/viscose blend that’s loved for its softness and breathability. The cable-knit design adds a dose of cozy style to any outing.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202222/0017/fuzzy-luxe-cable-knit-baby-blanket-1-o.jpg",
            "category_id": 3
        },
        {
            "name": "Emery Lion Baby Quilt",
            "price": 129.99,
            "quantity": 1000,
            "description": "This Emery Lion Quilt brings a cheery, colorful look to their crib. Woven from pure linen, this animal-inspired quilt features bright embroidery of so-cute lions and tigers.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202215/0094/emery-lion-baby-quilt-1-o.jpg",
            "category_id": 3
        },
        {
            "name": "Unicorn Shaped Pillow",
            "price": 34.99,
            "quantity": 1000,
            "description": "This magical unicorn pillow is all about cuddles. Perfect for naptime, reading time and playtime, they'll love cuddling up with this new friend.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202210/0057/unicorn-shaped-pillow-1-o.jpg",
            "category_id": 3
        },
        {
            "name": "Rainbow Unicorn Toddler Bedding",
            "price": 129.99,
            "quantity": 1000,
            "description": "Inspire their most magical dreams with our enchanting unicorn toddler bedding. The quilt is hand decorated with frolicking unicorns, vibrant manes and dazzling shooting stars. Crafted from soft pure cotton, it’s stitched over poly-cotton fill for lightweight warmth and lasting comfort. Pair with a unicorn sheet set or an organic white sheet set. Finish the look with a rainbow pillow.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0036/rainbow-unicorn-toddler-bedding-o.jpg",
            "category_id": 3
        },
        {
            "name": "Dump Truck Sound Pillow",
            "price": 49.99,
            "quantity": 1000,
            "description": "They'll rest easy with a hard working pillow. Featuring a cool dump truck design and fanciful embroidery, this fun pillow makes truck engine and trumpet horn sounds with just the push of a button.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202222/0002/dump-truck-sound-pillow-o.jpg",
            "category_id": 3
        },
        {
            "name": "west elm kids x pbk x Sarah Sherman Samuel Arches Twin Over Twin Bunk Bed",
            "price": 2799.99,
            "quantity": 1000,
            "description": "Their space will shape up nicely when you add this arched bunk bed. Its sturdy, expertly crafted wooden frame adds a hint of rustic charm, while its grand scale creates a striking silhouette. Great for smaller bedrooms, this piece also sleeps two for the space of one. Designed in collaboration with west elm and celebrated interiors expert, Sarah Sherman Samuel.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202208/0221/sarah-sherman-samuel-arches-twin-over-twin-bunk-bed-1-o.jpg",
            "category_id": 2
        },        
        {
            "name": "Camden House Bed",
            "price": 799.99,
            "quantity": 1000,
            "description": "Take blanket forts to the next level with our Camden House Bed. This piece is made from quality materials that last.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202222/0020/camden-house-bed-2-o.jpg",
            "category_id": 2
        },
        {
            "name": "Romantic Toy Bin",
            "price": 299.99,
            "quantity": 1000,
            "description": "Keep their little fingers safe and make clean-up fun with an open toy bin. Built-in cubbies put toys within reach and fixed dividers organize books, toys and everything else.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202204/0029/romantic-toy-bin-o.jpg",
            "category_id": 2
        },
        {
            "name": "Flounced Swimsuit",
            "price": 19.99,
            "quantity": 1000,
            "description": "Baby Exclusive. Fully lined swimsuit in textured fabric with narrow, ruffle-trimmed shoulder straps joined at back.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F00%2F12%2F001210accda41f157f56330043428bbf18dea141.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_girls_clothing_swimwear_swimsuits%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 1
        },
        {
            "name": "Poncho Towel",
            "price": 24.99,
            "quantity": 1000,
            "description": "Poncho towel in soft cotton terry with velour at outer side. Hood with appliqués and open sides with narrow ties.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=format%5Bwebp%5D%2Cquality%5B79%5D%2Csource%5B%2F46%2Fe9%2F46e9eba40396233017db6c363a10779f840d8def.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bhome_bathshower_accessories_towels_bathtowels%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url%5Bfile%3A%2Fproduct%2Fmain%5D",
            "category_id": 4
        },
        {
            "name": "Textured Swim Trunks",
            "price": 14.99,
            "quantity": 1000,
            "description": "Kids Exclusive. Textured swim trunks. Elasticized waistband with drawstring. Lined front.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F9b%2F20%2F9b207f9346d298acc751773abe51ce6b11f0c169.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 1
        },
        {
            "name": "Paper Straw Cooler Bag",
            "price": 17.99,
            "quantity": 1000,
            "description": "Semi-circular cooler bag in braided paper straw. Zipper and two handles at top, sun appliqué at one side, and insulating foil lining. Width 5 in. Height 6 3/4 in. Length 7 in.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F9f%2F81%2F9f815bd55d25023c252ae1753cecb5927e6c6442.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 7
        },
        {
            "name": "Cotton Sun Hat",
            "price": 6.99,
            "quantity": 1000,
            "description": "Sun hat in airy, woven cotton fabric. Wavy brim and ties underneath. Lined.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F6a%2F48%2F6a48ef3935fa9b631aae72ee194e2db352b4dd9b.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_baby_boy_accessories_hats%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 7
        },
        {
            "name": "Backpack",
            "price": 14.99,
            "quantity": 1000,
            "description": "Backpack in woven fabric. Adjustable shoulder straps, handle, and concealed zipper at top. Outer compartment and padded backplate. Depth 3 1/2 in. Width 7 in. Height 8 3/4 in.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2Fb6%2F9d%2Fb69dce625e903f931d5b067a015981731167c02d.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_baby_boy_accessories%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 7
        },
        {
            "name": "Strawberry-shaped Hat",
            "price": 7.99,
            "quantity": 1000,
            "description": "Lightly padded, strawberry-shaped hat in jersey. Felt appliqué at top and elasticized cuff. Lined.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F03%2F8d%2F038db0bb0962c7bd3328e253e8520b2115aa9c6b.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_baby_boy_accessories_hats%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 7
        },
    ]

    for p in products:
        db.session.add(Product(**p))

    db.session.commit()


def undo_products():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()
