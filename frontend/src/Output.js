import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
const Output = (props) => {
  const [articles, setArticles] = useState([]);
  const backPage = props.backPage;

  const transformData = (data) => {
    const finalData = [];
    for (let i = 0; i < data.length - 8; i += 9) {
      const a = {};

      a.url = data[i];
      a.properties.author = data[i + 1];
      a.properties.description = data[i + 2];
      a.properties.word_count = data[i + 3];
      a.properties.sentiment_value = data[i + 4];
      a.properties.grade_level = data[i + 5];
      a.properties.reading_ease = data[i + 6];
      a.properties.reading_time = data[i + 7];
      a.properties.relative_sentiment_value = data[i + 8];
      finalData.push(a);
      return finalData;
    }
    const b = { URL: data[0] };
    finalData.push(b);

    for (let i = 1; i < data.length - 8; i++) {
      const a = {};
      a["properties"] = data[i];
      a["properties"] = data[i + 1];
      a["properties"] = data[i + 2];
      a["properties"] = data[i + 3];
      a["properties"] = data[i + 4];
      a["properties"] = data[i + 5];
      a["properties"] = data[i + 6];
      a["properties"] = data[i + 7];
      a["properties"] = data[i + 8];
      b.push(a);
    }
    return finalData;
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
          <div className="organizers">
            <h1>Url, {article[0]}</h1>
            <p>Formalness, {article[1]}</p>
            <h2>Word Count, {article[2]}</h2> */
          </div>
        );
      })}
      <div className="organizers"></div>
    </div>
  );
};
export default Output;
