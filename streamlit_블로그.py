import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# 블로그 제목과 소개
st.title("📸 여행과 사진")
st.subheader("카메라로 담는 나의 시선")
st.text(""" 
        저는 쉬는 날이면 카메라를 들고 여행을 떠나는 게 취미입니다. 
        길을 걸으며 아름다운 순간들을 남기고, 그 장소의 분위기를 느끼는 것을 좋아하는 것입니다.
        사진은 순간을 기록하고, 그 분위기를 언제든 다시 느낄 수 있게 해줍니다.
        """)

# 배경음악
st.markdown("### :gray[🎶 배경음악]")
st.audio("./data/lofi.mp3", format="audio/mpeg", loop=True)

# 구분선
st.divider()

# 블로그 시작
st.header("💭 여행지를 돌아보며")
st.caption("후쿠오카 · 교토·오사카 · 강릉 · 부산 / Canon Eos · iPhone SE · iPhone 7")

# 지도에 표시
# 도시별 위도/경도 데이터
locations = {
    "후쿠오카": [33.5902, 130.4017],
    "교토": [35.0116, 135.7681],
    "오사카": [34.6937, 135.5023],
    "강릉": [37.7512, 128.8760],
    "부산": [35.1796, 129.0756]
    }
# 데이터 프레임으로 변환
df = pd.DataFrame(locations.values(), columns=["lat", "lon"], index=locations.keys())

# 지도 표시
st.markdown("### 🗺️")
st.map(df)

st.text('''
        최근 다녀온 여행지들을 돌아보며, 그곳에서 남긴 사진들을 공유해드리고자 합니다.
        도시는 각각의 매력을 지니고 있으며, 날씨에 따라 색감과 분위기가 달라집니다.
        따라서 그런 색감을 잘 살리기 위해서는 카메라의 특징에 맞춰서 잘 골라 사용해야 합니다.
    ''')

# 링크
st.markdown("- 여행 준비는 [Visit Japan](https://www.japan.travel/en/) 참고")

st.divider()

# 여행지별 소개

# 후쿠오카
st.markdown("## :red[🎌 후쿠오카]")
st.write("**일본 규슈 여행**의 중심지입니다. 주변에 *아름다운 소도시가 많아 도시와 시골의 매력을 둘 다 느끼기에 좋은 곳*입니다.")
# 지도에 표시
df_fukuoka = pd.DataFrame([[33.5902, 130.4017]], columns=["lat", "lon"])
st.map(df_fukuoka)

