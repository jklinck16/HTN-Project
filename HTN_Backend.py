import json
import requests
from newspaper import Article
from newspaper import Config
import cohere
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"*":{"origins": "*"}})

@app.route("/main")
@cross_origin()
def handlequery():
    input = request.args.getlist("args")
    print(input)
    result = main(input[0].split())

    return result


    #http://127.0.0.1:5000/main?args=%27canada%20trudeau%20pierre%20anita%20economy%27



#def cohere_summary(text):
    #co = cohere.Client('u8CtzGJvVaaIuQtuCyWNiCoHaRVVjfdqGKdyflV3')
def main(input_array):

    def sort_list(array, size):
        for ind in range(size):
            min_index = ind

            for j in range(ind + 1, size):
                # select the minimum element in every iteration
                if array[j][0] < array[min_index][0]:
                    min_index = j
             # swapping the elements to sort the array
            (array[ind], array[min_index]) = (array[min_index], array[ind])
        return array

    def word_count(text):
        word_count_var = len(text.split())
        return word_count_var


    def raw_sentiment(text):
        raw_scores = []
        #print(text)
        output = ('https://onesimpleapi.com/api/readability?'
                  'token=3wEsSs9EGcHNyjHv2A5qEPnB6jcxbQdoVOsj3hDC&'
                  'output=json&'
                  'text=' + text
                  )
        response = requests.get(output)
        raw_scores = response.json().get('sentiment_scores', {'negative': 0.03,'neutral': 0.92,'positive': 0.05})
        sentiment_value = response.json().get('sentiment', 'neutral')
        grade_level = response.json().get('grade_level', 12)
        reading_ease = response.json().get('reading_ease', 83)
        reading_time = response.json().get('reading_time', '1 minute')
        #print(raw_scores)
        #print(raw_scores, sentiment_value, grade_level, reading_ease, reading_time)
        return raw_scores, sentiment_value, grade_level, reading_ease, reading_time



    def sort_raw_scores(raw_scores):
        sorted_scores = []
        temp_list = []
        for i in range(len(raw_scores)):
            index = i
            negative_score = raw_scores[i]['negative']
            #print(negative_score)
            positive_score = raw_scores[i]['positive']
            neutral_score = raw_scores[i]['neutral']
            ratio_score = ((positive_score+neutral_score)/(negative_score+neutral_score))
            temp_list.append(ratio_score)
            temp_list.append(i)

            sorted_scores.append(temp_list)
            temp_list = []

        arr = sorted_scores
        #print(arr)
        size = len(arr)
        arr = sort_list(arr,size)
        #print(arr)
        return arr


    def strip_article(link):
        try:
            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
            config = Config()
            config.browser_user_agent = user_agent
            url = link
            article = Article(url, config=config)
            article.download()
            article.parse()
            return article.text.rstrip('\n')
        except:
            print('failed to download and parse')
            return ''

    string1 = input_array[0]
    string2 = input_array[1]
    string3 = input_array[2]
    string4 = input_array[3]
    string5 = input_array[4]

    final_string = 'qInTitle= {} OR {} OR {} OR {} OR {}&'.format(string1, string2, string3, string4, string5)
    print(final_string)
    author = ""
    description = ""
    url = ('https://newsapi.org/v2/everything?'
            + final_string +
           #'https://newsapi.org/v2/top-headlines/sources?'
           'language = en&'
           #'country= us&'
           'from=2022-09-16&'
           'sortBy=popularity&'
           'apiKey=103798ec6988494ea133a88138c01817')

    response = requests.get(url)
    #print(response.json())
    #breakpoint()
    articles_list = response.json()['articles']

    main_list = []


    for i in range(len(articles_list)-1):
        temp_list = []
        temp_list.append(articles_list[i]['url'])
        temp_list.append(articles_list[i]['author'])
        temp_list.append(articles_list[i]['description'])
        main_list.append(temp_list)
    #print(main_list)


    #print(clean_list)

    final_list = []
    raw_scores_list = []
    #for y in range(len(clean_list)-1):
    #    final_list.append(clean_list[y])
    #    final_list.append(strip_article(clean_list[y]).replace('\n\n', ''))
    main_list = main_list[:15]
    #print(url_list)

    y = 0
    c=0
    while y+c < 5+c:
        try:
            temp_var = (raw_sentiment(strip_article(main_list[y+c][0]).replace('\n\n', '').replace('\n\n', '')))
            temp_list=[]
            temp_list.append(main_list[y])
            temp_list.append(word_count(strip_article(main_list[y+c][0]).replace('\n\n', '').replace('\n\n', '')))
            temp_list.append(temp_var[1])
            temp_list.append(temp_var[2])
            temp_list.append(temp_var[3])
            temp_list.append(temp_var[4])

            final_list.append(temp_list)

            raw_scores_list.append(temp_var[0])
            #print(one_simple_function((strip_article(url_list[y]).replace('\n\n', '').replace('\n\n', ''))))
            #print(len(raw_scores_list))

            # instead of appending to list, call functions that perform calculations and add the data to a list.
            # url, word count, raw sentiment, relative sentiment, grade level, reading ease, informal/formal (look into this later)
            y += 1
        except ValueError as err:
            c+=1
            #print("added to c")

    #print(raw_scores_list)
    #print(final_list)
    arr = sort_raw_scores(raw_scores_list)
    #print(arr)
    current_num = 0
    final_list_fr = []
    i = 0


    while i < 5:
      #print(final_list[arr[i][1]][0])
      #print(arr[i][1])
      final_list_fr.append(final_list[(arr[i][1])][0][0]) # url
      final_list_fr.append(final_list[(arr[i][1])][0][1]) # author
      final_list_fr.append(final_list[(arr[i][1])][0][2]) # description
      final_list_fr.append(final_list[(arr[i][1])][1]) # word count
      final_list_fr.append(final_list[(arr[i][1])][2]) # sentiment value
      final_list_fr.append(final_list[(arr[i][1])][3]) # grade level
      final_list_fr.append(final_list[(arr[i][1])][4]) # reading ease
      final_list_fr.append(final_list[(arr[i][1])][5]) # reading time

      final_list_fr.append(arr[i][0]) #relative sentiment value
      #print(final_list_fr)
      i += 1

    return jsonify(final_list_fr)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
