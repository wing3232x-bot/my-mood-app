import streamlit as st
from supabase import create_client

# Supabase 接続（Streamlit Secretsから読む）
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase = create_client(url, key)

st.title("😊 気分記録アプリ（Supabase版）")

mood = st.slider("今の気分（1〜5）", 1, 5, 3)
memo = st.text_input("ひとことメモ")

if st.button("記録する"):
    supabase.table("moods").insert({
        "mood_level": mood,
        "memo": memo
    }).execute()
    st.success("記録しました")
    st.rerun()

st.subheader("これまでの記録")

res = supabase.table("moods").select("*").order(
    "created_at", desc=True
).execute()

for row in res.data:
    st.write(
        f"{row['created_at'][:16]} | 気分:{row['mood_level']} | {row['memo']}"
    )
