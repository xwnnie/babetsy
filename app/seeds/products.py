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
            "name": "Babyletto Lolly 3-in-1 Convertible Crib",
            "price": 449.99,
            "quantity": 1000,
            "description": "The Babyletto® Lolly Convertible Crib is a stylish space-saving solution for any modern nursery. With thought-out details like natural spindles and feet and a sturdy pinewood frame, this sleek crib is perfect for the smallest of spaces. Plus, it includes a toddler rail to transform from a crib to toddler bed for easy conversion.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202222/0068/babyletto-lolly-3-in-1-convertible-crib-o.jpg",
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
            "name": "Quinn White Washed Hamper",
            "price": 125.99,
            "quantity": 1000,
            "description": "With a classic drum shape and lid, this woven hamper keeps dirty clothes stylishly contained.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202223/0017/quinn-white-washed-hamper-o.jpg",
            "category_id": 4
        },
        {
            "name": "Splish Splash Bath Mat",
            "price": 40.99,
            "quantity": 1000,
            "description": "Give bath time a bright accent with an-ultra splashy quote and a soft and absorbent mat.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0062/splish-splash-bath-mat-o.jpg",
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
            "name": "Modern House Bookcase",
            "price": 599.99,
            "quantity": 1000,
            "description": "Perfect for their bedroom or play space, our minimalist bookcase creates the perfect home for all their favorite things. With three shelves divided into both small and large cubbies, there’s room for everything from toys to books and more.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202225/0012/modern-house-bookcase-o.jpg",
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
        {
            "name": "Dress and Accessory",
            "price": 29.99,
            "quantity": 1000,
            "description": "Dress in woven fabric with a matching hairband. Dress with buttons at back, short puff sleeves with concealed elastic at cuffs, and gathered seam above a flared skirt. Lining in woven cotton fabric. Elasticized hairband with decorative flowers.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F21%2F77%2F21771d36e85deebf6421483a303fef9b41387186.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 1
        },
        {
            "name": "2-pack Ribbed Shirts",
            "price": 14.99,
            "quantity": 1000,
            "description": "Baby Exclusive. Short-sleeved shirts in soft, ribbed, cotton jersey with a button placket. Scalloped edges at neckline, button placket, and cuffs.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2Fc0%2F98%2Fc0989b5a341cba3cbcdea6796f012a0a91026dd7.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_baby_boy_clothing_tshirtsshirts_tshirts%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 1
        },
        {
            "name": "3-pack Jumpsuits with Zipper",
            "price": 29.99,
            "quantity": 1000,
            "description": "Long-sleeved jumpsuits in soft cotton jersey with a zip at front and along one leg. Covered feet.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F4b%2F20%2F4b20a8758f7faca8fcbc78411d1a415def5ce5ef.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 1
        },
        {
            "name": "2-pack cotton jersey dresses",
            "price": 14.99,
            "quantity": 1000,
            "description": "Two wide, sleeveless dresses in soft cotton jersey, one with an all-over print. Narrow cut at the top with narrow shoulder straps, and gathered tiers on the skirt.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2Ff0%2Fda%2Ff0da4ddca6a645373869249befe3a7e2e57f1079.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 1
        },
        {
            "name": "2-piece cotton set",
            "price": 14.99,
            "quantity": 1000,
            "description": "Set with a blouse and pair of shorts in a cotton weave. Blouse with a round neckline, two buttons at the top and a flounced seam at the top that continues over the shoulders. Long sleeves with soft, narrow elastication at the cuffs. Unlined. Shorts with soft, covered elastication at the waist. Unlined.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F45%2F45%2F4545bbd907e91ebf43842085ef614e0e31666a40.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 1
        },
        {
            "name": "2-pack Jumpsuits with Zip",
            "price": 19.99,
            "quantity": 1000,
            "description": "Jumpsuits in soft organic cotton jersey. Zip at front with chin guard, and extending along one leg. Ribbing at neckline, cuffs, and hems.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2Fa9%2F94%2Fa99487db54ee405d57c476152a7f7f25fcb81fa0.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_baby_boy_clothing_nightwear%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 1
        },
        {
            "name": "3-pack Ribbed Hats with Ears",
            "price": 14.99,
            "quantity": 1000,
            "description": "Ribbed hats in soft cotton jersey with ears and foldover cuff.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2Fe8%2F41%2Fe8411ba8dd175dd1ee480141a9f53f88019073c8.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_baby_boy_accessories_hats%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 7
        },
        {
            "name": "2-piece Set",
            "price": 14.99,
            "quantity": 1000,
            "description": "Fleece-lined set with a hat and mittens in a soft cable knit. Hat with faux fur pompom at top, small faux suede appliqué at front, earflaps, and ties under chin. Mittens with ribbed cuffs. Sizes 0-2 months and 2-6 months without thumbs.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F0f%2F99%2F0f99de77c0dea69ee71af342aa7a26be0b67cff4.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_newborn_sets%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B1%5D&call=url[file:/product/main]",
            "category_id": 7
        },
        {
            "name": "3-pack Triangular Scarves",
            "price": 14.99,
            "quantity": 1000,
            "description": "Double-layered triangular scarves in soft, organic cotton jersey. Snap fastener at back of neck.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2Fc2%2F01%2Fc20189773bd61726e1d6b1a50c9f0a2ada2c9300.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 7
        },
        {
            "name": "Cotton Hat",
            "price": 12.99,
            "quantity": 1000,
            "description": "Baby Exclusive. Hat in soft cotton poplin with ruffle trim at front, elastic at back, and ties under chin. Cotton lining.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F99%2F33%2F99339d270db178756a9b51727b665ea2494c6f2f.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 7
        },
        {
            "name": "2-pack Cotton Hats",
            "price": 12.99,
            "quantity": 1000,
            "description": "Hats in double-layers of soft cotton jersey. One hat with a printed pattern.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F42%2Fbf%2F42bfbdd460ad4c5de653dc20fa7ed383be236d31.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 7
        },
        {
            "name": "Swim Cap UPF 50",
            "price": 12.99,
            "quantity": 1000,
            "description": "Swim cap UV-protective material with a visor at front. Flap at back to protect back of neck. UPF 50.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F03%2F60%2F03601d4f75c908ccdfd2ae22ee6fd85e54e72be3.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_babygirl_swimwear%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 7
        },
        {
            "name": "Disney Princess Towel Collection",
            "price": 62.99,
            "quantity": 1000,
            "description": "Inspire bathtime fun with fluffy towels featuring their favorite Disney Princess characters. Super plush, soft and absorbent, they’re woven from pure cotton, embroidered with three iconic designs and finished in a soft pink hue.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0809/disney-princess-towel-collection-4-o.jpg",
            "category_id": 4
        },
        {
            "name": "Super Soft Lamb Baby Hooded Towel And Washcloth",
            "price": 45.99,
            "quantity": 1000,
            "description": "Let a sweet animal friend join in on their clean routine with this lamb-inspired set. Made from pure cotton, these luxuriously soft bath time pieces are absorbent and smooth on their skin.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202208/0036/super-soft-lamb-baby-hooded-towel-and-washcloth-o.jpg",
            "category_id": 4
        },
        {
            "name": "Rainbow Bath Accessories",
            "price": 39.99,
            "quantity": 1000,
            "description": "Pastel stripes in the colors of the rainbow give their bathroom a cheerful look. Sized for little hands, our bath accessories are lightweight, shatter-resistant and made to last.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0247/rainbow-bath-accessories-o.jpg",
            "category_id": 4
        },
        {
            "name": "Tassel Bath Mat",
            "price": 39.99,
            "quantity": 1000,
            "description": "Brighten up the room with a colorful spot for drying off. Extra absorbent and soft underfoot, our exclusive pink bath mat features multicolored tassels along the border turning a bathroom must-have into a style statement.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202208/0095/tassel-bath-mat-o.jpg",
            "category_id": 4
        },
        {
            "name": "6-pack Triangular Scarves",
            "price": 19.99,
            "quantity": 1000,
            "description": "Double-layered triangular scarves in soft organic cotton jersey with adjustable snap fastening at back of neck.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F84%2F5d%2F845dccec39769939f9c470d820982fd80bb503be.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 7
        },
        {
            "name": "2-pack Cotton Turbans",
            "price": 9.99,
            "quantity": 1000,
            "description": "Turbans in soft cotton jersey with a decorative gathered detail at front.",
            "image_url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F22%2Fb7%2F22b79e258b1369f890cc3722f1fd3a67baf86493.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5Bkids_baby_girl_accessories_hats%5D%2Ctype%5BDESCRIPTIVESTILLLIFE%5D%2Cres%5Bm%5D%2Chmver%5B2%5D&call=url[file:/product/main]",
            "category_id": 7
        },
        {
            "name": "Peanuts® Shower Curtain",
            "price": 79.99,
            "quantity": 1000,
            "description": "Snoopy® soaking in a sudsy bath decorate this playful Peanuts® Shower Curtain. It’ll add some fun to their bathtime or showertime routine. Plus, keyhole buttons make for easy hanging.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0092/peanuts-shower-curtain-o.jpg",
            "category_id": 4
        },
        {
            "name": "Jungle Bath Squirties Set",
            "price": 24.99,
            "quantity": 1000,
            "description": "Make bath time fun with playful jungle animals. Bound to be a bathtub favorite, these colorful floating animals are easy to fill up and squirt.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0151/jungle-bath-squirties-set-o.jpg",
            "category_id": 4
        },
        {
            "name": "Shark Shower Curtain",
            "price": 65.99,
            "quantity": 1000,
            "description": "Bath time becomes extra adventurous with this array of blue-hued sharks and schools of sweet fish.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0224/shark-shower-curtain-o.jpg",
            "category_id": 4
        },
        {
            "name": "Disney Winnie The Pooh Crib Mobile",
            "price": 69.99,
            "quantity": 1000,
            "description": "Their dreams will be as sweet as honey when Disney's Winnie the Pooh watches over the crib. The adorable bear, plush clouds and gentle honeybees rotate overhead while a soothing lullaby plays.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202204/0030/disney-winnie-the-pooh-crib-mobile-o.jpg",
            "category_id": 5
        },
        {
            "name": "Ceramic Rainbow Nightlight",
            "price": 39.99,
            "quantity": 1000,
            "description": "Help them drift off to dreamland with this rainbow-shaped nightlight. It emits a soft glow and is a comforting addition to their sleep space.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202204/0026/ceramic-rainbow-nightlight-o.jpg",
            "category_id": 5
        },
        {
            "name": "Chasing Paper Wallpaper Puppy Pile",
            "price": 50.99,
            "quantity": 1000,
            "description": "Puppies on peel-and-stick wallpaper? There's nothing to not love here! This fabric wallpaper sticks to nearly any surface and is fade-resistant to last through the years. And when you’re ready to remove, it comes off easily with no mess.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202210/0026/chasing-paper-wallpaper-puppy-pile-o.jpg",
            "category_id": 5
        },
        {
            "name": "Minted® Vintage Airplane Personalized Wall Art by Jessie Steury",
            "price": 78.99,
            "quantity": 1000,
            "description": "This personalizable art piece by Jessie Steury is ready to take off and land in their space. Minted crowdsources artwork from a global community of artists, the public votes and we select winners exclusively for Pottery Barn Kids. By supporting this collection, you're helping independent artists across the world.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202205/0065/minted-vintage-airplane-wall-art-by-jessie-steury-o.jpg",
            "category_id": 5
        },
        {
            "name": "Ava Regency Dresser",
            "price": 1299.99,
            "quantity": 1000,
            "description": "Inspired by the glamorous furniture from Hollywood's Golden Age, the Ava Regency Collection is a classic for a reason. Artful curves, appliqué trim inserts and tapered feet are masterfully crafted throughout the collection to bring a cohesive look to the room. Each piece is constructed from made-to-last materials to ensure safety, stability and longevity.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202207/0211/ava-regency-dresser-o.jpg",
            "category_id": 2
        },
        {
            "name": "Babyletto Hudson 3-in-1 Convertible Crib",
            "price": 499.99,
            "quantity": 1000,
            "description": "The Babyletto® Hudson Convertible Crib is a stylish solution for any modern nursery. Boasting a mid-century design with thought-out details like rounded spindles and feet and a sturdy pinewood frame, this sleek crib is perfect for every space. Plus, it includes a toddler rail to transform from a crib to toddler bed for easy conversion.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202222/0163/babyletto-hudson-3-in-1-convertible-crib-o.jpg",
            "category_id": 2
        },
        {
            "name": "Camden Convertible Crib",
            "price": 799.99,
            "quantity": 1000,
            "description": "Designed with clean lines, our Camden Convertible Crib makes a modern statement in their room, and it converts to a toddler bed as your child grows. Built to last from quality materials like solid New Zealand pine, it offers safety, longevity and enduring style. Plus, it’s GREENGUARD Gold Certified to contribute to cleaner indoor air for a safer sleep space.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202222/0162/camden-convertible-crib-o.jpg",
            "category_id": 2
        },
        {
            "name": "Modern Farmhouse Extra-Wide Dresser & Topper Set",
            "price": 1499.99,
            "quantity": 1000,
            "description": "Natural wood, clean lines and slatted details come together in our Modern Farmhouse Collection, a rustic-meets-contemporary design concept that grows with your little ones. This nursery set is an all-in-one storage and changing solution. The dresser boasts six drawers – all secured on waxed wooden gliders – for tucking in clothes, fresh linens and more; the topper keeps essentials within easy reach. This collection is built to our high, exacting standards to ensure safety, stability and longevity.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202218/0187/modern-farmhouse-extra-wide-dresser-topper-set-o.jpg",
            "category_id": 2
        },
        {
            "name": "Disney Winnie the Pooh Organic Crib Fitted Sheet Bundle - Set of 2",
            "price": 88.99,
            "quantity": 1000,
            "description": "Update their sleep space with charming illustrations from Disney Winnie the Pooh. Made from GOTS certified organic cotton, this set includes two crib fitted sheets to keep your little Pooh Bear warm and cozy through the night.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202205/0002/disney-winnie-the-pooh-picture-perfect-organic-crib-fitted-o.jpg",
            "category_id": 3
        },
        {
            "name": "Star Wars™ The Mandalorian™ Grogu™ Heirloom Baby Blanket",
            "price": 75.99,
            "quantity": 1000,
            "description": "It's wise to bundle your precious cargo in our cozy Grogu™ Heirloom Baby Blanket. Great for snuggling at home or strolling across the galaxy. It’s knitted from exceptionally warm acrylic yarn and backed in silky-soft vela plush.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202205/0086/star-wars-the-mandalorian-grogu-heirloom-baby-blanket-1-o.jpg",
            "category_id": 3
        },
        {
            "name": "Plan Toys x pbk Punch Drop",
            "price": 45.99,
            "quantity": 1000,
            "description": "This superfun punch drop toy from Plan Toys® develops your little one’s hand-eye coordination. They can hammer the balls into the box and watch them roll out for maximum fun! Plan Toys® is the first company in the world to manufacture toys from reclaimed rubberwood to provide a more sustainable solution for playtime.",
            "image_url": "https://assets.pkimgs.com/pkimgs/ab/images/dp/wcm/202212/0043/plan-toys-x-pbk-punch-drop-o.jpg",
            "category_id": 6
        },
    ]

    for p in products:
        db.session.add(Product(**p))

    db.session.commit()


def undo_products():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()
