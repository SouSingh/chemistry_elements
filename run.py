import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import json


predefined_properties = {
    "hydrogen": {
        "Symbol": "H",
        "Atomic_Number": "1",
        "Atomic_Weight": "1.00794",
        "Density": "0.0899",
        "Melting_Point": "14.01",
        "Boiling_Point": "20.28",
        "Phase": "Gas",
        "Absolute_Melting_Point": "14.01"
    },
    "carbon": {
        "Symbol": "C",
        "Atomic_Number": "6",
        "Atomic_Weight": "12.011",
        "Density": "2.267",
        "Melting_Point": "3550",
        "Boiling_Point": "4827",
        "Phase": "Solid",
        "Absolute_Melting_Point": "3550"
    },
    "sodium": {
        "Symbol": "Na",
        "Atomic_Number": "11",
        "Atomic_Weight": "22.98977",
        "Density": "0.971",
        "Melting_Point": "97.72",
        "Boiling_Point": "883",
        "Phase": "Solid",
        "Absolute_Melting_Point": "97.72"
    },
    "silicon": {
        "Symbol": "Si",
        "Atomic_Number": "14",
        "Atomic_Weight": "28.085",
        "Density": "2.329",
        "Melting_Point": "1414",
        "Boiling_Point": "2900",
        "Phase": "Solid",
        "Absolute_Melting_Point": "1414"
    },
    "sulfur": {
        "Symbol": "S",
        "Atomic_Number": "16",
        "Atomic_Weight": "32.07",
        "Density": "2.07",
        "Melting_Point": "115.21",
        "Boiling_Point": "444.6",
        "Phase": "Solid",
        "Absolute_Melting_Point": "115.21"
    },
    "calcium": {
        "Symbol": "Ca",
        "Atomic_Number": "20",
        "Atomic_Weight": "40.078",
        "Density": "1.54",
        "Melting_Point": "842",
        "Boiling_Point": "1484",
        "Phase": "Solid",
        "Absolute_Melting_Point": "842"
    },
    "iron": {
        "Symbol": "Fe",
        "Atomic_Number": "26",
        "Atomic_Weight": "55.845",
        "Density": "7.874",
        "Melting_Point": "1538",
        "Boiling_Point": "2862",
        "Phase": "Solid",
        "Absolute_Melting_Point": "1538"
    }
}

# Load the model and tokenizer
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("Sourabh2/Chemical_compund", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("Sourabh2/Chemical_compund", trust_remote_code=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    return tokenizer, model, device

tokenizer, model, device = load_model()

# Function to convert the output to JSON format
def convert_to_json(input_string):
    try:
        element, properties_str = input_string.split(' | ', 1)
        properties_list = properties_str.strip("[]").split(", ")
        properties_dict = {key.strip(): value.strip() if value.strip() else None for prop in properties_list for key, value in [prop.split(": ", 1)]}
        json_data = {element: properties_dict}
        return json.dumps(json_data, indent=4)
    except ValueError:
        return json.dumps({"error": "Invalid format in model output"}, indent=4)

# Function to generate chemical properties
def chemical_state(element):
    input_str = element.lower()
    input_ids = tokenizer.encode(input_str, return_tensors='pt').to(device)
    output = model.generate(
        input_ids,
        max_length=300,
        num_return_sequences=1,
        do_sample=True,
        top_k=8,
        top_p=0.95,
        temperature=0.1,
        repetition_penalty=1.2
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Streamlit app interface
st.title("Chemical Properties Generator")
material_name = st.text_input("Enter the name of the material (e.g., Nitrogen):", "Nitrogen")

if st.button("Generate"):
    with st.spinner("Generating chemical properties..."):
        if material_name.lower() in predefined_properties:
            json_result = json.dumps({material_name.capitalize(): predefined_properties[material_name.lower()]}, indent=4)
        else:
            input_string = chemical_state(material_name)
            json_result = convert_to_json(input_string)
        
        st.json(json.loads(json_result))


        # Option to download the JSON result
        st.download_button(
            label="Download JSON",
            data=json_result,
            file_name=f"{material_name.lower()}_properties.json",
            mime="application/json"
        )
