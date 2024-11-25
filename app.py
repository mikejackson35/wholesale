# import streamlit as st
# from product_utils import products

# # Set the page layout to wide mode
# st.set_page_config(layout="wide")

# # Initialize order summary state
# if "order_summary" not in st.session_state:
#     st.session_state["order_summary"] = []

# if "total_cost" not in st.session_state:
#     st.session_state["total_cost"] = 0.0

# # Define a function to update the order summary
# def update_order_summary():
#     order_summary = []
#     total = 0.0

#     for idx, product in enumerate(products):
#         qty_134 = st.session_state.get(f"qty_134_{idx}", 0)
#         qty_225 = st.session_state.get(f"qty_225_{idx}", 0)

#         # Add 1.34oz orders to the summary
#         if qty_134 > 0:
#             cost_134 = qty_134 * product["price_134"]
#             total += cost_134
#             order_summary.append(f"1.34oz {product['name']}: {qty_134} x ${product['price_134']:.2f} = ${cost_134:.2f}")

#         # Add 2.25oz orders to the summary
#         if qty_225 > 0:
#             cost_225 = qty_225 * product["price_225"]
#             total += cost_225
#             order_summary.append(f"2.25oz {product['name']}: {qty_225} x ${product['price_225']:.2f} = ${cost_225:.2f}")

#     st.session_state["order_summary"] = order_summary
#     st.session_state["total_cost"] = total

# # Layout: row1 for products and summary, row2 for the submit button
# row1_cols = st.columns(5)
# row2_cols = st.columns(5)

# # Logo and title in column 1 of row 1
# with row1_cols[0]:
#     st.image('assets/logo_wilde_chips.jpg', width=200)
#     st.markdown("<h4 style='text-align: left;'>Wholesale</h4>", unsafe_allow_html=True)

# # Products in columns 2-4 of row 1
# for idx, product in enumerate(products[:3]):
#     with row1_cols[idx + 1]:
#         st.markdown(f"<h4 style='text-align: left;'>{product['name']}</h4>", unsafe_allow_html=True)
#         st.image(product["main_image"], width=200)
#         st.write(product["description"])
#         size_cols = st.columns([2,2,1])  # Two columns for side-by-side counters
#         with size_cols[0]:
#             st.number_input(
#                 f"1.34oz", min_value=0, value=0, step=1, key=f"qty_134_{idx}", on_change=update_order_summary
#             )
#         with size_cols[1]:
#             st.number_input(
#                 f"2.25oz", min_value=0, value=0, step=1, key=f"qty_225_{idx}", on_change=update_order_summary
#             )

# # Order summary in column 5 of row 1
# with row1_cols[4]:
#     st.header("Shopping Cart")
#     for line in st.session_state["order_summary"]:
#         st.markdown(line, unsafe_allow_html=True)
#     st.markdown(f"### Total Cost: **${st.session_state['total_cost']:.2f}**", unsafe_allow_html=True)

# # Remaining products in columns 1-4 of row 2
# for idx, product in enumerate(products[3:]):
#     with row2_cols[idx]:
#         st.markdown(f"<h4 style='text-align: left;'>{product['name']}</h4>", unsafe_allow_html=True)
#         st.image(product["main_image"], width=200)
#         st.write(product["description"])
#         size_cols = st.columns([2,2,1])  # Two columns for side-by-side counters
#         with size_cols[0]:
#             st.number_input(
#                 f"1.34oz", min_value=0, value=0, step=1, key=f"qty_134_{idx + 3}", on_change=update_order_summary
#             )
#         with size_cols[1]:
#             st.number_input(
#                 f"2.25oz", min_value=0, value=0, step=1, key=f"qty_225_{idx + 3}", on_change=update_order_summary
#             )

