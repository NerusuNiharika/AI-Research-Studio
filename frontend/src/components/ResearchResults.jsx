import DownloadButtons from "./DownloadButtons";

function ResearchResults({
  report,
  reportPath,
  pptPath,
}) {

  return (

    <div className="researchResults">

      <div className="reportContainer">

        <div className="reportBody">

          {report ? (

            <pre className="reportText">

              {report}

            </pre>

          ) : (

            <div className="emptyState">

              <div className="emptyIcon">
                🤖
              </div>

              <h3>
                No Research Generated
              </h3>

              <p>

                Enter a research topic and optionally upload a PDF.

                Your AI generated report will appear here.

              </p>

              <div className="workflowPreview">

                <div className="workflowStep">
                  🔍 Topic
                </div>

                <div className="workflowArrow">
                  →
                </div>

                <div className="workflowStep">
                  📄 PDF
                </div>

                <div className="workflowArrow">
                  →
                </div>

                <div className="workflowStep">
                  🤖 AI
                </div>

                <div className="workflowArrow">
                  →
                </div>

                <div className="workflowStep">
                  📊 Report
                </div>

              </div>

            </div>

          )}

        </div>

      </div>

      {(reportPath || pptPath) && (

        <div className="downloadArea">

          <DownloadButtons
            reportPath={reportPath}
            pptPath={pptPath}
          />

        </div>

      )}

    </div>

  );

}

export default ResearchResults;