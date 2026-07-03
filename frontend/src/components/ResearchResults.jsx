import ReactMarkdown from "react-markdown";
import DownloadButtons from "./DownloadButtons";

function ResearchResults({

  report,

  hero,

  sections,

  reportPath,

  pptPath,

}) {

  return (

    <div className="researchResults">

      <div className="reportContainer">

        <div className="reportBody">

          {report ? (

            <div className="markdownReport">

              <h1 className="reportTitle">
                {report.match(/^#\s*(.*)$/m)?.[1] || "Research Report"}
              </h1>

              {/* Hero Image */}

              {hero && (

                <div className="heroImageContainer">

                  <img

                    src={hero.image_url}

                    alt="Research"

                    className="heroImage"

                  />

                  <p className="imageSource">

                    Source{" "}

                    <a

                      href={hero.source_url}

                      target="_blank"

                      rel="noreferrer"

                    >

                      {hero.source}

                    </a>

                  </p>

                </div>

              )}

              {sections.map((section, index) => (

                <div

                  key={index}

                  className="reportSection"

                >

                  <h2 className="sectionHeading">

                    {section.title}

                  </h2>

                  {section.image && (

                    <div className="sectionImageContainer">

                      <img

                        src={section.image.image_url}

                        alt={section.title}

                        className="sectionImage"

                      />

                      <p className="imageSource">

                        Source{" "}

                        <a

                          href={section.image.source_url}

                          target="_blank"

                          rel="noreferrer"

                        >

                          {section.image.source}

                        </a>

                      </p>

                    </div>

                  )}

                  <ReactMarkdown

                    components={{

                      p: ({ children }) => (

                        <p className="reportParagraph">

                          {children}

                        </p>

                      ),

                      ul: ({ children }) => (

                        <ul className="reportList">

                          {children}

                        </ul>

                      ),

                      ol: ({ children }) => (

                        <ol className="reportList">

                          {children}

                        </ol>

                      ),

                      li: ({ children }) => (

                        <li className="reportListItem">

                          {children}

                        </li>

                      ),

                      strong: ({ children }) => (

                        <strong className="reportBold">

                          {children}

                        </strong>

                      ),

                    }}

                  >

                    {section.content}

                  </ReactMarkdown>

                </div>

              ))}

            </div>

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