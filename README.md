<h1 align= "center" dir="auto"> Welcome to <a href="https://babetsy.herokuapp.com/">BABETSY</a>! </h1> <a name="top"> </a>
<h5 align= "center" dir="auto">
   <a href="https://babetsy.herokuapp.com/">» Live Link «</a>
</h5>
<h4 align= "center" dir="auto">
  <a href="https://github.com/xwnnie/babetsy">» Explore the Wiki «</a>
</h4>

BABETSY is a shopping website for users to browse and purchase baby products, such as baby clothing, furniture, bedding and toys. It's inspired by [Etsy](https://www.etsy.com/) in name and [H&M](https://www2.hm.com/en_us/index.html) in UX design. 

## Technologies Used
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Redux](https://img.shields.io/badge/redux-%23593d88.svg?style=for-the-badge&logo=redux&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

## Getting started
1. Clone this repository (only this branch)

   ```bash
   git clone https://github.com/xwnnie/babetsy.git
   ```

2. Install dependencies

      ```bash
      pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt
      ```

3. Create a **.env** file based on the example with proper settings for your
   development environment
4. Setup your PostgreSQL user, password and database and make sure it matches your **.env** file

5. Get into your pipenv, migrate your database, seed your database, and run your flask app

   ```bash
   pipenv shell
   ```

   ```bash
   flask db upgrade
   ```

   ```bash
   flask seed all
   ```

   ```bash
   flask run
   ```

6. To run the React App in development, checkout the [README](./react-app/README.md) inside the `react-app` directory.


# Features
## Authentication
Users can log into an existing account, sign up or test the site by clicking on the Demo User feature.
<img width="1461" alt="babetsy-login" src="https://user-images.githubusercontent.com/50897748/173940890-aa4eb3d2-3732-4854-916e-19ac421ac194.png">


## Home Page
<img width="1480" alt="babetsy-homepage" src="https://user-images.githubusercontent.com/50897748/173940420-3203da63-f778-4280-8162-c5150d921e59.png">
<img width="1489" alt="babetsy-homepage2" src="https://user-images.githubusercontent.com/50897748/173942850-483ae900-55bb-4144-a6ae-4a2b7af3ef74.png">


## Browse products and view product details
   * A user can view all product listings by clicking on a category on the category navigation bar.
   * A user can view details of a single product, such as name, image, price, description and reviews.
![product-detail](https://user-images.githubusercontent.com/50897748/173993790-eef9d083-c639-495e-8653-5195aca12c2b.gif)


## Add to Cart and Place Order
   * A logged in user can add a product to the shopping bag, update the quantity and remove the product from their shopping bag.
   * A logged in user can check out items in their shopping cart. On the checkout page, they can update their shipping address. 
   * After an order is placed, they can cancel it within one hour on order history page. 
   * A logged in user can view all placed orders in order history.
![checkout](https://user-images.githubusercontent.com/50897748/173993444-2355ca9c-f644-4dca-9cc6-49939bdb234e.gif)
  
  

## Reviews on purchased products
A logged in user can post, edit and delete review on purchased products
<img width="1479" alt="babetsy-reviews" src="https://user-images.githubusercontent.com/50897748/173942270-6832900a-9d43-4dd8-a832-9d28ee35f7b8.png">


## Favorites
A user can add and remove products from their favortie products page.
   * Clicking on the heart icon on a product image will add or remove the product from their favorites list
   * view all favorite products on the my-favorite page.
<img width="1481" alt="babetsy-favorites" src="https://user-images.githubusercontent.com/50897748/173942341-5c311d25-106d-4da1-957f-ade6a7702905.png">



## Search
A user can search for products by entering a keyword on search bar, which will redirect them to their search results page
<img width="1474" alt="babetsy-search" src="https://user-images.githubusercontent.com/50897748/173942543-ca621402-5b81-45de-9f47-02c42f72350e.png">


## Page Not Found
Accessing a path that does not exist will render a page not found and redirects the user to the homepage automatically after 3 seconds
<img width="1482" alt="babetsy-404" src="https://user-images.githubusercontent.com/50897748/173942681-10d65851-32fa-480e-aa31-00de6c9b2d3e.png">



[Back to top](#top)

