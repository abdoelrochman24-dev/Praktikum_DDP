# import streamlit as st

# st.set_page_config(page_title="Bangun Datar", page_icon="📐")

# st.title("Hello, Streamlit!")
# st.write("Welcome to your first Streamlit app.")

# def luas_persegi(sisi):
#     return sisi * sisi

# def luas_segitiga(alas, tinggi):
#     return 0.5 * alas * tinggi

# def luas_lingkaran(jari_jari):
#     return 3.14 * jari_jari * jari_jari

# # Sidebar
# menu = st.sidebar.selectbox("Pilih Bangun Datar", ("Luas Persegi", "Luas Segitiga", "Luas Lingkaran"))
 
# if menu == "Luas Persegi":
#     st.header("Luas Persegi")

# # image
#     st.image("https://cnc-magazine.oramiland.com/parenting/images/Persegi_finirezyhome.wordpress.co.width-500.format-webp.webp",     
#     caption="Persegi adalah bangun datar dua dimensi yang memiliki empat sisi sama panjang dan empat sudut siku-siku.",
#     width=300
# )

# # INPUT
# sisi = st.number_input("Masukkan panjang sisi persegi  (cm):", min_value=0)
# if st.button("Hitung"):
#     luas = luas_persegi(sisi)
#     st.write(f"Luas Persegi dengan sisi {sisi} adalah {luas}")

# elif menu == "Luas Segitiga":
#     st.header("Luas Segitiga")

