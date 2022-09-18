import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
const Output = (props) => {
  const [articles, setArticles] = useState([]);
  const backPage = props.backPage;

  const transformData = (data) => {
    const finalData = [];
    console.log("the data before transformation is", data);
    for (let i = 0; i < data.length - 8; i += 9) {
      const a = {};
      const properties = {};
      a.url = data[i];
      properties.author = data[i + 1];
      properties.description = data[i + 2];
      properties.word_count = data[i + 3];
      properties.sentiment_value = data[i + 4];
      properties.grade_level = data[i + 5];
      properties.reading_ease = data[i + 6];
      properties.reading_time = data[i + 7];
      properties.relative_sentiment_value = data[i + 8];
      a.properties = properties;
      finalData.push(a);
    }
    console.log("final data from this message is", finalData);
    return finalData;
  };

  const getResult = async () => {
    const keyword1 = "gun";
    const keyword2 = "weapon";
    const keyword3 = "murder";
    const keyword4 = "kidnapping";
    const keyword5 = "killing";

    const response = await fetch(
      `http://localhost:5000/main?args=${keyword1} ${keyword2} ${keyword3} ${keyword4} ${keyword5}`,
      {
        headers: {
          "Access-Control-Allow-Origin": true,
        },
      }
    );

    const data = await response.json();

    console.log("data", data);

    const transformedData = transformData(data);
    console.log("transformed data is", data);

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

          <div className="organizers" key={article.URL}>

            <h1>Url, {article.url}</h1>
            <p>Author, {article.properties.author}</p>
            <p>Description, {article.properties.description}</p>
            <p>Word Count, {article.properties.word_count}</p>
            <p>Sentiment Value, {article.properties.sentiment_value}</p>
            <p>Grade Level, {article.properties.grade_level}</p>
            <p>Reading Ease, {article.properties.reading_ease}</p>
            <p>Reading Time, {article.properties.reading_time}</p>
            <p>Relative sentiment value, {article.properties.relative_sentiment_value}</p>
          </div>
        );
      })}
      <div className="organizers"></div>
    </div>
  );
};
export default Output;
