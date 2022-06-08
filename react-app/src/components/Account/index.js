import { useSelector } from "react-redux";

const Account = () => {
    let orders = useSelector(state => state.orders);
    orders = Object.values(orders);
    let products = useSelector((state) => state.products);
    let purchases;

    orders.sort((a, b) => {
    const keyA = new Date(a[0]?.created_at);
    const keyB = new Date(b[0]?.created_at);
    return keyA > keyB ? -1 : 1;
    });

    return (
        <div>
            <div>My Orders</div>
            {orders.map(order => {
                purchases = Object.values(order)
                // console.log("!!!!!!!!!", purchases)
               return (
                 <div key={order.id}>
                   <div>{purchases[0].order_number}</div>
                   <div>placed on: {purchases[0].created_at}</div>
                   <div>Items:</div>
                   {purchases.map((item) => (
                     <div key={item.product_id}>
                       {/* <div>{products[item.product_id]}</div> */}
                       <div>name: {products[item?.product_id]?.name}</div>
                       <div>product id: {item.product_id}</div>
                       <div>quantity: {item.quantity}</div>
                     </div>
                   ))}
                 </div>
               ); 
            } )}
        </div>
    )
}

export default Account;