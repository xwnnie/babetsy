import { useSelector } from "react-redux";
import { useHistory, useLocation } from "react-router-dom";
import { useEffect } from "react";

import "./index.css";

const Products = () => {
  const history = useHistory();
  useLocation(); //cause re-render after path changes

  const categories = {
    clothing: 1,
    furniture: 2,
    bedding: 3,
    bath: 4,
    decor: 5,
    toys: 6,
  };
  const categoryName = history.location.pathname.slice(1);
  const categoryId = categories[categoryName];

  const productsObj = useSelector((state) => state.products);
  let products = Object.values(productsObj);
  products = products.filter((product) => product.category_id === categoryId);

  const handleOnClick = (id) => {
    history.push(`/products/${id}`);
  };
  return (
    <div>
      {/* <h1>{categoryName}</h1> */}
      <div className="products-container">
        {products.map((product) => (
          <div
            key={product.id}
            onClick={(e) => handleOnClick(product.id)}
            className="product-card"
          >
            <img src={product.image_url} alt={product.name} />
            <div>${product.price}</div>
            <div>{product.name}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Products;
