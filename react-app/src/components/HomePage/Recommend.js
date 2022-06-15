import { useHistory } from "react-router-dom";
import { useSelector } from "react-redux";
import { useState } from "react";

import FaveHeart from "../FaveHeart";

const Recommend = () => {
  const history = useHistory();
  const productsObj = useSelector((state) => state.products);
  let products = Object.values(productsObj);
  const recommendedProducts = [52, 42, 43, 44, 45, 46, 47, 48, 60, 18, 28, 36];

  const [pivot, setPivot] = useState(0);

  const handleOnClick = (id) => {
    history.push(`/products/${id}`);
  };

  let currProducts = recommendedProducts.slice(pivot, pivot + 4);

  products = products.filter((product) => currProducts.includes(product.id));

  return (
    <div className="recommend-container">
      {pivot <= 0 ? null : (
        <button
          onClick={() => setPivot(pivot - 4)}
          className="recommend-arrow-left"
        >
          <span className="material-symbols-outlined">chevron_left</span>
        </button>
      )}
      <div className="recommend-products">
        {products.map((product) => (
          <div key={product.id} className="product-card">
            <FaveHeart productId={product.id} />
            <img
              src={product.image_url}
              alt={product.name}
              onClick={(e) => handleOnClick(product.id)}
              className="recommend-product-img"
            />
            <div className="recommend-product-price">${product.price}</div>
            <div className="recommend-product-name">{product.name}</div>
          </div>
        ))}
      </div>

      {pivot >= recommendedProducts.length - 4 ? null : (
        <button
          onClick={() => setPivot(pivot + 4)}
          className="recommend-arrow-right"
        >
          <span className="material-symbols-outlined">chevron_right</span>
        </button>
      )}
    </div>
  );
};

export default Recommend;
