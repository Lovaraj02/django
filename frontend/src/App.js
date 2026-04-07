import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Signup from "./Signup";
import Login from "./Login";
import Register from "./Register";
import Log from "./Log";

const App = () => {
  return (
    <BrowserRouter>
      <div>
        <nav>
          <Link to="/register">Signup</Link> |{" "}
          <Link to="/login">Login</Link>
        </nav>

        <Routes>
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
};

export default App;