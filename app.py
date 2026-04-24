import streamlit as st

st.title("Simple Calculator")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)
op = st.selectbox("Choose operator", ["+", "-", "*", "/"])

if st.button("Calculate"):
    match (op, num2):
        case ('+', _):
            result = num1 + num2
        case ('-', _):
            result = num1 - num2
        case ('*', _):
            result = num1 * num2
        case ('/', 0):
            result = "Error: Division by zero"
        case ('/', _):
            result = num1 / num2
        case _:
            result = "Invalid operator"

    st.write("Result:", result)