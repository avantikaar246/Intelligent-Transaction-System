import React, { useState } from "react";
import api from "../api/api";

export default function AddTransaction() {
  const [form, setForm] = useState({ merchant: "", amount: "" });

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("/transactions", form);
      alert("Transaction added!");
      setForm({ merchant: "", amount: "" });
    } catch (err) {
      console.error(err);
      alert("Error adding transaction");
    }
  };

  return (
    <div style={{ padding: "30px", maxWidth: "400px", margin: "auto" }}>
      <h2>Add Transaction</h2>
      <form onSubmit={handleSubmit}>
        <input name="merchant" value={form.merchant} onChange={handleChange} placeholder="Merchant" required />
        <input name="amount" type="number" value={form.amount} onChange={handleChange} placeholder="Amount" required />
        <button type="submit">Add</button>
      </form>
    </div>
  );
}