# # IMAGE
# st.image("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPAAAADSCAMAAABD772dAAAAh1BMVEX////8/PwAAADT09NAQED5+fn29vb09PTs7OwjIyPg4ODl5eXJycnS0tLo6Ojx8fHc3NwzMzOOjo6jo6NoaGizs7N3d3e5ubmCgoKbm5tNTU16enolJSXKysobGxs8PDxsbGysrKxWVlYsLCwdHR2Li4tFRUUNDQ1PT09hYWG3t7ednZ0TExN5/iKUAAANGklEQVR4nO1diXbiOgyVDA4hARLWsJW1hQL9/+8byQmdAoFsTgjLffMOtAXbN5Jl2ZZlgDfeeOONN95443WAPiT/u3dbCgFKqV4lUb5zU4oB8XQ6QnQceBHCAEa9g9jtkbDv3ZJCIGG14tfXYMuoCPfeTSgWFWHduwnF4uUIfzBhBHyVYQlhMwD2OV7E7yDCX8IDaA5fZBxmh3IkfrYrl97euzGFwTFNeBEBByCy/O/ezSgMxNWoGK/Dl6U7Est7t6JASHC3e2Hz3PjeTSkGKKsj+Fq9zlgM3bHE2noJr2K4XOGSMn8I8yXGJuq44xEYroTh7hUIk391qEqwfkxw6v0XUGkkha4AWnNythrCeXrCJODvEWmy4fAMcdK7d3tyhVqQhu5cBj8BOp/eUw/GzM0ihf79ERpb87kJA646vqFC/lHCYPHMC5jErNs2fiXKc2Nn1nhqwjYrNBO0d6b/xvupAT7reIyw+goWOizRCkguBk/sUy/XEn0jZVSCVUs0ReNpLXVLNP9zC95IVupnnEQwv97w//zolzcp9eQZLTUR7E8N+F2pPBoqem2RUj8diB3z+iPIYx+mF+/zCa0WKfQA/oc5OKPakTCgQbr+TPC115sZ8L+v0rD0R9xszZ6pG/NY5GxPOqo5cP4zRNjXDeOJhibWZPYvTn/5nyC93Q2fyfsgnW4I85SP/ONOopTscz4RYXTE+RzhZH8Y2QlDfBqfGnkWeOZN4bk7qdzs5+AbLF6d8r2Y+JNSc4Reoe3KC87WO5fe6bAE3Ke76wupPySIw6B3sTtqtc0zaSKMO8/Qh0mwbKEvVPVCfXm5y30GwiBZoS9+f26RWQO67ScYmpB3VC5DlBCNc6tNAt90CmxZDlA0m8IJk9uFhHkZ037woDXypsD47If/LfQhjKoPvcDFWjpchf7JHofInT4+7z5yOBNZ4ubv6uQprHPfmiEl8mpm/g3LC6Sc0ys7okbDCO/ZnSo8rE9Njf4aJx5o2ktW6gdVa1fYynIlACplf0gBU6unyeNWlFI/oqFmX6OzgcRLVage0+OJmNciyY242m6n64QbJuSY+RDfu/yQsO5elxT11Ct/oecw/H5ACUv2muTVzmh+meGk1DxShHtnpQX6W8FWqq6IKtCnBg/kcaGysutRhgImK5APw9efNBzW6fshyVZ4D+V78M6ZlYkwTSofJ4KcVBqqo9sSwtbtP8Nk55uCh4AB3U8wbjKKnBWhioR4DMa80eBGHIi+Pg4fC2kK+ShzCITN140hOPhQ5FG8xQ5Cp5BlA/FYiujehxHjLPpKXX4RSwNMUuhIyWDUtFHKhpBoaGtYXiCRfMc5VygjdJ6pcpCEvpblA2pgX0Cc3fyIPszCRfGhrWG5gEcRWRNuDAHbczPiQyouRJR+YEJYxYrI4d3DGIXtBlDqbswxVyLWJ41GDPtLQ5dolnoLFcEQlZjti0HEf35lJgysg/GAGM+NWk3K24t9gcRccYyb88Dw036Uk7QhaRypxWxcXPvrW+pyEobegiQXS1OdZcwHg+zHlJCv2g5qCISYjbOEHVMRkJW6hC41Cda4iD67DnMY5Xj8L7dfRkutziDtkkgi5vjKBY87ZdRpnrEnkISMGYSGfE6Rpl/pW5YXEk5fYweh8ceW09JJWAXrJEICmUkO74lp/gtDkzcL4kNWEuwbq1XfkmVnQhEWfXYd1uzK3lJo4VLFrJVHwqiCdRIJwG5HrFqelE/CrY7KY6lVsE5o9NkNhAf3XIdVppg1xO0+oTOEiTOXHqqJPp4vvr4T7xIkJSyh3U3WqBzhiuR5SJPGYvGmcYJunx9oeMT6MsUXE4b7+zEy9w/vYYeJGpK4Ha1dgmEpqIiDRkpAmFStlXz6Zl2JwbxVEddUAsLIWZMSt0O6x9OlsWui/77CQ3OLhB/inAHqBGZc1mwt7u1iWsLO9H3uDHEpIHnsrXsvBswzGhJMMEBxeO5dU1JRzd15RsOZiDB97nN5xwUuCTan8kvzVedQS/egPsJC6QsCPfDNIWUODuv0SSUoYrhIUZ0eqFRRKU+EmoMr0bSRlcofL833tKDFW8FpV8n/TDZkgsUSSUrtpKowI3iHfqxhUs4utTRPT4zf/LyESe8ePjUH66w17N2q1UtWk6g4p+PnAfl0bvG75BL52H72J43/l+RjrlNz9p7iLTX6Z9jTx48em1w7qGKs3WISeydC5VkrGKTQsyzfV6GHnIX4R8yBE6k1PLGDIE8gP0ffZVZz5ssHYWwbv5e+FAUzW0iRPec8rWjNrUmVsxEDn+3wUEVvGS12mFuG0aKHYrcuuw2CN3OKNlyk0JlgKFmSkBZztaJHA7rYK2H21zOySiAO45loeFvRvvguDRC9IRYb3tP/yWigUfr3LsGi6vvTsBQO/8YRI3oKRJiUfiAm4Fwmn6KB7DIxSJ5AZIXOWN/RNg/805Vg1g/q56Hw4zD5ZEuXY6DEIezr3mdx7geqzDpZJXz0SRdVFXcpZ4HqdoR/SoRzqt8gDAWmpEL01FZwxnlwAFZpKuqwDRLzDkVwduk2YVL9wnxqP1FhNpVurY4aSSrN05DZcZCpcG4tUucIwhL6n0VYLd/OZA/rtbYtlqs5GK7FsEPMFsPh5Es9xoUYToio6AKMWL1F+AEohF0h159Q7/K22ZN9GZ4al5z+3vP6Hnzs+/193/M9a7ffp2r6LqJLb2BfCSuAnxZnjczYjkignypKw6D/N5vUccEWj5EQ8vgWr1WFfhrF3L0tzqyT2UL7BSnHw+clj/+roxCo9m/UfFGdjQknxV/P6v3EgISG0GIrpI6ppfk3FWpOcGbaRoPM6ohBslsdjbkKTTMz51DTMJeWwPm5c+3HDZFyefUMsWMtb4LmVP6yWj4go2L87PWUdZLXMgu60xyniRKGPW0apKnv4Sb9wezIslUyP127d7psjZ3fTZlo1PvaIgB15dtRedZygHITvnb6uouuHJakcO1DHpYapbovSBt03T+MvF5s6R+LkXOfLfWNAIljPK4CDVLqHJwPFWChr9zQBGKpwOucecSsqXDKkgJVIJHe8Rhxmib6rCiMqlK34eokjA8uEn7slF6+JQl0DAf5vLx1o40xz8z1R/1pPl43Sp597yqkhO5Yc/vsqmaNMdb6bIzkZH6ac13z9FCvylQ0djqkcU5zxB+vWuosj/2Ebz3l8EWF49Ia6F+QJ6gCMbMXhJpWJ/IGB2JqSB5ITI3q4d4BnTGgZnM6oosRDvNHuI6Ax04j1VmE83LySXLteI0LZPfVgwtvs4gHIZ81I0us5/P2CUToHlISYHDhbSZ9XLZzWfa1tjaewqhnJgxQ+9xntDetnJbIrPr5qRY5zS5h/4qFDN9HdZVs1naEgQmfQouEQS0kp/2uCqfMKUtbCOHsEmY4GaKLpbowJp+AN2t6rtKaCEPjJ/XuZrBVlQ/h+nl6KU2E1f51qi/yDvs6t7AR6+KwhDbC6sLbxFJix8WMnSoqOS6PO2kizDEoP0YK15D3Xr/yOzFjfeZktFQGlTRBGRwHVctvzmBP8yJMNsfcprkb1MkeTnkDNCydFa7LSjO8H5l0lzPvsC8rLwkzEBbDxFEz+/rfmze1I1fC4F8Mm6jxte1HrnPgyzSPcqrTa99PE6i0CngcVz4qlUqzkhM84TVP8VHvayu9WXHHX/EXuMjQVTbj6qaaIzbzdX1a/4vpXGsF35v4PUSCNKQ0giD9nODUHKf2B/SD1vqIQGw3kZlq3nwMqeT8qkvd5ccMRkH/eic9GyuoUjOw0+y61LPsYwVBFX/e6Qeevd5so7bIJAOsnZhQH6mL1fe4A0EQrR9DK5UaJUkrl6zy7mo8XkVafp4jjXUR5tDbQ50cGFj/nsjwBXrsMAj6ArZOgTDcWm5HROk1PXghNG2NctB6Cz6Z63py/KUBrcl4IMEeW5PvAVTGq3zOahDhOr2IqFBJTi87SpSuMQozJeGd5bZ822CLhbufgCvm+4bY9KzBZy5TMp8wiqi8V5wQ29W6UkmEJfkxm6mwlHEY8DVbNhEmyS7afIgxzdQmBoYz2+psahH7vKTRFZhNbn0kIWbBJAS/hcmExz0lafVUexuOlcwpEfxQbDZiFTkKHHYA3W2iDIa3wRJGPgYTZFlhwmSeXd5o6I3Zz8+L8JSfZmQkhBi07GXKu6HOoZ6t6sMMT6iFyh7fD+aATzhXCX+Cf7DvJpOmqLbbm3ZPx1jMDqRl/gxaZrNj2w3hn8OyxMT8WDFhVIStfPqwVBKGQTuCcFflH234u3BZQSZ/2h5X153aYdpee8phZV9kvavQhNhVSUiwNW1mrii07olY9HbVGt7uxGLEXmhNRFyXFLPSYxnBQSx1KMk4/iZI7pC9miuVW7wFC1HTgg+/IU09A9Mv0d+zZ/DHxYKLt/rxqPe+vvHG08EpUfLhQpDwGuPHh6ZFmMdBTitBb7zxxhtvvPHGG2+88cYbb7zxxhPiH739fNFWzO2iAAAAAElFTkSuQmCC",
# caption="Segitiga adalah bangun datar dua dimensi yang memiliki tiga sisi dan tiga sudut.", width=300)


