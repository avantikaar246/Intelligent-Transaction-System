import { useState } from "react";
import api from "../api/api";
import ResultCard from "../components/ResultCard";

export default function Evaluate() {
  const [form, setForm] = useState({
    user_id: "u101",
    amount: 12000,
    hour: 1,
    txn_count_last_24h: 9,
    location_mismatch: 1,
    device_familiarity: 0,
    card_number: "4111111111111111",
    card_bin: "411111"
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const submitTransaction = async () => {
    setLoading(true);
    try {
      const res = await api.post("/evaluate-transaction", form);
      setResult(res.data);
    } catch (err) {
      alert("Backend error. Is Flask running?");
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: "30px", maxWidth: "600px", margin: "auto" }}>
      <h2>Intelligent Transaction Evaluation</h2>

      {Object.keys(form).map((key) => (
        <div key={key} style={{ marginBottom: "10px" }}>
          <label>{key}</label>
          <input
            name={key}
            type={["amount", "hour", "txn_count_last_24h", "location_mismatch", "device_familiarity"].includes(key) ? "number" : "text"}
            value={form[key]}
            onChange={handleChange}
            style={{ width: "100%", padding: "6px" }}
          />
        </div>
      ))}

      <button onClick={submitTransaction} disabled={loading}>
        {loading ? "Evaluating..." : "Evaluate Transaction"}
      </button>

      <ResultCard result={result} />
    </div>
  );
}
