import { useSelector } from "react-redux";

const Products = () => {
    const productsObj = useSelector(state => state.products);
    const products = Object.values(productsObj)
  return (
    <div>
      <h1>Products</h1>
      {products.map((product) => (
        <div key={product.id}>
          <div>{product.id}</div>
          <div>{product.name}</div>
        </div>
      ))}
    </div>
  );
};

export default Products;
