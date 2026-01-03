import React from "react";

export default function ResultCard({ result }) {
  if (!result) return null;

  const { risk_level, decision, visa_checks } = result;

  return (
    <div
      style={{
        marginTop: "20px",
        padding: "20px",
        border: "1px solid #ccc",
        borderRadius: "8px",
        backgroundColor: "#f9f9f9",
      }}
    >
      <h3 style={{ marginBottom: "10px" }}>Transaction Evaluation Result</h3>

      <p>
        <strong>Risk Level:</strong> {risk_level || "N/A"}
      </p>
      <p>
        <strong>Decision:</strong> {decision || "N/A"}
      </p>

      {visa_checks && Object.keys(visa_checks).length > 0 && (
        <div style={{ marginTop: "15px" }}>
          <h4>Visa Checks</h4>
          <pre
            style={{
              backgroundColor: "#eee",
              padding: "10px",
              borderRadius: "5px",
              overflowX: "auto",
            }}
          >
            {JSON.stringify(visa_checks, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
