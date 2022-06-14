import { useSelector } from "react-redux";
import { useHistory, useLocation } from "react-router-dom";
import FaveHeart from "../FaveHeart";

import "./index.css";

const Summer = () => {
    const history = useHistory();

  const productsObj = useSelector((state) => state.products);
  let products = Object.values(productsObj);
  const summerProducts = [42, 43, 44, 45, 46, 47, 48, 60];
  products = products.filter((product) => summerProducts.includes(product.id));

  const handleOnClick = (id) => {
    history.push(`/products/${id}`);
  };
  return (
    <div className="summer-container">
      <div className="summer-header"><div>SUMMER COLLECTION</div></div>
      <div className="products-container">
        {products.map((product) => (
          <div key={product.id} className="product-card">
            <FaveHeart productId={product.id} />
            <img
              src={product.image_url}
              alt={product.name}
              onClick={(e) => handleOnClick(product.id)}
            />
            <div>${product.price}</div>
            <div className="products-page-name">{product.name}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Summer;
