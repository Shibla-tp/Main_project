import streamlit as st
import pickle
import requests

data=pickle.load(open('news.pkl','rb'))
news_list=data['headline'].values
similarity=pickle.load(open('feature.pkl','rb'))


def recommendations(news):
    news_index=data[data['headline']==news].index[0]
    dist_per_news=similarity[4]
    news_list=sorted(list(enumerate(dist_per_news)),reverse=True,key=lambda x:x[1])[1:11]
    articles=[]

    for i in news_list:
        articles.append(data['headline'][i[0]])    
    return articles

headline_features=pickle.load(open('feature.pkl','rb'))
st.title('News Recommendation System')
option = st.selectbox(
    'Enter the News article',
    (news_list))

st.write('You selected:', option)

if st.button('Recommend'):
    name=recommendations(option)
    st.write(name)