import streamlit as st

st.set_page_config(page_title="MM Movie Recap Studio", page_icon="🎬", layout="wide")

st.title("🎬 MM Movie Recap Studio")
st.write("မြန်မာ့ရုပ်ရှင်ဇာတ်လမ်းများနှင့် ဗီဒီယိုများကို ဇာတ်လမ်းဆင်ကာ တည်းဖြတ်ဖန်တီးနိုင်သောနေရာ။")

# ဇာတ်လမ်းခေါင်းစဉ်နှင့် အချက်အလက်ထည့်ရန်
movie_title = st.text_input("ရုပ်ရှင်ခေါင်းစဉ် (Movie Title)")
synopsis = st.text_area("ဇာတ်လမ်းအကျဉ်း (Synopsis / Script)")

if st.button("ဇာတ်လမ်းဖိုင် ထုတ်လုပ်ရန်"):
    if movie_title and synopsis:
        st.success(f"အောင်မြင်ပါပြီ! '{movie_title}' အတွက် ဇာတ်လမ်းတွဲကို စတင်ပြင်ဆင်နေပါပြီ။")
    else:
        st.warning("ကျေးဇူးပြု၍ ခေါင်းစဉ်နှင့် ဇာတ်လမ်းအကျဉ်းကို ထည့်သွင်းပေးပါ။")