# 이미지
st.markdown("### :red[📸 후쿠오카의 사진]")
st.image("./data/후쿠오카_야경.jpg", caption="후쿠오카의 야경 with iPhone SE", width=500)
st.image("./data/후쿠오카_도심.jpg", caption="후쿠오카 도심의 풍경 with iPhone SE", width=500)
st.image("./data/후쿠오카_시골.jpg", caption="후쿠오카 근교 소도시 with iPhone SE", width=500)
# 동영상
st.markdown("### :red[🎥 후쿠오카의 야경]")
video_file = open("./data/후쿠오카_야경.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

# Magic 문법
"""
- 후쿠오카는 **iPhone SE**로 촬영한 사진들이 많습니다. 
- 흐린 날, 채도가 빠진 색감을 잘 잡는 데엔 SE가 제격입니다.
"""

# 후쿠오카의 기후 지표
st.markdown("### :red[📈 후쿠오카 기후 지표]")
col1, col2, col3 = st.columns(3)    # 3개의 칼럼 생성성
col1.metric("평균 기온", "20°C", "2°C")
col2.metric("강수량", "150mm", "-30mm")
col3.metric("습도", "70%", "+5%")

# 콜아웃
st.markdown("### :red[📌 후쿠오카 여행 팁]")
st.success("후쿠오카는 관광지가 몰려 있어 **도보**로 이동하기 편리합니다. 대중교통도 잘 되어 있습니다.", icon = "✅")
st.info("후쿠오카 주변엔 유후인, 벳푸, 다자이후, 히타 등 **매력적인 소도시**가 많습니다. 버스투어를 하루 정도는 해보시는 것을 추천드립니다.", icon = "ℹ️")
st.write(" - [버스투어 사이트](https://tourvis.com/activity/product/PRD3000384127)")
st.warning("후쿠오카는 **여름에 매우 습합니다**. 우산을 꼭 챙기세요", icon = "⚠️")
st.error("일본의 **골든위크같은 황금연휴**에는 많은 가게들이 영업을 쉬고, 혼잡합니다. 가급적이면 이 시기는 피해서 여행하세요.", icon = "🚫")


st.divider()


# 교토 & 오사카
st.markdown("## :orange[🎎 교토 & 오사카]")
st.write("**역사와 현대를 동시**에 느낄 수 있는 여행지입니다.")

# 지도에 표시
locations_KO = {
    "교토": [35.0116, 135.7681],
    "오사카": [34.6937, 135.5023]
}
df_ko = pd.DataFrame(locations_KO.values(), columns=["lat", "lon"], index=locations_KO.keys())
st.map(df_ko)

# 이미지
st.image("./data/오사카_도심1.jpg", caption="오사카 도심의 풍경 with Canon EOS", width=500)
st.image("./data/오사카_도심2.jpg", caption="오사카의 도로변 with Canon EOS", width=500)
st.image("./data/교토_도심.jpg", caption="교토의 사찰 with Canon EOS", width=500)
st.image("./data/교토_야경.jpg", caption="교토의 야경 with Canon EOS", width=500)

# 동영상
st.markdown("### :orange[🎥 교토의 야경]")
video_file = open("./data/교토_야경.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

# Magic 문법
"""
- 교토와 오사카는 **Canon EOS**로 촬영한 사진들이 많습니다.
- Canon EOS는 **색감이 풍부하고, 선명한 사진**을 찍기에 좋습니다.
- 특히 빛이 별로 없는 밤에 야경을 찍을 때는 카메라의 성능이 중요합니다.
- 제 걸작 중에 하나인 교토 야경 사진도 캐논을 사용했습니다.
"""

# 교토 & 오사카의 기후 지표
st.markdown("### :orange[📈 교토 & 오사카 기후 지표]")

# 교토의 기후 지표
col1, col2, col3 = st.columns(3)    # 3개의 칼럼 생성
col1.metric("평균 기온", "18°C", "+1°C")
col2.metric("강수량", "120mm", "-20mm")
col3.metric("습도", "65%", "+3%")

# 오사카의 기후 지표
col4, col5, col6 = st.columns(3)    # 3개의 칼럼 생성
col4.metric("평균 기온", "19°C", "+2°C")
col5.metric("강수량", "130mm", "-10mm")
col6.metric("습도", "68%", "+4%")

# 콜아웃
st.markdown("### :orange[📌 교토 & 오사카 여행 팁]")
st.success("교토와 오사카는 맛집투어·쇼핑·사진 촬영 모두 만족할 수 있는 **최고의 장소**입니다.", icon = "✅")
st.info("교토와 오사카는 관광지가 여기저기에 있어 걷는 시간이 많을 것입니다. **편한 신발**을 착용하세요.", icon = "ℹ️")
st.warning("일본은 환승이 되지 않습니다. **교통패스**를 사서 이동하는 것이 훨씬 저렴합니다.", icon = "⚠️")
st.error("교토의 기온거리는 **관광객 출입이 금지**되어 있습니다. 촬영이 금지된 곳도 있으니 잘 확인하셔야 합니다.", icon = "🚫")


st.divider()


## 강릉
st.markdown("## :green[🌊 강릉]")
st.write("아름다운 해변으로 유명한 여행지입니다.")

# 지도에 표시
df_gangneung = pd.DataFrame([[37.7512, 128.8760]], columns=["lat", "lon"])
st.map(df_gangneung)

# 이미지
st.markdown("### :green[📸 강릉의 사진]")
st.image("./data/강릉_바다.jpg", caption="강릉의 해변 with iPhone 7", width=500)
st.image("./data/강릉_해변.jpg", caption="강릉의 해변 with iPhone 7", width=500)
st.image("./data/강릉_모래사장.jpg", caption="강릉의 해변 with iPhone SE", width=500)
st.image("./data/강릉_골목.jpg", caption="시골의 풍경 with iPhone SE", width=500)


# Magic 문법
"""
- 강릉은 **iPhone 7**로 촬영한 사진들이 많습니다.
- iPhone 7은 **자연 풍경**을 담기에 적합한 카메라입니다.
- 특히 실내보다 실외에서 자연광을 받으며 촬영할 때 색감을 잘 살립니다.
"""

# 강릉의 기후 지표
st.markdown("### :green[📈 강릉 기후 지표]")
col1, col2, col3 = st.columns(3)    # 3개의 칼럼 생성
col1.metric("평균 기온", "17°C", "+1°C")
col2.metric("강수량", "100mm", "-20mm")
col3.metric("습도", "60%", "+2%")

# 콜아웃
st.markdown("### :green[📌 강릉 여행 팁]")
st.success("강릉은 옥수수와 순두부가 유명합니다. 짬뽕순두부는 꼭 드셔보세요!", icon = "✅")
st.info("강릉은 해안도로를 타고 드라이브 하기가 좋은 곳입니다. 차를 가져오시는 것을 추천드립니다.", icon = "ℹ️")
st.warning("강릉은 여름에 **관광객**으로 붐빕니다. 숙소 예약은 미리 하세요.", icon = "⚠️")
st.error("강릉의 해수욕장들은 파도가 매우 거셉니다. 꼭 구명조끼를 구매하세요.", icon = "🚫")


st.divider()

# 부산
st.markdown("## :blue[🌃 부산]")
st.write("한국의 대표적인 해양 도시로, 아름다운 해변과 야경으로 유명합니다.")

# 지도에 표시
df_busan = pd.DataFrame([[35.1796, 129.0756]], columns=["lat", "lon"])
st.map(df_busan)

# 이미지
st.markdown("### :blue[📸 부산의 사진]")
st.image("./data/부산_노을.jpg", caption="부산 해변의 풍경 with iPhone 7", width=500)
st.image("./data/부산_바다.jpg", caption="부산의 야경 with iPhone SE", width=500)
st.image("./data/부산_바다2.jpg", caption="부산 인물사진 with iPhone SE", width=500)
st.image("./data/부산_카페1.jpg", caption="부산의 카페 with iPhone SE", width=500)
st.image("./data/부산_카페2.jpg", caption="부산의 카페 with iPhone SE", width=500)

# 동영상
st.markdown("### :blue[🎥 부산의 바다]")
video_file = open("./data/부산_바다.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

# Magic 문법
"""
- 부산은 **iPhone SE**로 촬영한 사진들이 많습니다.
- iPhone SE는 몽글몽글하고 흐릿한 색감을 담기에 적합한 카메라입니다.
- SE는 7보다 실외든 실내든 색감을 잘 살리는 편이라 사용하는 분들이 많습니다.
- 7은 SE보다 색감이 더 선명하고, 채도가 높습니다.
"""

# 부산의 기후 지표
st.markdown("### :blue[📈 부산 기후 지표]")
col1, col2, col3 = st.columns(3)    # 3개의 칼럼 생성
col1.metric("평균 기온", "19°C", "+2°C")
col2.metric("강수량", "110mm", "-10mm")
col3.metric("습도", "65%", "+3%")

# 콜아웃
st.markdown("### :blue[📌 부산 여행 팁]")
st.success("부산은 맛집, 카페, 쇼핑, 해변 등 **다양한 즐길 거리**가 많은 도시입니다.", icon = "✅")
st.info("**전포 카페거리**에는 분위기 좋은 카페가 정말 많습니다. 꼭 방문해보세요.", icon = "ℹ️")
st.warning("부산은 여름에 **무더위**가 심합니다. 시원한 옷차림으로 대비하세요.", icon = "⚠️")
st.error("부산의 **스카이캡슐**은 예약을 하지 않으면 이용할 수 없습니다. 미리 예약해두세요.", icon = "🚫")


st.divider()


# 수식
st.write("## :green[💸 여행 경비 계산식]")
st.latex(r'''
\text{총 비용} = \text{교통비} + \left( \text{숙박비} \times (\text{일수} - 1) \right) + \text{식비}
''')

st.divider()


# 코드 블록
st.markdown("## :blue[📱 여행지별 사용 기기]")
with st.echo():
    # 이 블록의 코드와 결과를 출력
    devices = {
        "후쿠오카": "iPhone SE",
        "교토·오사카": "Canon EOS",
        "강릉": "iPhone 7",
        "부산": "iPhone SE"
    }

    city = "후쿠오카"
    device = devices.get(city, "unknown")
    print(device)


# 데이터테이블
# pandas DataFrame을 사용하여 여행지별 월 평균 기온을 표시
st.markdown("## :red[🌡️ 여행지별 월 평균 기온]")
df = pd.DataFrame({
    "월": [f"{i}월" for i in range(1, 13)],
    "후쿠오카": [6.6, 7.5, 10.7, 15.8, 20.2, 23.9, 27.9, 29.2, 25.5, 19.4, 13.6, 8.5],
    "교토": [4.6, 5.4, 8.7, 14.2, 18.7, 22.7, 26.6, 28.1, 24.1, 17.8, 12.0, 7.1],
    "오사카": [6.0, 6.7, 9.9, 15.2, 19.8, 23.9, 27.9, 29.4, 25.3, 19.3, 13.2, 8.2],
    "강릉": [-0.5, 0.6, 5.0, 11.1, 16.5, 20.8, 24.5, 26.3, 21.4, 15.3, 9.2, 2.9],
    "부산": [2.4, 3.9, 8.1, 13.1, 17.8, 21.6, 25.8, 27.3, 23.1, 17.1, 11.3, 5.6]
})

df


st.divider()


st.markdown("## :orange[📊 여행지별 평균 기온]")

# streamlit 그래프

weather_data = pd.DataFrame({
    "Month": [f"{i}월" for i in range(1, 13)],
    "Fukuoka": [6.6, 7.5, 10.7, 15.8, 20.2, 23.9, 27.9, 29.2, 25.5, 19.4, 13.6, 8.5],
    "Kyoto": [4.6, 5.4, 8.7, 14.2, 18.7, 22.7, 26.6, 28.1, 24.1, 17.8, 12.0, 7.1],
    "Osaka": [6.0, 6.7, 9.9, 15.2, 19.8, 23.9, 27.9, 29.4, 25.3, 19.3, 13.2, 8.2],
    "Gangneung": [-0.5, 0.6, 5.0, 11.1, 16.5, 20.8, 24.5, 26.3, 21.4, 15.3, 9.2, 2.9],
    "Busan": [2.4, 3.9, 8.1, 13.1, 17.8, 21.6, 25.8, 27.3, 23.1, 17.1, 11.3, 5.6]
})

# 시각화를 위해 인덱스를 Month로 설정
weather_data = weather_data.set_index("Month")

'#### :orange[📈 st.line_chart()]'
st.line_chart(weather_data)

'#### :orange[📉 st.area_chart()]'
st.area_chart(weather_data)

'#### :orange[📊 st.bar_chart()]'
st.bar_chart(weather_data)


st.divider()


# 여행지별 월 평균 기온 데이터

st.markdown("### :blue[📶 matplotlib 그래프]")
weather_data = pd.DataFrame({
    "Month": [f"{i}" for i in range(1, 13)],
    "Fukuoka": [6.6, 7.5, 10.7, 15.8, 20.2, 23.9, 27.9, 29.2, 25.5, 19.4, 13.6, 8.5],
    "Kyoto": [4.6, 5.4, 8.7, 14.2, 18.7, 22.7, 26.6, 28.1, 24.1, 17.8, 12.0, 7.1],
    "Osaka": [6.0, 6.7, 9.9, 15.2, 19.8, 23.9, 27.9, 29.4, 25.3, 19.3, 13.2, 8.2],
    "Gangneung": [-0.5, 0.6, 5.0, 11.1, 16.5, 20.8, 24.5, 26.3, 21.4, 15.3, 9.2, 2.9],
    "Busan": [2.4, 3.9, 8.1, 13.1, 17.8, 21.6, 25.8, 27.3, 23.1, 17.1, 11.3, 5.6]
})

# 데이터 설정


months = weather_data["Month"]
cities = weather_data.columns[1:]
x = np.arange(len(months))  # x축 위치
width = 0.15  # 막대 너비
multiplier = 0

# 그래프 생성
fig, ax = plt.subplots(figsize=(14, 6), layout="constrained")

# 도시별로 막대그래프 그리기
for city in cities:
    offset = width * multiplier
    rects = ax.bar(x + offset, weather_data[city], width, label=city)
    ax.bar_label(rects, padding=2, fontsize=8)
    multiplier += 1

# 레이아웃 설정
ax.set_ylabel("Temperature (°C)")
ax.set_xlabel("Month")
ax.set_title("Comparison of average temperature by city")
ax.set_xticks(x + width * 2, months, rotation=45)
ax.legend(loc='upper left', ncol=len(cities))
ax.set_ylim(0, 35)

plt.tight_layout()
plt.show()

st.pyplot(fig)


st.divider()


st.markdown("# :blue[📉 Seaborn 그래프]")
# 도시별 월별 평균 기온 데이터
weather_data = pd.DataFrame({
    "Month": [f"{i}" for i in range(1, 13)],
    "Fukuoka": [6.6, 7.5, 10.7, 15.8, 20.2, 23.9, 27.9, 29.2, 25.5, 19.4, 13.6, 8.5],
    "Kyoto": [4.6, 5.4, 8.7, 14.2, 18.7, 22.7, 26.6, 28.1, 24.1, 17.8, 12.0, 7.1],
    "Osaka": [6.0, 6.7, 9.9, 15.2, 19.8, 23.9, 27.9, 29.4, 25.3, 19.3, 13.2, 8.2],
    "Gangneung": [-0.5, 0.6, 5.0, 11.1, 16.5, 20.8, 24.5, 26.3, 21.4, 15.3, 9.2, 2.9],
    "Busan": [2.4, 3.9, 8.1, 13.1, 17.8, 21.6, 25.8, 27.3, 23.1, 17.1, 11.3, 5.6]
})

# long-form 형식으로 변환
weather_long = weather_data.melt(id_vars="Month", var_name="City", value_name="Temperature")

# 월을 숫자로 다시 매핑해 정렬 가능하도록 설정
month_order = [f"{i}" for i in range(1, 13)]
weather_long["Month"] = pd.Categorical(weather_long["Month"], categories=month_order, ordered=True)

# 시각화
sns.set_theme(style="darkgrid")
plt.figure(figsize=(10, 6))
sns.lineplot(
    data=weather_long,
    x="Month",
    y="Temperature",
    hue="City",
    marker="o"
)

plt.title("Comparison of average temperature by city")
plt.ylabel("Temperature (°C)")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()

import streamlit as st
st.pyplot(plt)

