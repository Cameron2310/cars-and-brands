import { Link } from "react-router-dom";
import "./Navbar.css";

function Navbar({ props }) {
  return (
    <header className="header">
      <div className="left">
        <a href="#">Navbar</a>
      </div>
      <div className="mid">
        <ul className="navbar">
          {props.map((prop, i) => {
            return (
              <li>
                <Link to={`${prop.name}/`} key={i}>
                  {prop.name}
                </Link>
              </li>
            );
          })}
        </ul>
      </div>
      <div className="right">
        <Link to="login/">Login</Link>
      </div>
    </header>
  );
}

export default Navbar;
