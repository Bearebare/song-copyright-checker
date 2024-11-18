import streamlit as st
import pandas as pd
import numpy as np
import tempfile
import os

# ตั้งค่าหน้าเว็บ
st.set_page_config(
    page_title="ตรวจสอบลิขสิทธิ์เพลง",
    page_icon="🎵",
    layout="wide"
)

def analyze_song(audio_data):
    """จำลองการวิเคราะห์เพลง"""
    # สร้างข้อมูลจำลอง
    results = {
        'melody_similarity': np.random.uniform(0, 100),
        'rhythm_similarity': np.random.uniform(0, 100),
        'vocal_similarity': np.random.uniform(0, 100),
        'music_similarity': np.random.uniform(0, 100)
    }
    return results

def find_similar_songs():
    """จำลองการค้นหาเพลงที่คล้ายกัน"""
    similar_songs = []
    num_songs = np.random.randint(1, 4)  # สุ่มจำนวนเพลงที่คล้าย 1-3 เพลง
    
    thai_artists = ['เบิร์ด ธงไชย', 'ทาทา ยัง', 'แสตมป์ อภิวัชร์', 'อัสนี-วสันต์', 'ป้าง นครินทร์']
    song_types = ['เพลงป็อป', 'เพลงร็อค', 'เพลงลูกทุ่ง', 'เพลงสตริง', 'เพลงแร็พ']
    
    for _ in range(num_songs):
        similar_songs.append({
            'title': f'เพลง{np.random.choice(["รัก", "เหงา", "คิดถึง", "ใจ", "ฝัน"])}',
            'artist': np.random.choice(thai_artists),
            'type': np.random.choice(song_types),
            'similarity': round(np.random.uniform(70, 99), 2),
            'copyright_owner': f'ค่ายเพลง {np.random.choice(["A", "B", "C", "D"])}'
        })
    
    return similar_songs

def main():
    st.title("🎵 ระบบตรวจสอบลิขสิทธิ์เพลง")
    
    # สร้าง sidebar
    with st.sidebar:
        st.header("📝 คำแนะนำ")
        st.write("""
        1. อัปโหลดไฟล์เพลงของคุณ
        2. รอระบบวิเคราะห์
        3. ตรวจสอบผลการวิเคราะห์
        """)
        
        st.header("⚠️ หมายเหตุ")
        st.write("""
        - รองรับไฟล์ MP3 และ WAV
        - ขนาดไฟล์ไม่เกิน 200MB
        - ใช้เวลาวิเคราะห์ 1-2 นาที
        """)
    
    # ส่วนอัปโหลดไฟล์
    uploaded_file = st.file_uploader("อัปโหลดเพลงของคุณ", type=['mp3', 'wav'])
    
    if uploaded_file:
        # แสดงตัวอย่างเสียง
        st.audio(uploaded_file)
        
        if st.button("🔍 ตรวจสอบการละเมิดลิขสิทธิ์"):
            with st.spinner('กำลังวิเคราะห์เพลง...'):
                # จำลองการวิเคราะห์
                analysis = analyze_song(uploaded_file)
                similar_songs = find_similar_songs()
                
                # แสดงผลการวิเคราะห์
                st.header("📊 ผลการวิเคราะห์")
                
                # แสดงกราฟความคล้ายคลึง
                df_analysis = pd.DataFrame({
                    'องค์ประกอบ': ['ทำนอง', 'จังหวะ', 'เสียงร้อง', 'ดนตรี'],
                    'เปอร์เซ็นต์': [
                        analysis['melody_similarity'],
                        analysis['rhythm_similarity'],
                        analysis['vocal_similarity'],
                        analysis['music_similarity']
                    ]
                })
                
                st.bar_chart(df_analysis.set_index('องค์ประกอบ'))
                
                # แสดงเพลงที่คล้ายคลึง
                st.header("🎵 เพลงที่มีความคล้ายคลึง")
                
                for song in similar_songs:
                    with st.expander(f"🎵 {song['title']} - {song['artist']} ({song['similarity']}% คล้ายคลึง)"):
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.write(f"**ประเภท:** {song['type']}")
                            st.write(f"**เจ้าของลิขสิทธิ์:** {song['copyright_owner']}")
                        
                        with col2:
                            if song['similarity'] >= 90:
                                st.error("⚠️ มีความเสี่ยงสูงในการละเมิดลิขสิทธิ์")
                            elif song['similarity'] >= 80:
                                st.warning("⚡ มีความคล้ายคลึงที่ควรระวัง")
                            else:
                                st.info("ℹ️ มีความคล้ายคลึงบางส่วน")

    # แสดงคำอธิบายเพิ่มเติม
    with st.expander("ℹ️ วิธีการตรวจสอบ"):
        st.write("""
        ระบบจะวิเคราะห์องค์ประกอบต่างๆ ของเพลง:
        
        1. **ทำนอง** 🎼
           - การเรียงลำดับโน้ต
           - การดำเนินทำนอง
        
        2. **จังหวะ** 🥁
           - ความเร็วของเพลง
           - รูปแบบจังหวะ
        
        3. **เสียงร้อง** 🎤
           - ลักษณะการร้อง
           - การออกเสียง
        
        4. **ดนตรี** 🎸
           - การเรียบเรียง
           - เครื่องดนตรีที่ใช้
        """)

if __name__ == "__main__":
    main()
