import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./Register.css";

import { registerUser } from "../services/auth";

function Register() {

  const navigate = useNavigate();

  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [loading, setLoading] = useState(false);

  const handleRegister = async (e) => {

    e.preventDefault();

    if (password !== confirmPassword) {
      alert("Passwords do not match.");
      return;
    }

    try {

      setLoading(true);

      await registerUser(
        username,
        email,
        password
      );

      alert("Registration Successful!");

      navigate("/login");

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

    <div className="registerPage">

      <div className="registerCard">

        <div className="registerHeader">

          <h1>Create Account</h1>

          <p>
            Register to access AI Research Studio
          </p>

        </div>

        <form onSubmit={handleRegister}>

          <div className="inputGroup">

            <label>Username</label>

            <input
              type="text"
              placeholder="Enter username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />

          </div>

          <div className="inputGroup">

            <label>Email</label>

            <input
              type="email"
              placeholder="Enter email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />

          </div>

          <div className="inputGroup">

            <label>Password</label>

            <input
              type="password"
              placeholder="Enter password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />

          </div>

          <div className="inputGroup">

            <label>Confirm Password</label>

            <input
              type="password"
              placeholder="Confirm password"
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />

          </div>

          <button
            type="submit"
            className="registerButton"
            disabled={loading}
          >

            {loading ? "Creating Account..." : "Create Account"}

          </button>

        </form>

        <div className="loginText">

          Already have an account?

          <Link to="/login">

            Login

          </Link>

        </div>

      </div>

    </div>

  );

}

export default Register;