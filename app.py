import streamlit as st
from product_utils import products

# Set the page layout to wide mode
st.set_page_config(layout="wide")

# Initialize order summary state
if "order_summary" not in st.session_state:
    st.session_state["order_summary"] = []

if "total_cost" not in st.session_state:
    st.session_state["total_cost"] = 0.0

# Define a function to update the order summary
def update_order_summary():
    order_summary = []
    total = 0.0

    for idx, product in enumerate(products):
        qty_134 = st.session_state.get(f"qty_134_{idx}", 0)
        qty_225 = st.session_state.get(f"qty_225_{idx}", 0)

        # Add 1.34oz orders to the summary
        if qty_134 > 0:
            cost_134 = qty_134 * product["price_134"]
            total += cost_134
            order_summary.append(f"1.34oz {product['name']}: {qty_134} x ${product['price_134']:.2f} = ${cost_134:.2f}")

        # Add 2.25oz orders to the summary
        if qty_225 > 0:
            cost_225 = qty_225 * product["price_225"]
            total += cost_225
            order_summary.append(f"2.25oz {product['name']}: {qty_225} x ${product['price_225']:.2f} = ${cost_225:.2f}")

    st.session_state["order_summary"] = order_summary
    st.session_state["total_cost"] = total

# Layout: row1 for products and summary, row2 for the submit button
row1_cols = st.columns(5)
row2_cols = st.columns(5)

# Logo and title in column 1 of row 1
with row1_cols[0]:
    st.image('assets/logo_wilde_chips.jpg', width=200)
    st.markdown("<h4 style='text-align: left;'>Wholesale</h4>", unsafe_allow_html=True)

# Products in columns 2-4 of row 1
for idx, product in enumerate(products[:3]):
    with row1_cols[idx + 1]:
        st.markdown(f"<h4 style='text-align: left;'>{product['name']}</h4>", unsafe_allow_html=True)
        st.image(product["main_image"], width=200)
        st.write(product["description"])
        size_cols = st.columns([2,2,1])  # Two columns for side-by-side counters
        with size_cols[0]:
            st.number_input(
                f"1.34oz", min_value=0, value=0, step=1, key=f"qty_134_{idx}", on_change=update_order_summary
            )
        with size_cols[1]:
            st.number_input(
                f"2.25oz", min_value=0, value=0, step=1, key=f"qty_225_{idx}", on_change=update_order_summary
            )

# Order summary in column 5 of row 1
with row1_cols[4]:
    st.header("Shopping Cart")
    for line in st.session_state["order_summary"]:
        st.markdown(line, unsafe_allow_html=True)
    st.markdown(f"### Total Cost: **${st.session_state['total_cost']:.2f}**", unsafe_allow_html=True)

# Remaining products in columns 1-4 of row 2
for idx, product in enumerate(products[3:]):
    with row2_cols[idx]:
        st.markdown(f"<h4 style='text-align: left;'>{product['name']}</h4>", unsafe_allow_html=True)
        st.image(product["main_image"], width=200)
        st.write(product["description"])
        size_cols = st.columns([2,2,1])  # Two columns for side-by-side counters
        with size_cols[0]:
            st.number_input(
                f"1.34oz", min_value=0, value=0, step=1, key=f"qty_134_{idx + 3}", on_change=update_order_summary
            )
        with size_cols[1]:
            st.number_input(
                f"2.25oz", min_value=0, value=0, step=1, key=f"qty_225_{idx + 3}", on_change=update_order_summary
            )

# Submit button in column 5 of row 2
with row2_cols[4]:
    if st.button("Submit Order"):
        st.success("Order submitted!")
        st.markdown(f"Thanks for your order. <br>You'll get it when you get it. <br>Now send us money.",unsafe_allow_html=True)