import "./App.css";
import Brand from "./components/Brand";
import { useState, useEffect } from "react";
import axios from "axios";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";

function App() {
  const [post, setPost] = useState(null);

  useEffect(() => {
    axios.get("http://localhost:8000/api/brands/").then((response) => {
      setPost(response.data);
    });
  }, []);

  if (!post) return null;
  return (
    <Router>
      <Navbar props={post} />
      <Routes>
        <Route path=":brandName/" element={<Brand />} />
      </Routes>
    </Router>
  );
}

export default App;
