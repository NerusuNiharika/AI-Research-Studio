function LoadingSpinner() {
  return (
    <div
      style={{
        position: "fixed",
        top: 0,
        left: 0,
        width: "100%",
        height: "100vh",

        background: "rgba(10,15,30,0.75)",
        backdropFilter: "blur(8px)",

        display: "flex",
        justifyContent: "center",
        alignItems: "center",

        zIndex: 9999,
      }}
    >
      <div
        style={{
          background: "linear-gradient(135deg,#1E293B,#0F172A)",
          padding: "45px",
          borderRadius: "20px",
          width: "420px",
          textAlign: "center",
          boxShadow: "0 20px 45px rgba(0,0,0,.45)",
          border: "1px solid rgba(255,255,255,.08)",
        }}
      >
        <div
          style={{
            width: "65px",
            height: "65px",
            margin: "0 auto 25px",
            border: "6px solid rgba(255,255,255,.2)",
            borderTop: "6px solid #8B5CF6",
            borderRadius: "50%",
            animation: "spin 1s linear infinite",
          }}
        />

        <h2
          style={{
            color: "#FFFFFF",
            marginBottom: "15px",
            fontSize: "28px",
          }}
        >
          Research in Progress
        </h2>

        <p
          style={{
            color: "#CBD5E1",
            fontSize: "16px",
            lineHeight: "1.8",
          }}
        >
          AI agents are gathering information,
          reviewing content, and generating
          your report.
        </p>

        <p
          style={{
            marginTop: "18px",
            color: "#A5B4FC",
            fontSize: "14px",
          }}
        >
          This may take 1–3 minutes depending on the topic.
        </p>

        <style>
          {`
            @keyframes spin {
              0% {
                transform: rotate(0deg);
              }
              100% {
                transform: rotate(360deg);
              }
            }
          `}
        </style>

      </div>
    </div>
  );
}

export default LoadingSpinner;