#  # Input
# alas = st.number_input("Masukkan panjang alas segitiga", min_value=0)
# tinggi = st.number_input("Masukkan panjang tinggi segitiga", min_value=0)
# if st.button("Hitung"):
#         luas = luas_segitiga(alas, tinggi)
#         st.write(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas}")
    


# elif menu == "Luas Lingkaran":
#     st.header("Luas Lingkaran")

# st.image("data:image/png;base64,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",
#          caption="Lingkaran adalah bangun datar dua dimensi yang terdiri dari semua titik yang berjarak sama dari titik pusatnya.", width=300)

# # Input
# jari_jari = st.number_input("Masukkan panjang jari-jari lingkaran", min_value=0)
# if st.button("Hitung"):
#         luas = luas_lingkaran(jari_jari)
#         st.write(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas}")

import streamlit as st

st.set_page_config(page_title="Bangun Datar", page_icon="📐")

st.title("Aplikasi perhitungan bangun datar")
st.write("Silahkan pilih menu di samping untuk memulai")

def luas_persegi(sisi):
    return sisi * sisi

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def luas_lingkaran(jari_jari):
    return 3.14 * jari_jari * jari_jari

# Sidebar
menu = st.sidebar.selectbox("Pilih bangun datar", ("Luas Persegi", "Luas Segitiga", "Luas Lingkaran"))

