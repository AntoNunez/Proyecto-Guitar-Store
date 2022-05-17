import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import Cards from "./Cards.jsx";
import Forgot_password from "../component/Login/forgot_password.js";
import Carousel from "./Carousel-home.jsx";
import { GiGuitarHead } from "react-icons/gi";
import { Link } from "react-router-dom";


export const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <>
      <Carousel img="https://picsum.photos/1080/720" />
      <Cards />

      <div className="text-center mt-5">
        <h1>Hello Rigo!!</h1>
        <p>
          <img src={rigoImageUrl} />
        </p>
        <div className="alert alert-info">
          {store.message ||
            "Loading message from the backend (make sure your python backend is running)..."}
        </div>
      </div>
      <Forgot_password />

      


    </>
  );
};





















