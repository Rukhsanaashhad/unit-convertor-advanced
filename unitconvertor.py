import streamlit as st  

# Conversion functions
def length_converter(value, from_unit, to_unit):  
    units = {  
        'meters': 1,  
        'kilometers': 0.001,  
        'miles': 0.000621371,  
        'feet': 3.28084,  
    }  
    return value * (units[to_unit] / units[from_unit])  

def weight_converter(value, from_unit, to_unit):  
    units = {  
        'grams': 1,  
        'kilograms': 0.001,  
        'pounds': 0.00220462,  
        'ounces': 0.035274,  
    }  
    return value * (units[to_unit] / units[from_unit])  

def temperature_converter(value, from_unit, to_unit):  
    if from_unit == 'Celsius':  
        if to_unit == 'Fahrenheit':  
            return value * 9/5 + 32  
        elif to_unit == 'Kelvin':  
            return value + 273.15  
        return value  
    elif from_unit == 'Fahrenheit':  
        if to_unit == 'Celsius':  
            return (value - 32) * 5/9  
        elif to_unit == 'Kelvin':  
            return (value - 32) * 5/9 + 273.15  
        return value  
    elif from_unit == 'Kelvin':  
        if to_unit == 'Celsius':  
            return value - 273.15  
        elif to_unit == 'Fahrenheit':  
            return (value - 273.15) * 9/5 + 32  
        return value  

# Streamlit UI  
st.title("Unit Converter  By Muhammad Ashhad Khan")  

# Select the type of conversion  
conversion_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])  

# Input value  
value = st.number_input("Enter value to convert", 0.0)  

# Conversion input based on the type selected  
if conversion_type == "Length":  
    from_unit = st.selectbox("From unit", ['meters', 'kilometers', 'miles', 'feet'])  
    to_unit = st.selectbox("To unit", ['meters', 'kilometers', 'miles', 'feet'])  
    if st.button("Convert"):  
        result = length_converter(value, from_unit, to_unit)  
        st.header(f"{value} {from_unit} is equal to {result} {to_unit} 📏")  

elif conversion_type == "Weight":  
    from_unit = st.selectbox("From unit", ['grams', 'kilograms', 'pounds', 'ounces'])  
    to_unit = st.selectbox("To unit", ['grams', 'kilograms', 'pounds', 'ounces'])  
    if st.button("Convert"):  
        result = weight_converter(value, from_unit, to_unit)  
        st.header(f"{value} {from_unit} is equal to {result} {to_unit} ⚖️")  

elif conversion_type == "Temperature":  
    from_unit = st.selectbox("From unit", ['Celsius', 'Fahrenheit', 'Kelvin'])  
    to_unit = st.selectbox("To unit", ['Celsius', 'Fahrenheit', 'Kelvin'])  
    if st.button("Convert"):  
        result = temperature_converter(value, from_unit, to_unit)  
        st.header(f"{value} {from_unit} is equal to {result} {to_unit} 🌡️")  
