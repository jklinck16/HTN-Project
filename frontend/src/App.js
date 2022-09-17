import "./App.css";
import HomePage from "./Homepage.js";
import OutputPage from "./Output.js";
import { useState } from "react";
import { Routes, Route } from "react-router-dom";
import { BrowserRouter as Router, Link } from "react-router-dom";
function App() {
  const pages = {
    HOMEPAGE: "HOMEPAGE",
    OUTPUT: "OUTPUT",
  };
  const [currentPage, setCurrentPage] = useState(pages.HOMEPAGE);
  console.log(pages.HOMEPAGE);
  const nextPage = () => {
    // switch (currentPage) {
    //   case pages.HOMEPAGE:
    //     setCurrentPage(pages.OUTPUT);
    //   default:
    //     setCurrentPage(pages.OUTPUT);
    // }
  };
  const backButton = () => {
    switch (currentPage) {
      case pages.OUTPUT:
        setCurrentPage(pages.HOMEPAGE);
      default:
        setCurrentPage(pages.HOMEPAGE);
    }
  };
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/output" element={<OutputPage />} />
        </Routes>
      </Router>
      {/* {(() => {
        switch (currentPage) {
          case pages.HOMEPAGE:
            return <HomePage nextPage={nextPage} />;
          case pages.OUTPUT:
            return <OutputPage backPage={backButton} />;
          default:
            return <HomePage />;
        }
      })()} */}
    </div>
  );
}

export default App;
