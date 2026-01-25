import streamlit as st
import datetime

st.title("☀️ 今日の気分ログ")

# 入力フォーム
date = st.date_input("日付", datetime.date.today())
mood = st.select_slider("今の気分は？", options=["最悪", "微妙", "普通", "良い", "最高"])
note = st.text_area("一言メモ")

if st.button("記録する"):
    st.balloons()
    st.success(f"{date} の気分（{mood}）を記録しました！")
    # 本来はここに保存処理を書きますが、今回は簡易版のため表示のみ
