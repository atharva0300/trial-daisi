import pydaisi as pyd
import streamlit as st
import summary as s

# the hello function is the new endpoint
# everytime, the hello API method is called, this method will be called and executed
def hello(name = 'World') : 
    # returns a string
    return 'Hello ' + str(name) + '! Glad to meet you'


'''

No endpoints will be created for classes definition
No endpoints will be created for classes methods
No endpoints will be created for module privates (whith name starting with an _ or __)


'''
def st_ui(): 
    # predefined method of streamlit to design the App in the dashboard
    name = st.text_input('Type your name ' , value = 'Daisi user')
    greeting = hello(name)
    # invoke the hello function and store the return message in greeting variable
    st.header(greeting)
    # display the greeting in header format
    # just like saying h1 greeting or h2 greeting in html language

    with st.expender("Summary") : 
        # creates an expander named summary
        st.markdown(s.get_summary(name))
        # the the summary


if __name__ =='__main__' : 
    st_ui()