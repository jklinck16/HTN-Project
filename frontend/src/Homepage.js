import logo from "./sheild.png";
import { Link } from "react-router-dom";
const Homepage = (props) => {
  const nextPage = props.nextPage;
  return (
    <div>
      <h1 className="title">News Shield</h1>
      <ul className="bg-bubbles">
        <li className="li"></li>
        <li className="li"></li>
        <li className="li"></li>
        <li className="li"></li>
        <li className="li"></li>
        <li className="li"></li>
        <li className="li"> </li>
        <li className="li"></li>
        <li className="li"></li>
        <li className="li"></li>
      </ul>
      <div className="column">
        <div className="box">
          <h1 className="header">How it Works!</h1>
          <p className="text">
            The website homepage has a list of controversial/popular news topics
            (possibly based on the website's page views). When you select a
            topic, the backend uses the NewsAPI to get articles on the topic
            using keywords. The website will display all retrieved articles from
            an un-biast list of news articles. The text in each article is
            analyzed and the following info is returned about each article:
          </p>
          <h2 className="header">Purpose</h2>
          <p className="text">
            The purpose of the platform is to prevent misinformation and bias
            from websites while providing detailed summaries. Our platform will
            provide a informative analysis on the choosen topic ensuring most
            relevant quality of articles. By allowing users to make instinctive
            descions based on our information, we believe they will be more
            likely to think for themselves and generate valid opinions.
          </p>
          <img className="logo" src={logo}></img>
          <p className="authors">By: Jeffrey, Geoffrey, Ken, Kristian</p>
        </div>
      </div>
      <div className="column">
        <div className="form">
          <Link to="/output">
            <button className="login-button" onClick={nextPage}>
              Environmental Issues
            </button>
            <button className="login-button" onClick={nextPage}>
              Healthcare
            </button>
            <button className="login-button" onClick={nextPage}>
              Canadian Politics
            </button>
            <button className="login-button" onClick={nextPage}>
              Education
            </button>
            <button className="login-button" onClick={nextPage}>
              Economic Equality
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Homepage;
