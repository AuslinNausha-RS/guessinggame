import streamlit as st
#Title and description
st.title("MY PORTFOLIO")
st.write("A showcase of my skills and projects.")

st.header("About Me")
st.subheader("Hello,I am Auslin Nausha")
st.subheader("I am a student of AI&DS")

col1, col2=st.columns([1,2])
with col1:
    st.write(''':green[LANGUAGES KNOWN]
    \n:green[INTERESTED IN]
    \n:green[EXTRA CURICULAR ACTIVITIES]
    \n:green[KNOWN GAMES]
    \n:green[HOBBIES]
    \n:green[AIM]''')
with col2:
    st.write('''\n:  Python
    \n: Coding
    \n: Painting
    \n: Throw ball,Kabbadi
    \n: Listening to music
    \n: Data scientist''')
st.write(":blue[I am passionate about developing projects that solve real-world problems.]")
st.write("""
- **Email**: auslinnausha123@gmail.com
-**Linkedin**:[linkedin.com/in/auslinnausha](https://www.linkedin.com/in/auslin nausha-267b3489)
""")





import streamlit as st
import random

# Set up the title of the app
st.title("Number Guessing Game")

# Define the range for the random number
number_range = st.slider("Select the range for the number:", 1, 100, 50)

# Initialize session state
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, number_range)
    st.session_state.attempts = 0

# Display the number of attempts
st.write(f"You have made {st.session_state.attempts} attempts.")

# Get user input
guess = st.number_input("Enter your guess:", min_value=1, max_value=number_range, step=1)

# Button to submit guess
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number_to_guess:
        st.write("Too low! Try again.")
    elif guess > st.session_state.number_to_guess:
        st.write("Too high! Try again.")
    else:
        st.write(f"Congratulations! You guessed the number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts.")
        # Reset game
        if st.button("Play Again"):
            st.session_state.number_to_guess = random.randit(1, number_range)
            st.session_state.attempts = 0

# Button to reset the game
if st.button("Reset Game"):
    st.session_state.number_to_guess = random.randit(1, number_range)
    st.session_state.attempts = 0
    st.write("Game has been reset. Start guessing!")            








                               
            



