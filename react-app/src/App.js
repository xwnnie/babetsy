import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import { authenticate } from "./store/session";
import { loadProducts } from "./store/products";

import CategoryNav from './components/CategoryNav';
import MyNav from './components/MyNav';
import HomePage from './components/HomePage';
import Products from './components/Products';
import SingleProduct from './components/SingleProduct';
import Cart from './components/Cart';

import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import NavBar from './components/AuthNav';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import User from './components/User';


function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  const sessionUser = useSelector(state => state.session.user);

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

    useEffect(() => {
      (async () => {
        dispatch(loadProducts());
      })();
    }, [dispatch]);

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
        {/* <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route> */}
        <ProtectedRoute path="/my-account" exact={true}>
          {/* <UsersList /> */}
        </ProtectedRoute>
        <ProtectedRoute path="/cart" exact={true}>
          <Cart />
        </ProtectedRoute>
        {/* <ProtectedRoute path="/users" exact={true}>
          <UsersList />
        </ProtectedRoute>
        <ProtectedRoute path="/users/:userId" exact={true}>
          <User />
        </ProtectedRoute> */}
      </Switch>
    </BrowserRouter>
  );
}

export default App;
