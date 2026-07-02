function DownloadButtons({ reportPath, pptPath }) {

  const API = "http://127.0.0.1:8000";

  return (

    <div className="downloadButtons">

      <button
        className={`downloadBtn reportBtn ${!reportPath ? "disabledBtn" : ""}`}
        disabled={!reportPath}
        onClick={() => window.open(`${API}/${reportPath}`, "_blank")}
      >
        📄 Download Report
      </button>

      <button
        className={`downloadBtn pptBtn ${!pptPath ? "disabledBtn" : ""}`}
        disabled={!pptPath}
        onClick={() => window.open(`${API}/${pptPath}`, "_blank")}
      >
        📊 Download Presentation
      </button>

    </div>

  );

}

export default DownloadButtons;