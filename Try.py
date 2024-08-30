# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:12:53 2024

@author: user
"""

import streamlit as st 

import random

import pickle

filename = "modelbloodloss.pickle"
loaded_model = pickle.load(open(filename, "rb"))



st.markdown("<h1 style='text-align: center; color: black ; font-size: 40px ;'>มาเล่นเกมส์กัน!</h1>", unsafe_allow_html=True)

if "button" not in st.session_state:
        st.session_state.button = ''

if "quiz" not in st.session_state:
        st.session_state.quiz = ''


if "ans" not in st.session_state:
        st.session_state.ans = ''




sex = ['หญิง','ชาย' ]
UD = ['ความดันโลหิตสูง','หัวใจขาดเลือด','เบาหวาน','ไตวายเรื้อรัง']
cement =['ไม่ใส่cement','ใส่cement']
ASA = ['I','II','III','IV','V']
side = ['ซ้าย','ขวา']

a = random.randint(60,100)
b = random.choice(sex)
c = random.choice(UD)
d = random.choice(ASA)
e = random.choice(cement)
f = random.choice(side)

if st.button('**เลือกคนไข้ได้เลย!**'):
    #value1 = f"ผู้ป่วย{b} อายุ {a} ปี โรคประจำตัว{c} ASA class {d} สะโพก{f}หัก แพทย์ set ผ่าตัดข้อเทียมแบบ {e}"
    st.session_state['button'] = f"ผู้ป่วย{b} อายุ{a}ปี โรคประจำตัว{c} ASA class {d} สะโพก{f}หัก แพทย์ set ผ่าตัดข้อเทียมแบบ {e}"
    
st.write(st.session_state['button'])    
    
            
        
quiz = st.radio("**ผู้ป่วยเสี่ยงต่อการให้เลือดหรือไม่**", ["ไม่มีความเสี่ยง" , "มีความเสี่ยง"],  horizontal = True)
if st.button('**ส่งคำตอบ**'):
    if quiz == "ไม่มีความเสี่ยง" :
        #solution  = int(0)
        st.session_state['quiz'] = 'คุณตอบว่าผู้ป่วยมีความเสี่ยงน้อยที่จะเสียเลือด'
        #st.write(":green[คุณตอบว่าผู้ป่วยมีความเสี่ยงน้อยที่จะเสียเลือด]")
   
    else :
        #solution  = int(1)
        st.session_state['quiz'] = 'คุณตอบว่าผู้ป่วยมีความเสี่ยงมากที่จะเสียเลือด'
        #st.write(":red[คุณตอบว่าผู้ป่วยมีความเสี่ยงมากที่จะเสียเลือด]") 
        
st.session_state['quiz']


st.markdown("<h1 style='text-align: center; color: black ; font-size: 25px ;'>Blood Loss Assessment by Samutsakhon Tool (BLAST)</h1>", unsafe_allow_html=True)


q1 = st.radio("**เพศ**", ["ชาย" , "หญิง"],  horizontal = True)
if q1 == "ชาย" :
    a = int(1)
else :
    a = int(0)
    
q2 = st.radio("**ผู้ป่วยเป็นโรคไตหรือไม่**" , ["ไม่เป็น" , "เป็น"],  horizontal = True)
if q2 == "ไม่เป็น" :
    b = int(0)
else :
    b = int(1)
    
q3 = st.radio("**ผู้ป่วยเป็นโรคหัวใจขาดเลือดหรือไม่**" , ["ไม่เป็น" , "เป็น"],  horizontal = True)
if q3 == "ไม่เป็น" :
    c = int(0)
else :
    c = int(1)
    
q4 = st.radio("**การผ่าตัดนี้ใส่ cementหรือไม่**" , ["ไม่ใส่" , "ใส่"],  horizontal = True)
if q4 == "ไม่ใส่" :
    d = int(0)
else :
    d = int(1)
    
    
st.markdown(

"""
ให้ท่านประเมิน ASA Clsss ของผู้ป่วย โดย
- ASA Class I หมายความว่า ผู้ป่วยแข็งแรงดีไม่มีโรคประจำตัว
- ASA Class II หมายความว่า ผู้ป่วยที่มีโรคประจำตัวอยู่ในระดับรุนแรงน้อยและควบคุมได้ดี
- ASA Class III หมายความว่า ผู้ป่วยมีโรคประจำตัวอยู่ในระดับปานกลางถึงรุนแรง ควบคุมได้ไม่ดี
- ASA Class IV หมายความว่า  ผู้ป่วยที่มีโรคประจำตัวที่มีอาการรุนแรง มีอัตราเสี่ยงต่อการเสียชีวิตสูง
- ASA Class V หมายความว่า ผู้ป่วยในระยะสุดท้ายที่มีโอกาสตายได้ภายใน 24 ชั่วโมง
ไม่ว่าจะได้รับการผ่าตัดหรือไม่
"""

)
    

q5 = st.radio("**ผู้ป่วยเป็น ASA Classใด**" , ["I" , "II", "III", "IV", "V"],  horizontal = True)
if q5 == "I" :
    e = int(1)
elif q5 == "II" :
    e = int(2)    
elif q5 == "III" :
    e = int(3) 
elif q5 == "IV" :
    e = int(4)
else :
    e = int(5)  
    

    
if st.button('**ประเมินความเสี่ยง**'):
    s=[a,b,c,d,e]
    array = loaded_model.predict([s])
    k=loaded_model.predict_proba([s]).round(2)
    if array[0] == 0: 
           st.session_state['ans'] = 'ผู้ป่วยมีความเสี่ยงน้อยที่จะเสียเลือด ควรจองเลือดไม่เกิน 1 U '
           #st.write(f":green[ผู้ป่วยมีความเสี่ยงน้อยที่จะเสียเลือด ควรจองเลือดไม่เกิน 1 U ค่าความเชื่อมั่น {k[0][0]*100}%]")
    else:
           st.session_state['ans'] = 'ผู้ป่วยมีความเสี่ยงที่จะเสียเลือด ควรจองเลือด 2 U ขึ้นไป'
           #st.write(f":red[ผู้ป่วยมีความเสี่ยงที่จะเสียเลือด ควรจองเลือด 2 U ขึ้นไป ค่าความเชื่อมั่น {k[0][1]*100}%]")

st.write(st.session_state['ans'])

if  st.session_state['button'] ==  ''  or  st.session_state['quiz'] == ''  or   st.session_state['ans'] == '':
    
    st.write("")

elif st.session_state['ans'] == 'ผู้ป่วยมีความเสี่ยงน้อยที่จะเสียเลือด ควรจองเลือดไม่เกิน 1 U ' and  st.session_state['quiz'] == 'คุณตอบว่าผู้ป่วยมีความเสี่ยงน้อยที่จะเสียเลือด'   :
    
    st.markdown(":rainbow[ยินดีด้วย คุณตอบถูก รับรางวัลไปเลย!]:tada::gift:")
    
elif st.session_state['ans'] == 'ผู้ป่วยมีความเสี่ยงที่จะเสียเลือด ควรจองเลือด 2 U ขึ้นไป' and st.session_state['quiz'] == 'คุณตอบว่าผู้ป่วยมีความเสี่ยงมากที่จะเสียเลือด'  :
    
    st.markdown(":rainbow[ยินดีด้วย คุณตอบถูก รับรางวัลไปเลย!]:tada::gift:")
        
else :
    
    st.write("เสียใจด้วย คุณตอบผิด  ลองใหม่อีกครั้งนะคะ")
