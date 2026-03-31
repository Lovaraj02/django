import { API } from "./api";
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
      <h2>Signup</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          placeholder="Username"
          onChange={handleChange}
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          onChange={handleChange}
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          onChange={handleChange}
        />

        <button type="submit">Signup</button>
      </form>
    </div>
  );
};

export default Signup;