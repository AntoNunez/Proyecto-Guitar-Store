import React, { useContext, useState, useEffect } from "react";
const Mapeo_Carousel = () => {
  const [lista, setlista] = useState([]);

  const urlApi =
    "https://3001-jorgereboll-proyectofin-f5wtyul2spl.ws-us45.gitpod.io/api/products";

  useEffect(() => {
    getTask(urlApi);
  }, []);

  const getTask = (url) => {
    fetch(url)
      .then((Response) => Response.json())
      .then((data) => {
        console.log(data);
        setlista(data);
      })
      .catch((error) => console.log(error));
  };

  return (
    <div className="container">
      <div
        id="carouselExampleInterval"
        className="carousel slide"
        data-bs-ride="carousel"
      >
        <div className="carousel-inner">
         
          {lista.length > 0 &&
            lista.map((tastk, index) => {
              return (
                <div
                  className={"carousel-item " + (index == 0 ? "active" : "")}
                  data-bs-interval="2000"
                >
                  <img src={tastk.img} className="d-block w-100" alt="..." />
                </div>
              );
            })}
        </div>
        <button
          className="carousel-control-prev"
          type="button"
          data-bs-target="#carouselExampleInterval"
          data-bs-slide="prev"
        >
          <span
            className="carousel-control-prev-icon"
            aria-hidden="true"
          ></span>
          <span className="visually-hidden">Previous</span>
        </button>
        <button
          className="carousel-control-next"
          type="button"
          data-bs-target="#carouselExampleInterval"
          data-bs-slide="next"
        >
          <span
            className="carousel-control-next-icon"
            aria-hidden="true"
          ></span>
          <span className="visually-hidden">Next</span>
        </button>
      </div>
    </div>
  );
};
export default Mapeo_Carousel;