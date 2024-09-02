import streamlit as st

# Title of the application
st.title("Tip Calculator")

# Input fields for bill amount and tip percentage
bill_amount = st.number_input("Enter the total bill amount (in $):", min_value=0.0, step=0.01)
tip_percentage = st.slider("Tip Percentage:", min_value=0, max_value=100, value=15)

# Button to calculate tip
if st.button("Calculate Tip"):
    if bill_amount > 0:
        tip_amount = bill_amount * (tip_percentage / 100)
        total_amount = bill_amount + tip_amount
        
        st.success(f"Tip Amount: ${tip_amount:.2f}")
        st.info(f"Total Amount (including tip): ${total_amount:.2f}")
    else:
        st.error("Please enter a valid bill amount.")

# Footer
st.write("Powered by Streamlit")
