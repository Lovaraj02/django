import { API } from "./api";
import './App.css';
import { useState } from "react";

const Signup = () => {
  const [form, setForm] = useState({
    username: "",
    email: "",
    password: ""
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  };


const handleSubmit = (e) => {
  e.preventDefault();

  fetch(`${API}/signinapp/signup/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(form)
  })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.log(err));
};

  return (
    <div>
      <h1>Signup</h1>

      <form onSubmit={handleSubmit}>
        <input className="in"
          type="text"
          name="username"
          placeholder="Username"
          onChange={handleChange}
        />
        {/* <br/> */}

        <input className="in"
          type="email"
          name="email"
          placeholder="Email"
          onChange={handleChange}
        />
        {/* <br/> */}
        <input className="in"
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleChange}
        />
        {/* <br/> */}

        <button type="submit">Signup</button>
      </form>
    </div>
  );
};

export default Signup;