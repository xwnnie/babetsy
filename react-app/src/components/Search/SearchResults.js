import { useParams, useHistory } from "react-router-dom";
import { useSelector } from "react-redux";
import FaveHeart from "../FaveHeart";


const SearchResult = () => {
    const history = useHistory();
  const { searchQuery } = useParams();

  let products = useSelector((state) => state.products);
  products = Object.values(products);

  const results = products.filter(
    (product) =>
      product?.name?.toLowerCase().indexOf(searchQuery.toLowerCase()) >= 0
  );


  const handleOnClick = (id) => {
    history.push(`/products/${id}`);
  };

  return (
    <div className="summer-container">
      <div className="summer-header search-results"></div>
      <div className="main-container">
        <div id="search-h2">
          Showing Results for
          <span> "{searchQuery}" </span>
        </div>
        {!results.length ? (
          <div className="no-search-div">
            <div id="no-search-msg">NO MATCHING ITEMS</div>
          </div>
        ) : (
          <div className="products-container">
            {results.map((product) => (
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
        )}
      </div>
    </div>
  );
  
};

export default SearchResult;
