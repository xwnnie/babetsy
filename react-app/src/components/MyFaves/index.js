import { useSelector } from "react-redux";
import { useHistory } from "react-router-dom";

import FaveHeart from "../FaveHeart";

import "./index.css";

const MyFaves = () => {
  const history = useHistory();
  const productsObj = useSelector((state) => state.products);
  const faveProductIds = useSelector((state) => state.favorites);
  const products = faveProductIds.map((id) => productsObj[id]);

  const handleOnClick = (id) => {
    history.push(`/products/${id}`);
  };
  return (
    <div>
      <div className="favorites-header">Favorites</div>
      <div className="products-container">
        {products.map((product) => (
          <div key={product?.id} className="product-card">
            <FaveHeart productId={product?.id} />
            <img
              src={product?.image_url}
              alt={product?.name}
              onClick={(e) => handleOnClick(product?.id)}
            />
            <div>${product?.price}</div>
            <div>{product?.name}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MyFaves;
