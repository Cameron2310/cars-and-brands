import { useEffect, useState, useCallback } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

export default function Brand() {
  const { brandName } = useParams();
  const [data, setData] = useState();
  const [cars, setCars] = useState(); 

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios(`http://localhost:8000/api/${brandName}/`);
      setData(response.data);
    };
    fetchData();
  }, [brandName]);

  useEffect(() => {
    const car_data = async () => {
      const response = await axios(`http://localhost:8000/api/`, {
        params: {
          id: data.id,
        },
      });
      setCars(response.data);
    };
    car_data();
  }, [data]);

  if (!data || !cars) {
    return null;
  } else {
    return (
      <div>
        <h2>{data.name}</h2>
        <ul>
          {cars.map((car, i) => {
            return <li key={i}>{car.name}</li>;
          })}
        </ul>
      </div>
    );
  }
}
