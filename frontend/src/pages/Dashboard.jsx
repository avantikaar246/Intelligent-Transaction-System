import React from "react";
import { Link } from "react-router-dom";

export default function Dashboard() {
  return (
    <div style={{ padding: "30px" }}>
      <h1>Dashboard</h1>
      <nav>
        <Link to="/transactions">Transactions</Link> |{" "}
        <Link to="/add-transaction">Add Transaction</Link> |{" "}
        <Link to="/evaluate">Evaluate</Link>
      </nav>
    </div>
  );
}
