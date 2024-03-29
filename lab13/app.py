from textblob import TextBlob
def hello(name):
    output = f'Hello {name}'
    return output

def extract_sentiment(text):
    text = TextBlob(text)
    return text.sentiment.polarity

def text_contain_word(word: str, text: str):
    
    return word in text

def bubble_sort(arr):
    n = len(arr)
    flag = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                flag = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not flag:
            return