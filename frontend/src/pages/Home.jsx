import "./Home.css";
import { useNavigate } from "react-router-dom";
import Navbar from "../components/Navbar";

function Home() {

  const navigate = useNavigate();

  const handleStartResearch = () => {

    const token = localStorage.getItem("token");

    if (token) {

      navigate("/dashboard");

    } else {

      navigate("/login");

    }

  };

  return (

    <>

      <Navbar />

      <div className="home">

        {/* Floating Background */}

        <div className="bg-circle circle1"></div>
        <div className="bg-circle circle2"></div>
        <div className="bg-circle circle3"></div>

        {/* ================= HERO ================= */}

        <section className="hero">

          {/* LEFT */}

          <div className="hero-left">

            <span className="badge">

              ✨ AI Powered Research Platform

            </span>

            <h1>

              <span className="white">

                AI

              </span>{" "}

              <span className="gradient">

                Research Studio

              </span>

            </h1>

            <p>

              An intelligent research assistant that automates the complete
              research process by planning, analyzing, reviewing and generating
              professional reports and presentations from a single user query.

            </p>

            <div className="hero-buttons">

              <button
                className="startBtn"
                onClick={handleStartResearch}
              >

                🚀 Start Research

              </button>

              <button
                className="learnBtn"
                onClick={() => {

                  document
                    .getElementById("features")
                    ?.scrollIntoView({
                      behavior: "smooth",
                    });

                }}
              >

                Learn More

              </button>

            </div>

          </div>

          {/* RIGHT */}

          <div className="hero-right">

            <div className="network">

              <div className="center-node">

                🤖

              </div>

              <div className="node node1">

                📄

              </div>

              <div className="node node2">

                📊

              </div>

              <div className="node node3">

                🔍

              </div>

              <div className="node node4">

                🎯

              </div>

              <span className="line line1"></span>
              <span className="line line2"></span>
              <span className="line line3"></span>
              <span className="line line4"></span>

            </div>

          </div>

        </section>

        {/* ================= WORKFLOW ================= */}

        <section className="workflow">

          <h2>

            Research Workflow

          </h2>

          <div className="workflow-container">

            <div className="step">

              <div className="step-icon">

                🔍

              </div>

              <h3>

                Search Topic

              </h3>

              <p>

                Enter any research topic.

              </p>

            </div>

            <div className="arrow">

              →

            </div>

            <div className="step">

              <div className="step-icon">

                📄

              </div>

              <h3>

                Analyze PDFs

              </h3>

              <p>

                Understand uploaded documents.

              </p>

            </div>

            <div className="arrow">

              →

            </div>

            <div className="step">

              <div className="step-icon">

                📊

              </div>

              <h3>

                Create Report

              </h3>

              <p>

                Generate structured research.

              </p>

            </div>

            <div className="arrow">

              →

            </div>

            <div className="step">

              <div className="step-icon">

                🎯

              </div>

              <h3>

                Presentation

              </h3>

              <p>

                Download PPT & DOC instantly.

              </p>

            </div>

          </div>

        </section>

        {/* ================= FEATURES ================= */}

        <section
          id="features"
          className="features"
        >

          <h2>

            Everything You Need

          </h2>

          <div className="cards">

            <div className="card">

              <div className="icon">

                📚

              </div>

              <h3>

                Smart Research

              </h3>

              <p>

                Generate comprehensive research from a single topic in minutes.

              </p>

            </div>

            <div className="card">

              <div className="icon">

                📘

              </div>

              <h3>

                PDF Analysis

              </h3>

              <p>

                Upload PDFs and enrich your research with valuable insights.

              </p>

            </div>

            <div className="card">

              <div className="icon">

                📊

              </div>

              <h3>

                Detailed Reports

              </h3>

              <p>

                Automatically create structured reports with professional formatting.

              </p>

            </div>

            <div className="card">

              <div className="icon">

                🎯

              </div>

              <h3>

                Presentation Ready

              </h3>

              <p>

                Download PowerPoint and Word documents instantly.

              </p>

            </div>

          </div>

        </section>

      </div>

    </>

  );

}

export default Home;