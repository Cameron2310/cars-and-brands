import "./App.css";
import Brand from "./components/Brand";
import Navbar from "./components/Navbar";
import Car from "./components/Car";
import Login from "./components/Login";
import { useState, useEffect } from "react";
import axios from "axios";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  const [post, setPost] = useState(null);

  useEffect(() => {
    axios.get("http://localhost:8000/brands/").then((response) => {
      setPost(response.data);
    });
  }, []);

  if (!post) return null;
  return (
    <Router>
      <Navbar props={post} />
      <Routes>
        <Route path="login/" element={<Login />} />
        <Route path=":brandName/" element={<Brand />} />
        <Route path=":brandName/:carID" element={<Car />} />
      </Routes>
    </Router>
  );
}

export default App;
