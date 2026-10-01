import streamlit as st

# Set the title of the app
st.title("Streamlit Input Components Demo ")

name = st.text_input("Enter your name:")
st.write(f"Hello, {name}!")

age = st.number_input("Enter your age:", min_value=0, max_value=120)
st.write(f"You are {age} years old.")

#button click event
if st.button("Submit"):
    st.write(f"Thank you, {name}, for submitting your age of {age}.")


#Selectbox example
color = st.selectbox("Select your favorite color:", ["Red", "Green", "Blue"])
st.write(f"Your favorite color is {color}.")

#Checkbox example
if st.checkbox("I agree to the terms and conditions"):
    st.write("You agreed to the terms and conditions.") 

#Showing messages
st.success("This is a success message.")
st.warning("This is a warning message.")
st.error("This is an error message.")
st.info("This is an informational message.")
