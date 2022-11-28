import { useState, useEffect } from "react";
import axios from "axios";

export default function Login() {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();

  const fetchUser = async () => {
    const response = await axios("http://localhost:8000/login/", {
      params: {
        email: email,
        password: password,
      },
    });
    if (response.data.email === email) {
      console.log("User located");
    } else {
      console.log("User not in system.");
    }
  };
  const postUser = async () => {
    const post = await axios.post("http://localhost:8000/login/", {
      params: {
        email: email,
        password: password,
      },
    });
    console.log(response.data);
  };

  return (
    <div>
      <br />
      <div>
        <input
          type="text"
          placeholder="Email"
          onChange={(e) => {
            setEmail(e.target.value);
          }}
        />
        <input
          type="text"
          placeholder="Password"
          onChange={(e) => {
            setPassword(e.target.value);
          }}
        />
      </div>
      <br />
      <div>
        <button type="submit" onClick={fetchUser}>
          Login
        </button>
        <button onClick={postUser}>Sign Up</button>
      </div>
    </div>
  );
}
