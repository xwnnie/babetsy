import { useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import FaveHeart from "../FaveHeart";

import "./index.css";

const Newborn = () => {
  const history = useHistory();

  const productsObj = useSelector((state) => state.products);
  let products = Object.values(productsObj);
  const newbornProducts = [4, 14, 6, 12, 17, 51, 75, 76, 55, 58, 78, 82];
  products = products.filter((product) => newbornProducts.includes(product.id));

  const handleOnClick = (id) => {
    history.push(`/products/${id}`);
  };
  return (
    <div className="summer-container">
      <div className="summer-header newborn">
        <div>NEWBORN COLLECTION</div>
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
            <div>${product.price}</div>
            <div className="products-page-name">{product.name}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Newborn;