# # Submit button in column 5 of row 2
# with row2_cols[4]:
#     if st.button("Submit Order"):
#         st.success("Order submitted!")
#         st.markdown(f"Thanks for your order. <br>You'll get it when you get it. <br>Now send us money.",unsafe_allow_html=True)

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
            order_summary.append(f"{qty_134} - 1.34oz {product['name']} @ ${cost_134:.2f}cs")

        # Add 2.25oz orders to the summary
        if qty_225 > 0:
            cost_225 = qty_225 * product["price_225"]
            total += cost_225
            order_summary.append(f"{qty_225} - 2.25oz {product['name']} @ ${cost_225:.2f}cs")

    st.session_state["order_summary"] = order_summary
    st.session_state["total_cost"] = total

# Layout: 4 columns for products, 1 column for shopping cart and submit button
layout_cols = st.columns([1, 1, 1, 1])  # Last column is wider for the cart and button

# Products in the first 4 columns
for idx, product in enumerate(products[:3]):
    with layout_cols[idx]:
        st.markdown(f"<h4 style='text-align: left;'>{product['name']}</h4>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, .5])
        with col1:
            st.image(product["image_134"], width=125)
        with col2:
            st.image(product["image_225"], width=125)

        st.write(product["description"])
        size_cols = st.columns([1,1,.5])  # Two columns for side-by-side counters
        with size_cols[0]:
            st.number_input(
                f"2.25oz", min_value=0, value=0, step=1, key=f"qty_225_{idx}", on_change=update_order_summary
            )
        with size_cols[1]:
            st.number_input(
                f"1.34oz", min_value=0, value=0, step=1, key=f"qty_134_{idx}", on_change=update_order_summary
            )

# Products in the first 4 columns
for idx, product in enumerate(products[:3]):
    with layout_cols[idx]:
        st.write('#')
        st.write('#')


# Remaining products in the next row of the first 4 columns
for idx, product in enumerate(products[3:]):
    with layout_cols[idx]:
        st.markdown(f"<h4 style='text-align: left;'>{product['name']}</h4>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, .5])
        with col1:
            st.image(product["image_134"], width=125)
        with col2:
            st.image(product["image_225"], width=125)

        st.write(product["description"])
        size_cols = st.columns([1,1,.5])  # Two columns for side-by-side counters
        with size_cols[0]:
            st.number_input(
                f"2.25oz", min_value=0, value=0, step=1, key=f"qty_225_{idx + 3}", on_change=update_order_summary
            )
        with size_cols[1]:
            st.number_input(
                f"1.34oz", min_value=0, value=0, step=1, key=f"qty_134_{idx + 3}", on_change=update_order_summary
            )
# Unified Shopping Cart and Submit Button in the far-right column
# with layout_cols[5]:
#     st.header("Empty")
#     for line in st.session_state["order_summary"]:
#         st.markdown(line, unsafe_allow_html=True)
#     st.markdown(f"### Total Cost: **${st.session_state['total_cost']:.2f}**", unsafe_allow_html=True)

#     # Submit button
#     if st.button("Submit Order"):
#         st.success("Order submitted!")
#         st.markdown(f"Thanks for your order. <br>You'll get it when you get it. <br>Now send us money.", unsafe_allow_html=True)

st.sidebar.image('assets/logo_wilde_chips.jpg')#, width=200)
st.sidebar.divider()
st.sidebar.markdown("<h4 style='text-align: left;'><u>Shopping Cart</h4>", unsafe_allow_html=True)
for line in st.session_state["order_summary"]:
    st.sidebar.markdown(line, unsafe_allow_html=True)
st.sidebar.write('#')
total_cols = st.sidebar.columns([1, 1])
with total_cols[0]:
    st.markdown(f"<h4 style='text-align: left;'> Order Total:", unsafe_allow_html=True)
with total_cols[1]:
    st.markdown(f"<h4 style='text-align: left;'>${st.session_state['total_cost']:.2f}", unsafe_allow_html=True)

# Submit button
if st.sidebar.button("Submit Order",use_container_width = True):
    st.sidebar.success("Order submitted!")
    st.sidebar.markdown(f"Thanks for your order. <br>You'll get it when you get it. <br>Now send us money.", unsafe_allow_html=True)

# ---- REMOVE UNWANTED STREAMLIT STYLING ----
hide_st_style = """
            <style>
            Main Menu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
            
st.markdown(hide_st_style, unsafe_allow_html=True)