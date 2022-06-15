import { useSelector } from "react-redux";
import { useHistory, useLocation } from "react-router-dom";
import FaveHeart from "../FaveHeart";

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
    accessories: 7
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
    <div className="summer-container">
      <div className={"summer-header " + categoryName}>
        <div>{categoryName.toUpperCase()}</div>
      </div>
      <div className="products-container">
        {products.map((product) => (
          <div key={product.id} className="product-card">
            <FaveHeart productId={product.id} />
            <img
              src={product.image_url}
              alt={product.name}
              onClick={(e) => handleOnClick(product.id)}
            />
            <div
              className="products-page-price"
              onClick={(e) => handleOnClick(product.id)}
            >
              ${product.price}
            </div>
            <div
              className="products-page-name"
              onClick={(e) => handleOnClick(product.id)}
            >
              {product.name}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Products;
