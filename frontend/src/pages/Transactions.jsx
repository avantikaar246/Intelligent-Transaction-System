import React, { useEffect, useState } from "react";
import api from "../api/api";

export default function Transactions() {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    async function fetchTransactions() {
      try {
        const res = await api.get("/transactions");
        setTransactions(res.data);
      } catch (err) {
        console.error(err);
      }
    }
    fetchTransactions();
  }, []);

  return (
    <div style={{ padding: "30px" }}>
      <h2>Transactions</h2>
      <ul>
        {transactions.map((t, idx) => (
          <li key={idx}>{t.merchant} - ${t.amount}</li>
        ))}
      </ul>
    </div>
  );
}
