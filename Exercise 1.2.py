import streamlit as st

st.title("🍔 Food Ordering System")

# Input fields
customer_name = st.text_input("Enter Customer Name")

food_menu = {
    "Nasi Lemak": 5,
    "Chicken Chop": 12,
    "Burger": 8
}

food_selection = st.selectbox(
    "Select Food",
    list(food_menu.keys())
)

quantity = st.number_input("Enter Quantity", min_value=0, step=1)

# Button
if st.button("Order"):
    try:
        # Validation
        if customer_name.strip() == "":
            raise ValueError("Customer name cannot be empty!")

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0!")

        price = food_menu[food_selection]
        total_price = price * quantity

        # Display result
        st.success("✅ Order Successful!")
        st.write("### Order Details")
        st.write(f"👤 Name: {customer_name}")
        st.write(f"🍽️ Food: {food_selection}")
        st.write(f"🔢 Quantity: {quantity}")
        st.write(f"💰 Total Price: RM {total_price:.2f}")

    except ValueError as ve:
        st.error(f"❌ Error: {ve}")
    except Exception as e:
        st.error("❌ Unexpected error occurred!")
  
