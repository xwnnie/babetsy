from app.models import db, Review


def seed_reviews():
    reviews = [
        {
            "content": "This item is really cute but it was a bit hard to put together. It does come with everything you need to assemble. I was having issues trying to line up the holes and putting the screws in.",
            "author_id": 1,
            "product_id": 1, 
            "created_at": "Tue Jun 07 2022 20:33:17 GMT-0700 (Pacific Daylight Time)", 
            "updated_at": "Tue Jun 07 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        }, 
        {
            "content": "We bought these for our newborn and they're really great sheets.",
            "author_id": 1,
            "product_id": 2,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "I got this last minute due to a photoshoot! And this was literally my only choice due next day shipping. I must say so happy I got this so perfect!",
            "author_id": 2,
            "product_id": 3,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "We needed a crib within the last month of my pregnancy... Our diy project was falling apart.. But this turned out to be great! We were pleasantly surprised at how much we love this crib.",
            "author_id": 3,
            "product_id": 4,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "This item is really cute but it was a bit hard to put together. It does come with everything you need to assemble. I was having issues trying to line up the holes and putting the screws in. The were going in at an angle.",
            "author_id": 2,
            "product_id": 4,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "Sooo cute. Put in my newborn nursery. Highly recommended!!!",
            "author_id": 2,
            "product_id": 5,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "This set is amazing for the price! You do need to know that once you wash it, it will shrink. I bought it for our neighbor's newborn and it was too big for him at first until it was washed.",
            "author_id": 4,
            "product_id": 6,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "This was very beautiful. The onzie shirt though doesn't stretch and it wasn't a good material. But the botom is very beautiful. Overall good one for the price",
            "author_id": 5,
            "product_id": 7,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "Durable. Using it for potty training/washing hands. My daughter loves it. She wants to wash her hands and brush her teeth throughout the day just so she can use it! Cute personalization!",
            "author_id": 2,
            "product_id": 8,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "This is a great set of books. Packaged nicely and pricing very reasonable for the trio. The original Pat the Bunny is the best but other two books are cute as well.",
            "author_id": 3,
            "product_id": 9,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "I really love this canopy is so cute and we customized putting some lights on. My daughter just love it.",
            "author_id": 4,
            "product_id": 10,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "It's exactly what I expected, exactly what we wanted for our baby's room! For crib bedding it's a little pricy, but we feel it's worth it anyway :)",
            "author_id": 5,
            "product_id": 11,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "I love the look of this crib skirt in my little girls nursery. It's very feminine and fits great on her crib. It lines perfectly to right above the floor. ",
            "author_id": 2,
            "product_id": 12,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },        
        {
            "content": "I love it. Looks cute in my babies nursery",
            "author_id": 3,
            "product_id": 12,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "I just love this item. The little seat makes it easy to strap my grandbaby in. It is so adorable. Very sturdy. Worth the money.",
            "author_id": 4,
            "product_id": 13,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "This is a nice and sturdy crib that was easy to set up. I recommend two people setting it up. It is a solid wood frame that came nicely packaged. There are 3-4 hieght settings for the mattress.",
            "author_id": 4,
            "product_id": 14,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "Beautiful crib, instructions were easy to follow. Put it together by myself in about 90 minutes. Would have been quicker with help! Very sturdy. Arrived quicker than estimated ship date. ",
            "author_id": 5,
            "product_id": 15,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "Bought this for my daughters room. It's perfect. It's takes up little space and she can now see the covers to all of her books. Highly recommended.",
            "author_id": 2,
            "product_id": 16,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "I'm so glad I could add a few pieces after purchasing the original set so many years ago!",
            "author_id": 3,
            "product_id": 17,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "This walker is a great value for the price. It’s lightweight and has interesting toys attached.",
            "author_id": 4,
            "product_id": 18,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "This was my granddaughters most favorite. I find that toys have an attention span of only. a few weeks when it comes to education and this one took the cake for every day use. She asked for it every time she came to visit her Mina. ",
            "author_id": 5,
            "product_id": 19,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },        
        {
            "content": "I like this because is super soft! And easy to clean! Y but it for my baby girl she is 2 months and she love to be there and is warm to ! And because her room is everything with elefant match with everything!",
            "author_id": 2,
            "product_id": 20,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },
        {
            "content": "I thought this was a toy that was to advanced for my two 15 month old granddaughters, but they sat down and started playing with it. Within a few days they were turning the pieces and getting them on some of the pegs and each day I see progress.",
            "author_id": 3,
            "product_id": 21,
            "created_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)",
            "updated_at": "Tue Jun 08 2022 20:33:17 GMT-0700 (Pacific Daylight Time)"
        },



    ]
   
    for p in reviews:
        db.session.add(Review(**p))

    db.session.commit()

    db.session.commit()


def undo_reviews():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY CASCADE;')
    db.session.commit()
