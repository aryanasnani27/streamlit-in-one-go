import streamlit as st                                                          
st.title('Title -> Learning About Streamlit')
st.header('Header -> GeeksForGeeks')
st.subheader('Subheader -> GeeksForGeeks')
st.text('Text -> GeeksForGeeks')
 
st.markdown('#Hi')

st.success('Success')
st.info('Information!')
st.warning('Warning!')
st.error('Error!')

st.exception(ZeroDivisionError('Div not possible'))
st.help(ZeroDivisionError)

st.write('range(1,10)')
st.write(range(1,10))
st.write(1*2*3)

st.subheader('Code')
st.code('x=10\n'
        'for i in range(x):\n'
            "\tprint(i,end=' ')")
st.code('Output\n'
        '0 1 2 3 4 5 6 7 8 9')

st.subheader('Checkbox')
st.checkbox('Male')

if(st.checkbox('Adult')):
    st.write("You're an adult" )

st.subheader('RadioButton')
#st.radio('Select :',('Male','Female','Other'))
radioButton=st.radio('Select :',('Male','Female','Other'))
if(radioButton=='Male'):
    st.write("You're a Male")
elif(radioButton=='Female'):
    st.write("You're a female")
elif(radioButton=='Other'):
    st.write("You're an other gender")

st.subheader('Select Box')
selectbox=st.selectbox('Data Science: ',['Data Analysis','Web Scrapping','Machine Learning',
                               'Deep Learning','Natural Language PRocessing',
                               'Comuter vision','Image Processing'])
st.write("You've selected: ",selectbox)

st.subheader('Multi Select Box')
multiselect=st.multiselect('Data Science: ',['Data Analysis','Web Scrapping','Machine Learning',
                               'Deep Learning','Natural Language PRocessing',
                               'Comuter vision','Image Processing'])
st.write("You've selected: ",len(multiselect),'courses')

st.subheader('Button')
#st.button('click me')
if(st.button('Click me')):
    st.write('Thanks for clicking me!')

st.subheader('Slider')
vol=st.slider('Select the Volume:',1,100,step=1)
st.write('The volume is',vol)

st.subheader('Text input')
username=st.text_input('Name: ')
username=st.text_input('Password: ',type='password')

st.subheader('Text Area')
textarea=st.text_area('Write something interesting about yourself in 20 words',max_chars=20,placeholder="Enter the text")
st.write(textarea)

st.subheader('Input number')
age=st.number_input('Select your age',18,100)
st.write('Your age is: ',age)

st.subheader('Input Date')
st.date_input('Enter your DOB')

st.subheader('Input Time')
st.time_input('Time')
