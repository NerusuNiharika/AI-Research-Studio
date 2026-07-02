import { useRef, useState } from "react";
import "./ResearchForm.css";

function ResearchForm({ onStart }) {
  const [topic, setTopic] = useState("");
  const [file, setFile] = useState(null);

  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  const removeFile = (e) => {
    e.preventDefault();
    e.stopPropagation();

    setFile(null);

    if (fileInputRef.current) {
      fileInputRef.current.value = "";
    }
  };

  return (
    <div className="researchForm">

      {/* Research Topic */}

      <div className="formGroup">

        <label className="formLabel">
          🔍 Research Topic
        </label>

        <input
          type="text"
          placeholder="Example: Artificial Intelligence in Healthcare"
          value={topic}
          onChange={(e) => setTopic(e.target.value)}
        />

      </div>

      {/* Upload */}

      <div className="formGroup">

        <label className="formLabel">
          📄 Reference PDF (Optional)
        </label>

        <label className="uploadBox">

          {!file && (
            <>
              <input
                ref={fileInputRef}
                type="file"
                accept=".pdf"
                onChange={handleFileChange}
              />

              <div className="uploadContent">

                <div className="uploadIcon">
                  📂
                </div>

                <h3>Click to Upload PDF</h3>

                <p>Drag & Drop or Click</p>

              </div>
            </>
          )}

          {file && (

            <div className="uploadedContent">

              <button
                type="button"
                className="removeFile"
                onClick={removeFile}
              >
                ✕
              </button>

              <div className="pdfIcon">
                📄
              </div>

              <h3
                className="fileName"
                title={file.name}
              >
                {file.name}
              </h3>

            </div>

          )}

        </label>

      </div>

      <button
        className="researchButton"
        onClick={() => onStart(topic, file)}
      >
        🚀 Start Research
      </button>

    </div>
  );
}

export default ResearchForm;