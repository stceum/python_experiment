# coding:utf-8
def get_labels(url):
    '''
    input: the link of the web and the decode of the website(UTF-8 default)
    output: the list of the sentences
    '''
    import requests
    import jieba
    import re
    from bs4 import BeautifulSoup
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    rq = requests.get(url, headers = headers)
    html = rq.content
    bs_obj = BeautifulSoup(html, "html.parser")
    labels = bs_obj.find_all('a')
    except_dict = ['\+', '\?', '\!', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '\n', '\t']
    useless_list = [r'凤凰', r'新浪', r'新闻', r'独家', r'资讯', r'凰家尚品', r'体育文化', r'财经', r'图', r'娱乐', r'视频', r'体育', r'小说', r'视频', r'时尚', r'汽车房产']
    results = []
    for j in labels:
        text = ""
        for i in except_dict:
            # print(j.text)
            text = re.sub(i, '', j.text)
        for i in useless_list:
            text = text.replace(i, "")
        results.append(text)
    return results

def count_label(results):
    '''
    input: the list of the sentences
    output: a dictionary of the frequency of the worlds
    '''
    import jieba
    words = []
    for i in results:
        tmp = jieba.lcut(i)
        words = words + tmp
    summary = {}
    for i in words:
        if not i in summary.keys():
            summary[i] = 1
        else:
            summary[i] += 1
    return summary

def connect_sentences(short_sentences_dir):
    text = ""
    for i in short_sentences_dir:
        text = text + i + " "
    return text

def generate_word_cloud(input_sentence, width = 1000, height = 800, background_color = 'white', font_path = "simkai.ttf", file_path = 'word_cloud.png'):
    '''
    input: the long text (seperated by space between words)
    output: the picture of the words
    '''
    import wordcloud
    w = wordcloud.WordCloud(width=width,height=height,background_color=background_color, font_path = font_path)
    w.generate(input_sentence)
    w.to_file(file_path)
