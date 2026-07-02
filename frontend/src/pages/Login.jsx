import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Login.css";

import { loginUser } from "../services/auth";

function Login() {

  const navigate = useNavigate();

  const [username, setUsername] = useState("");

  const [password, setPassword] = useState("");

  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {

    e.preventDefault();

    try {

      setLoading(true);

      const response = await loginUser(
        username,
        password
      );

      // Save JWT Token
      localStorage.setItem(
        "token",
        response.access_token
      );

      // Save Username
      localStorage.setItem(
        "username",
        username
      );

      alert("Login Successful!");

      navigate("/");

    }

    catch (error) {

      if (error.response) {

        alert(error.response.data.detail);

      }

      else {

        alert("Unable to connect to server.");

      }

    }

    finally {

      setLoading(false);

    }

  };

  return (

    <div className="loginPage">

      <div className="loginCard">

        <div className="loginHeader">

          <h1>Welcome Back</h1>

          <p>

            Login to continue using AI Research Studio

          </p>

        </div>

        <form onSubmit={handleLogin}>

          <div className="inputGroup">

            <label>

              Username

            </label>

            <input
              type="text"
              placeholder="Enter username"
              value={username}
              onChange={(e)=>setUsername(e.target.value)}
              required
            />

          </div>

          <div className="inputGroup">

            <label>

              Password

            </label>

            <input
              type="password"
              placeholder="Enter password"
              value={password}
              onChange={(e)=>setPassword(e.target.value)}
              required
            />

          </div>

          <button
            type="submit"
            className="loginButton"
            disabled={loading}
          >

            {loading ? "Logging In..." : "Login"}

          </button>

        </form>

        <div className="registerText">

          New User?

          <Link to="/register">

            Register

          </Link>

        </div>

      </div>

    </div>

  );

}

export default Login;