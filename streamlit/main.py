import streamlit as st





import os


st.write("# Welcome to the Streamlit App!")

st.write({"key": "value"})


3+4  # Run the app with: streamlit run main.py
77+33/22
"hello world"  # Run the app with: streamlit run main.py




x = st.slider("Select a value")
st.write(x, "squared is", x * x)






# streamlit run main.py --server.port 8501 --server.address

"hello world"  if False else "bye"
# Run the app with: streamlit run main.py --server.port 8501 --server.address
st.progress(0.8)  # Run the app with: streamlit run main.py --server.port 8501 --server.address
st.popover("This is a popover")  # Run the app with: streamlit run main.py --server.port 8501 --server.address




pressed = st.button("Press me")
if pressed:
    st.write("Button was pressed!")
else:
    st.write("Button was not pressed!")

pressed2 = st.button("Press me 2")
print(pressed2, "second button")







st.write("Button 2 was pressed!") if pressed2 else st.write("Button 2 was not pressed!")


# text element  
st.title("Hello World")

st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a text element")
st.markdown("This is a markdown element")
st.latex(r"e^{i\pi} + 1 = 0")
st.code("print('Hello World')", language="python")
st.json({"key": "value"})
st.write("This is a write element")
st.write("This is a write element", "with multiple arguments")
st.caption("This is a caption element")
st.success("This is a success element")
st.error("This is an error element")
st.warning("This is a warning element")
st.info("This is an info element")

# st.exception("This is an exception element")

st.help("This is a help element")



st.spinner("This is a spinner element")

st.balloons()
st.snow()
st.progress(50)
st.empty()

st.sidebar.title("Sidebar")
st.sidebar.header("This is a sidebar header")
st.sidebar.subheader("This is a sidebar subheader")
st.sidebar.text("This is a sidebar text element")
st.sidebar.markdown("This is a sidebar markdown element")
st.divider()

st.image("https://www.streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", caption="Streamlit Logo")


st.image(os.path.join(os.getcwd(), "static" , "bg.jpg"),width=300, caption="Streamlit Logo ahmad")

# dataframe element 
# rervide pandas matplot seaborn plotly altair
options = st.multiselect(
    "What are your favorite colors?",
    ["Green", "Yellow", "Red", "Blue"],
    default=["Yellow", "Red"],
)

st.write("You selected:", options)