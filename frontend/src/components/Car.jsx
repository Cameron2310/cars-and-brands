import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

export default function Car() {
  const { carID } = useParams();
  const [carData, setCarData] = useState();

  useEffect(() => {
    const getCarData = async () => {
      const response = await axios(`http://localhost:8000/${carID}/`);
      setCarData(response.data);
    };
    getCarData();
  }, []);

  if (!carData) {
    return null;
  } else {
    return (
      <div>
        {carData.brand.name} {carData.name} {carData.price}
      </div>
    );
  }
}
