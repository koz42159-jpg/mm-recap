import streamlit as st

st.set_page_config(page_title="MM Movie Recap Studio", page_icon="🎬", layout="wide")

st.title("🎬 MM Movie Recap Studio")
st.write("မြန်မာ့ရုပ်ရှင်ဇာတ်လမ်းများနှင့် ဗီဒီယိုများကို ဇာတ်လမ်းဆင်ကာ တည်းဖြတ်ဖန်တီးနိုင်သောနေရာ။")

# 1. Video File Upload
st.header("📁 ရုပ်ရှင်ဗီဒီယို တင်ရန်")
uploaded_file = st.file_uploader("ဗီဒီယိုဖိုင်ကို ရွေးချယ်ပါ (MP4, MKV, AVI)", type=["mp4", "mkv", "avi"])

if uploaded_file is not None:
    st.success(f"အောင်မြင်ပါပြီ! ဗီဒီယိုဖိုင် ({uploaded_file.name}) တင်ပြီးပါပြီ။")
    st.video(uploaded_file)

# 2. Movie Details & Script
st.header("📝 ဇာတ်လမ်းအချက်အလက်နှင့် ဇာတ်ညွှန်း")
movie_title = st.text_input("ရုပ်ရှင်ခေါင်းစဉ် (Movie Title)")
synopsis = st.text_area("ဇာတ်လမ်းအကျဉ်း / ဇာတ်ညွှန်း (Synopsis / Script)")

# 3. Voiceover & Audio Settings
st.header("🎙️ အသံသွင်းခြင်းနှင့် အညွှန်းဆက်ခြင်း")
voice_option = st.selectbox("အသံထွက် ပုံစံရွေးချယ်ရန်", ["AI မန်နေဂျာ (အမျိုးသားအသံ)", "AI မန်နေဂျာ (အမျိုးသမီးအသံ)", "ကိုယ်ပိုင်အသံဖိုင် တင်မည်"])

if voice_option == "ကိုယ်ပိုင်အသံဖိုင် တင်မည်":
    audio_file = st.file_uploader("အသံဖိုင် တင်ရန် (MP3, WAV)", type=["mp3", "wav"])

# 4. Export / Generate Button
st.header("🚀 ဇာတ်လမ်းဖိုင် ထုတ်လုပ်ရန်")
if st.button("ဗီဒီယို ဇာတ်လမ်းတည်းဖြတ်ရန် စတင်မည်"):
    if movie_title and synopsis:
        st.success(f"'{movie_title}' အတွက် ဇာတ်လမ်းဖိုင်များကို စတင်ထုတ်လုပ်နေပါပြီ ကိုဇင်!")
        st.balloons()
    else:
        st.warning("ကျေးဇူးပြု၍ ရုပ်ရှင်ခေါင်းစဉ်နှင့် ဇာတ်လမ်းအကျဉ်းကို ထည့်သွင်းပေးပါ။")
