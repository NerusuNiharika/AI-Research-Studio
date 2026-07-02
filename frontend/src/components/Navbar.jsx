import "./Navbar.css";

import {
  Link,
  useLocation,
  useNavigate,
} from "react-router-dom";

import {
  useEffect,
  useState,
} from "react";

function Navbar() {

  const location = useLocation();
  const navigate = useNavigate();

  const [username, setUsername] = useState("");

  useEffect(() => {

    const user = localStorage.getItem("username");

    if (user) {
      setUsername(user);
    } else {
      setUsername("");
    }

  }, [location]);

  // Hide Navbar on Login & Register Pages
  if (
    location.pathname === "/login" ||
    location.pathname === "/register"
  ) {
    return null;
  }

  const logout = () => {

    localStorage.removeItem("token");
    localStorage.removeItem("username");

    navigate("/");

  };

  return (

    <nav className="navbar">

      {/* Logo */}

      <div className="logo">

        AI <span>Research Studio</span>

      </div>

      {/* Right Side */}

      <div className="navLinks">

        {/* HOME PAGE */}

        {location.pathname === "/" && (

          username ? (

            <div className="profileArea">

              <Link
                to="/profile"
                className="profileName"
                >

                👤 {username}

                </Link>

            </div>

          ) : (

            <Link
              to="/login"
              className="navItem"
            >

              Login

            </Link>

          )

        )}

        {/* DASHBOARD */}

        {location.pathname === "/dashboard" && (

          <div className="profileArea">

            <Link
              to="/"
              className="navItem"
            >

              Home

            </Link>

            <Link
                to="/profile"
                className="profileName"
            >

            👤 {username}

            </Link>

            <button
              className="logoutBtn"
              onClick={logout}
            >

              Logout

            </button>

          </div>

        )}

      </div>

    </nav>

  );

}

export default Navbar;