import { useParams } from "react-router-dom";

const SingleProduct = () => {
    const {productId} = useParams();
    return (
        <div>
            {productId}
        </div>
    )
}

export default SingleProduct