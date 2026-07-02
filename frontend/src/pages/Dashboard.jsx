import "./Dashboard.css";
import { useState } from "react";

import Navbar from "../components/Navbar";
import ResearchForm from "../components/ResearchForm";
import ResearchResults from "../components/ResearchResults";
import LoadingSpinner from "../components/LoadingSpinner";

import api from "../services/api";

function Dashboard() {

  const [loading, setLoading] = useState(false);

  const [report, setReport] = useState("");

  const [reportPath, setReportPath] = useState("");
  const [pptPath, setPptPath] = useState("");

  const startResearch = async (topic, file) => {

    if (!topic) {
      alert("Please enter a research topic");
      return;
    }

    try {

      setLoading(true);

      const formData = new FormData();

      formData.append("topic", topic);

      if (file) {
        formData.append("file", file);
      }

      const response = await api.post(
        "/research",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setReport(response.data.report);
      setReportPath(response.data.report_path);
      setPptPath(response.data.ppt_path);

    } catch (error) {

      console.error(error);
      alert("Research Failed");

    } finally {

      setLoading(false);

    }

  };

  return (

    <>

      <Navbar />

      {loading && <LoadingSpinner />}

      <div className="dashboard">

        {/* Header */}

        <div className="pageHeader">

          <div>

            <h1>Research Workspace</h1>

            <p>
              Generate AI-powered research reports and presentations.
            </p>

          </div>

        </div>

        {/* Main Grid */}

        <div className="workspace">

          {/* LEFT PANEL */}

          <div className="leftPanel">

            <div className="card">

              <div className="cardTitle">
                📂 Research Input
              </div>

              <ResearchForm onStart={startResearch} />

            </div>

            <div className="card statusCard">

              <div className="cardTitle">
                🤖 AI Status
              </div>

              <div className="statusItem">

                {loading
                  ? "🟣 Research in Progress..."
                  : "🟢 Waiting for Input"}

              </div>

              <div className="statusText">

                {loading
                  ? "The AI is planning, analyzing documents, and generating your research report."
                  : "Enter a research topic and click Start Research."}

              </div>

            </div>

            <div className="card tipsCard">

              <div className="cardTitle">
                💡 Tips
              </div>

              <ul>

                <li>Use specific research topics.</li>

                <li>Upload supporting PDF documents.</li>

                <li>Wait for the AI workflow to complete.</li>

                <li>Download the generated DOCX and PPT.</li>

              </ul>

            </div>

          </div>

          {/* RIGHT PANEL */}

          <div className="rightPanel">

            <div className="reportHeader">

              <h2>📄 Report Preview</h2>

            </div>

            <ResearchResults
              report={report}
              reportPath={reportPath}
              pptPath={pptPath}
            />

          </div>

        </div>

      </div>

    </>

  );

}

export default Dashboard;