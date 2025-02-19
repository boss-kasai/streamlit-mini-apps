import datetime

import jpholiday
import streamlit as st


def date_calendar_app():
    st.title("あの日まで何日？")

    # ユーザー入力
    target_date = st.date_input(
        "未来の日付を選択してください", min_value=datetime.date.today()
    )

    if st.button("計算"):
        today = datetime.date.today()
        delta = target_date - today

        weekdays = 0
        weekends = 0
        holidays = 0

        for i in range(delta.days + 1):
            day = today + datetime.timedelta(days=i)
            if day.weekday() < 5:
                weekdays += 1
            else:
                weekends += 1
            if jpholiday.is_holiday(day):
                holidays += 1
        st.write(f"今日から {target_date} までの日数: {delta.days} 日")
        st.write(f"平日の日数: {weekdays - holidays} 日")
        st.write(f"土日の日数: {weekends} 日")
        st.write(f"祝日の日数: {holidays} 日")
