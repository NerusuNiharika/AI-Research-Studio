import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import { getResearchHistory } from "../services/profile";
import "./Profile.css";

function Profile() {

    const username = localStorage.getItem("username");

    const [history, setHistory] = useState([]);

    useEffect(() => {

        loadHistory();

    }, []);

    const loadHistory = async () => {

        try {

            const data = await getResearchHistory();

            setHistory(data);

        }

        catch (error) {

            console.error(error);

        }

    };

    return (

        <>

            <Navbar />

            <div className="profilePage">

                <div className="profileCard">

                    <div className="profileHeader">

                        <div className="avatar">

                            👤

                        </div>

                        <h1>

                            {username}

                        </h1>

                        <p>

                            AI Research Studio User

                        </p>

                    </div>

                    <div className="profileSection">

                        <h2>

                            Previous Research

                        </h2>

                        {

                            history.length === 0 ?

                                (

                                    <p>

                                        No research generated yet.

                                    </p>

                                )

                                :

                                history.map((item) => (

                                    <div
                                        key={item.id}
                                        className="historyCard"
                                    >

                                        <h3>

                                            {item.topic}

                                        </h3>

                                        <div className="historyButtons">

                                            <a
                                                href={`http://127.0.0.1:8000/${item.report_path}`}
                                                target="_blank"
                                                rel="noreferrer"
                                            >

                                                📄 DOCX

                                            </a>

                                            <a
                                                href={`http://127.0.0.1:8000/${item.ppt_path}`}
                                                target="_blank"
                                                rel="noreferrer"
                                            >

                                                📊 PPT

                                            </a>

                                        </div>

                                    </div>

                                ))

                        }

                    </div>

                </div>

            </div>

        </>

    );

}

export default Profile;