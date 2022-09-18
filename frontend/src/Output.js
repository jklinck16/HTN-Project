import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
const Output = (props) => {
  const [articles, setArticles] = useState([]);
  const backPage = props.backPage;

  const transformData = (data) => {
    return data;
  };

  const getResult = async () => {
    const keyword1 = "america";
    const keyword2 = "trudeau";
    const keyword3 = "pierre";
    const keyword4 = "anita";
    const keyword5 = "sdgfsadfsad";


    const response = await fetch(
      `http://localhost:5000/main?args=${keyword1} ${keyword2} ${keyword3} ${keyword4} ${keyword5}`,
      {
        headers: {
          "Access-Control-Allow-Origin": true,
        },
      }
    );

    const data = response.json();

    console.log("data", data);

    const transformedData = transformData(data);

    return transformedData;

    return [
      {
        URL: "https//:google.com",
        properties: { formal: "formal", word_count: 4000 },
      },
      {
        URL: "https//:google.com",
        properties: { formal: "informal", word_count: 4020 },
      },
    ];
  };
  const initializeData = () => {
    const fn = async () => {
      const articles = await getResult();
      setArticles(articles);
    };
    fn();
  };
  //shower spinner while array empty
  useEffect(initializeData, []);
  return (
    <div>
      <h1 className="title">
        <Link to="/">
          <button className="buttonBack" onClick={backPage}>
            Back
          </button>
        </Link>
        Results
      </h1>
      {articles.map((article) => {
        return (
          <div className="organizers">
            //<h1>Url, {article.URL}</h1>
            //<p>Formalness, {article.properties.formal}</p>
            //<h2>Word Count, {article.properties.word_count}</h2>
          </div>
        );
      })}
      <div className="organizers"></div>
    </div>
  );
};
export default Output;
