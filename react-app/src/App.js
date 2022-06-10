import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import { authenticate } from "./store/session";
import { loadProducts } from "./store/products";
import { loadReviews } from "./store/reviews";
import { setOrders } from "./store/orders";
import { setFavorites } from "./store/favorites";

import CategoryNav from "./components/CategoryNav";
import MyNav from "./components/MyNav";
import HomePage from "./components/HomePage";
import Products from "./components/Products";
import SingleProduct from "./components/SingleProduct";
import Cart from "./components/Cart";
import OrderHistory from "./components/OrderHistory";
import MyAccount from "./components/MyAccount";
import MyReviews from "./components/MyReviews";

import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
import NavBar from "./components/AuthNav";
import ProtectedRoute from "./components/auth/ProtectedRoute";

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  const sessionUser = useSelector((state) => state.session.user);

  useEffect(() => {
    (async () => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  useEffect(() => {
    (async () => {
      dispatch(loadProducts());
      dispatch(loadReviews());
    })();
  }, [dispatch]);

  useEffect(() => {
    (async () => {
      if (sessionUser) {
        const res = await fetch(`/api/users/${sessionUser.id}`);
        if (res.ok) {
          const data = await res.json();
          dispatch(setOrders(data.orders));
          dispatch(setFavorites(data.favorite_products));
        }
      }
      setLoaded(true);
    })();
  }, [dispatch, sessionUser]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      {sessionUser ? <MyNav /> : <NavBar />}
      <CategoryNav />
      <Switch>
        <Route path="/" exact={true}>
          <HomePage />
        </Route>
        <Route
          path={[
            "/clothing",
            "/furniture",
            "/bedding",
            "/bath",
            "/decor",
            "/toys",
          ]}
          exact={true}
        >
          <Products />
        </Route>
        <Route path="/products/:productId" exact={true}>
          <SingleProduct />
        </Route>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path="/cart" exact={true} loaded={loaded}>
          <Cart />
        </ProtectedRoute>
        <ProtectedRoute path="/my-account" exact={true} loaded={loaded}>
          <MyAccount />
        </ProtectedRoute>
        <ProtectedRoute path="/my-orders" exact={true} loaded={loaded}>
          <OrderHistory />
        </ProtectedRoute>
        <ProtectedRoute path="/my-reviews" exact={true} loaded={loaded}>
          <MyReviews />
        </ProtectedRoute>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
