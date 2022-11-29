import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";
import axios from "axios";

export default function Brand() {
  const { brandName } = useParams();
  const [data, setData] = useState();
  const [cars, setCars] = useState();

  useEffect(() => {
    const fetchData = async () => {
      const response = await axios(`http://localhost:8000/${brandName}/`);
      if (response === undefined) {
        return;
      }
      setData(response.data);
    };
    fetchData();
  }, [brandName]);

  useEffect(() => {
    const carData = async () => {
      if (data === undefined) {
        return;
      }
      const response = await axios(`http://localhost:8000`, {
        params: {
          id: data.id,
        },
      });
      setCars(response.data);
    };
    carData();
  }, [data]);

  if (!data || !cars) {
    return null;
  } else {
    return (
      <div>
        <h2>{data.name}</h2>
        <ul>
          {cars.map((car, i) => {
            return (
              <li key={i}>
                <Link to={`${car.id}/`}>{car.name}</Link>
              </li>
            );
          })}
        </ul>
        <img src={data.img} />
      </div>
    );
  }
}
