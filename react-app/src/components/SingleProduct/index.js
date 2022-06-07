import { useParams } from "react-router-dom";
import { useSelector } from "react-redux";

const SingleProduct = () => {
  const { productId } = useParams();
  const product = useSelector((state) => state.products[productId]);
  const reviews = Object.values(product?.reviews);

  return (
    <div>
      <img src={product.image_url} alt={product.name} />
      <div>{product.id}</div>
      <div>{product.price}</div>
      <div>{product.name}</div>
      <div>{product.description}</div>
      <div>
          Reviews
        {reviews.map((review) => (
          <div>
            <div>{review.content}</div>
            <div>{review.author_name}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default SingleProduct;
