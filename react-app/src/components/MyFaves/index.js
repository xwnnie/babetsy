import { useSelector } from "react-redux";
import { useHistory, useLocation } from "react-router-dom";

import FaveHeart from "../FaveHeart";
import FavesSideBar from "./FavesSideBar";

import "./index.css";

const MyFaves = () => {
  const history = useHistory();
  useLocation();

  const productsObj = useSelector((state) => state.products);
  const faveProductIds = useSelector((state) => state.favorites);
  let products = faveProductIds.map((id) => productsObj[id]);

  const categories = {
    clothing: 1,
    furniture: 2,
    bedding: 3,
    bath: 4,
    decor: 5,
    toys: 6,
    accessories: 7
  };

  const categoryName = history.location.pathname.split("/")[2];
  const categoryId = categories[categoryName];
  // console.log(history.location.pathname, categoryName);
  if (categoryId) {
    products = products.filter((product) => product?.category_id == categoryId);
  }

  const handleOnClick = (id) => {
    history.push(`/products/${id}`);
  };
  return (
    <div>
      <FavesSideBar />
      <div className="favorite-products-container">
        {/* <div className="favorites-header">Favorites</div> */}
        <div className="products-container fave-page">
          {products.map((product) => (
            <div key={product?.id} className="product-card fave-page">
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
    </div>
  );
};

export default MyFaves;
