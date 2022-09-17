import json
import requests
from newspaper import Article
from newspaper import Config
import cohere

#def cohere_summary(text):
    #co = cohere.Client('u8CtzGJvVaaIuQtuCyWNiCoHaRVVjfdqGKdyflV3')

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
    print(text)
    output = ('https://onesimpleapi.com/api/readability?'
              'token=3wEsSs9EGcHNyjHv2A5qEPnB6jcxbQdoVOsj3hDC&'
              'output=json&'
              'text=' + text
              )
    response = requests.get(output)
    raw_scores = response.json()['sentiment_scores']
    sentiment_value = response.json()['sentiment']
    grade_level = response.json()['grade_level']
    reading_ease = response.json()['reading_ease']
    reading_time = response.json()['reading_time']
    print(raw_scores)
    return raw_scores

def sort_raw_scores(raw_scores):
    sorted_scores = []
    temp_list = []
    for i in range(len(raw_scores)):
        index = i
        negative_score = raw_scores[i]['negative']
        print(negative_score)
        positive_score = raw_scores[i]['positive']
        neutral_score = raw_scores[i]['neutral']
        ratio_score = ((positive_score+neutral_score)/(negative_score+neutral_score))
        temp_list.append(ratio_score)
        temp_list.append(i)

        sorted_scores.append(temp_list)
        temp_list = []

    arr = sorted_scores
    print(arr)
    size = len(arr)
    arr = sort_list(arr,size)
    print(arr)
    return arr


def strip_article(link):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    url = link
    article = Article(url, config=config)
    article.download()
    article.parse()
    return article.text.rstrip('\n')

string1 = "Liberal"
string2 = "Anita"
string3 = "Trudeau"
string4 = "Pierre Poilievre"
string5 = "asfasdfasdas"

final_string = 'qInTitle= {} OR {} OR {} OR {} OR {}&'.format(string1, string2, string3, string4, string5)

url = ('https://newsapi.org/v2/everything?'
        + final_string +
       #'https://newsapi.org/v2/top-headlines/sources?'
       'language = en&'
       #'country= us&'
       'from=2022-09-17&'
       'sortBy=popularity&'
       'apiKey=b0559a331d74449e9a9d8930bbb2e285')

response = requests.get(url)
articles_list = response.json()['articles']
url_list = []

for i in range(len(articles_list)-1):
    url_list.append(articles_list[i]['url'])
#print(url_list)

clean_list = []
for i in range(len(url_list)-1):
    if url_list[i][12:16] == 'cbc':
        clean_list.append(url_list[i])
    elif url_list[i][12:27] == 'theglobeandmail':
        clean_list.append(url_list[i])
    elif url_list[i][12:24] == 'nationalpost':
        clean_list.append(url_list[i])
    elif url_list[i][12:25] == 'financialpost':
        clean_list.append(url_list[i])
    elif url_list[i][12:19] == 'thestar':
        clean_list.append(url_list[i])

#print(clean_list)

final_list = []
raw_scores_list = []
#for y in range(len(clean_list)-1):
#    final_list.append(clean_list[y])
#    final_list.append(strip_article(clean_list[y]).replace('\n\n', ''))
url_list = url_list[:5]
print(url_list)


for y in range(len(url_list)):
    try:
        temp_list=[]
        temp_list.append(url_list[y])
        temp_list.append(word_count(strip_article(url_list[y]).replace('\n\n', '').replace('\n\n', '')))
        final_list.append(temp_list)
        raw_scores_list.append(raw_sentiment(strip_article(url_list[y]).replace('\n\n', '').replace('\n\n', '')))
        #print(one_simple_function((strip_article(url_list[y]).replace('\n\n', '').replace('\n\n', ''))))
        print(len(raw_scores_list))

        # instead of appending to list, call functions that perform calculations and add the data to a list.
        # url, word count, raw sentiment, relative sentiment, grade level, reading ease, informal/formal (look into this later)
    except ValueError as err:
        raw_scores_list.append({'negative': 0.0, 'neutral': 1, 'positive': 0.00})
print(raw_scores_list)
arr = sort_raw_scores(raw_scores_list)
print(arr)
current_num = 0
final_list_fr = []
i = 0


while i < 5:
  #print(final_list[arr[i][1]][0])
  final_list_fr.append(final_list[(arr[i][1])][0])
  final_list_fr.append(final_list[(arr[i][1])][1])
  final_list_fr.append(arr[i][0])
  print(final_list_fr)
  i += 1

print(final_list_fr)


list_to_send = []



















#domains=techcrunch.com,engadget.com,thenextweb.com
#domains=techcrunch.com
#from=2020-09-01&to=2020-09-1
#Specify words which must appear in articles, and words that must not, to remove irrelevent results: q=gamestop +stonks -sell
#qInTitle="title search"
