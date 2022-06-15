import React, { useState, useEffect } from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import { authenticate } from "./store/session";
import { loadProducts } from "./store/products";
import { loadReviews } from "./store/reviews";
import { setOrders } from "./store/orders";
import { setFavorites } from "./store/favorites";
import { setCartItems } from "./store/cart";

import CategoryNav from "./components/CategoryNav";
import MyNav from "./components/MyNav";
import HomePage from "./components/HomePage";
import Products from "./components/Products";
import SingleProduct from "./components/SingleProduct";
import Cart from "./components/Cart";
import OrderHistory from "./components/OrderHistory";
import MyAccount from "./components/MyAccount";
import MyReviews from "./components/MyReviews";
import MyFaves from "./components/MyFaves";
import Footer from "./components/Footer";
import Search from "./components/Search";
import SearchResult from "./components/Search/SearchResults";
import CheckOut from "./components/CheckOut";
import Summer from "./components/Summer";
import Newborn from "./components/Summer/Newborn";
import PageNotFound from "./components/PageNotFound";

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
          dispatch(setCartItems(data.cart));
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
      <Footer />
      <Search />
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
            "/accessories",
          ]}
          exact={true}
        >
          <Products />
        </Route>
        <Route path="/products/:productId" exact={true}>
          <SingleProduct />
        </Route>
        <Route path="/summer" exact={true}>
          <Summer />
        </Route>
        <Route path="/newborn" exact={true}>
          <Newborn />
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
        <ProtectedRoute path="/my-favorites" loaded={loaded}>
          <MyFaves />
        </ProtectedRoute>
        <Route path="/search/:searchQuery" exact>
          <SearchResult />
        </Route>
        <ProtectedRoute path="/checkout" exact={true} loaded={loaded}>
          <CheckOut />
        </ProtectedRoute>
        <Route>
          <PageNotFound />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