if menu == "Luas Persegi":
    st.header("Luas Persegi")

    # Image
    st.image("https://cilacapklik.com/wp-content/uploads/2022/06/Rumus-Luas-Dan-Keliling-Persegi.png", caption="Rumus Luas Persegi", width=300)

    # Input
    sisi = st.number_input("Masukkan panjang sisi persegi", min_value=0)
    if st.button("Hitung"):
        luas = luas_persegi(sisi)
        st.write(f"Luas persegi dengan sisi {sisi} adalah {luas}")

elif menu == "Luas Segitiga":
    st.header("Luas Segitiga")

    # Image
    st.image("https://media.suara.com/pictures/970x544/2021/11/11/76640-rumus-luas-segitiga-jadijuaracom.jpg", caption="Rumus Luas Segitiga", width=300)

    # Input
    alas = st.number_input("Masukkan panjang alas segitiga", min_value=0)
    tinggi = st.number_input("Masukkan panjang tinggi segitiga", min_value=0)
    if st.button("Hitung"):
        luas = luas_segitiga(alas, tinggi)
        st.write(f"Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas}")
    
elif menu == "Luas Lingkaran":
    st.header("Luas Lingkaran")

    # Image
    st.image("https://www.nesabamedia.com/wp-content/uploads/2019/04/rumus-luas-lingkarang.png", caption="Rumus Luas Lingkaran", width=300)

    # Input
    jari_jari = st.number_input("Masukkan panjang jari-jari lingkaran", min_value=0)
    if st.button("Hitung"):
        luas = luas_lingkaran(jari_jari)
        st.write(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas}")