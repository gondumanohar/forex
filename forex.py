import streamlit as st
from forex_python.converter import CurrencyRates, CurrencyCodes

# Initialize CurrencyRates and CurrencyCodes objects
c = CurrencyRates()
codes = CurrencyCodes()

# Title of the application
st.title("Currency Converter")

# Input fields for currency codes and amount
amount = st.number_input("Enter the amount to convert:", min_value=0.0, step=0.01)
from_currency = st.text_input("From Currency (e.g., USD):", value="USD").upper()
to_currency = st.text_input("To Currency (e.g., EUR):", value="EUR").upper()

# Button to trigger conversion
if st.button("Convert"):
    try:
        if amount > 0:
            # Fetch the conversion rate
            converted_amount = c.convert(from_currency, to_currency, amount)
            symbol = codes.get_symbol(to_currency)

            st.success(f"{amount} {from_currency} = {symbol} {converted_amount:.2f} {to_currency}")
        else:
            st.error("Please enter an amount greater than 0.")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Footer
st.write("Powered by Streamlit & forex-python")
