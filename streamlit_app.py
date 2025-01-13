import streamlit as st
from neuron import Neuron

st.image("img/neurona.jpg", width=400)
st.header("Neuron Simulator")

inputs = st.slider("Choose the number of inputs/weights for the neuron", 1, 10, 1)

st.title("Weights")
w = []

for i in range(inputs):
    st.markdown(f"w<sub>{i}</sub>", unsafe_allow_html=True)
    weight = st.number_input(f"Weight {i+1}", value=0.0)
    w.append(weight)

st.text("Weights: " + str(w))

st.title("Inputs")
x = []

for i in range(inputs):
    st.markdown(f"x<sub>{i}</sub>", unsafe_allow_html=True)
    input = st.number_input(f"Input {i+1}", value=0.0)
    x.append(input)

st.text("Inputs: " + str(x))

col1, col2 = st.columns(2)

with col1:
    st.title("Bias")
    b = st.number_input("Enter the value of the bias", value=0.0)

with col2:
    st.subheader("Select the activation function")
    
    activation_function = st.selectbox("Choose the activation function",
        ("Sigmoide", "ReLU", "Hiperbolic Tangent", "Binary Step"))
    

activation_function_map = {
    "Sigmoide": "sigmoid",
    "ReLU": "relu",
    "Hiperbolic Tangent": "tanh",
    "Binary Step": "binary_step"
}

if st.button("Calculate Output"):
    neuron = Neuron(weights=w, bias=b, activation_function_name=activation_function_map[activation_function])
    try:
        output = neuron.run(x)
        st.success(f"Neuron output: {output}")
    except ValueError as e:
        st.error(e)