// src/pages/Signup.jsx
import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import api from "../api/api"; // make sure this points to your axios instance

export default function Signup() {
  const [form, setForm] = useState({ username: "", password: "" });
  const navigate = useNavigate();

  // Update form fields
  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  // Submit signup request
  const handleSignup = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post("/signup", form); // goes to http://127.0.0.1:5000/signup
      // Flask should return { message: "User ... signed up successfully" } on success
      if (res.data.message) {
        alert(res.data.message); // show success message
        navigate("/"); // redirect to login page
      } else {
        alert("Signup failed!");
      }
    } catch (err) {
      console.error(err);
      alert("Server error! Make sure your Flask backend is running on http://127.0.0.1:5000");
    }
  };

  return (
    <div style={{ padding: "30px", maxWidth: "400px", margin: "auto" }}>
      <h2>Signup</h2>
      <form onSubmit={handleSignup}>
        <input
          type="text"
          name="username"
          placeholder="Username"
          value={form.username}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
          required
        />
        <button type="submit">Signup</button>
      </form>
      <p>
        Already have an account? <Link to="/">Login</Link>
      </p>
    </div>
  );
}
