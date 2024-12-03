import streamlit as st
from product_utils import products

# Set the page layout to wide mode
st.set_page_config(page_title='Wilde Wholesale',
                   page_icon='assets/logo_wilde_chips.jpg',
                   layout='wide',
                   initial_sidebar_state='expanded'
)

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
            order_summary.append(f"{qty_134} - 1.34oz {product['name']}")

        # Add 2.25oz orders to the summary
        if qty_225 > 0:
            cost_225 = qty_225 * product["price_225"]
            total += cost_225
            order_summary.append(f"{qty_225} - 2.25oz {product['name']}")

    st.session_state["order_summary"] = order_summary
    st.session_state["total_cost"] = total

# Layout
layout_cols = st.columns([1, 1, 1, 1])

# Products in the first 4 columns
for idx, product in enumerate(products[:3]):
    with layout_cols[idx]:
        title_cols = st.columns([1, 10])
        with title_cols[1]:
            st.markdown(f"<h5 style='text-align: center;'>{product['name']}</h5>", unsafe_allow_html=True)
        st.image(product["main_image"], 
                 width=150,
                 caption=product['description'],
                 output_format = 'PNG',
                 use_column_width=True
                 )
        size_cols = st.columns([1,1,.15])  # Two columns for side-by-side counters
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


# Remaining products in the next row of the first 4 columns
for idx, product in enumerate(products[3:]):
    with layout_cols[idx]:
        title_cols = st.columns([1, 10])
        with title_cols[1]:
            st.markdown(f"<h5 style='text-align: center;'>{product['name']}</h5>", unsafe_allow_html=True)
        st.image(product["main_image"],
                 width=150, 
                 caption=product["description"],
                 output_format = 'PNG',
                 use_column_width=True
                 )
        size_cols = st.columns([1,1,.15])  # Two columns for side-by-side counters
        with size_cols[0]:
            st.number_input(
                f"2.25oz", min_value=0, value=0, step=1, key=f"qty_225_{idx + 3}", on_change=update_order_summary
            )
        with size_cols[1]:
            st.number_input(
                f"1.34oz", min_value=0, value=0, step=1, key=f"qty_134_{idx + 3}", on_change=update_order_summary
            )
        if idx > 2:
            st.write('#')
            # CSS styles for the container
            container_style = """
                <style>
                .custom-container {
                    border: 2px solid #ffffff; /* Change this color to your desired border color */
                    padding: 15px;
                    border-radius: 10px; /* Optional: for rounded corners */
                    background-color: #f9f9f9; /* Optional: to set a background color */
                    margin-top: 15px; /* Optional: to add spacing below the container */
                    margin-bottom: 15px; /* Optional: to add spacing below the container */
                }
                </style>
            """

            # Inject the CSS into the Streamlit app
            st.markdown(container_style, unsafe_allow_html=True)

            with st.container(border=True):
                st.markdown('<center>Sizes Available<br><br>',unsafe_allow_html=True)
                price_cols = st.columns([1,1])
                with price_cols[0]:
                    st.markdown(f"<u>2.25oz</u><br>${product['price_225']:.2f}/cs<br>12 units/cs",unsafe_allow_html=True)
                    st.image('assets/Wilde_Rendering_12ct_Buffalo_09152022.png', width=160, output_format='PNG')
                with price_cols[1]:
                    st.markdown(f"<u>1.34oz</u><br>${product['price_134']:.2f}/cs<br>8 units/cs",unsafe_allow_html=True)
                    st.image('assets/Wilde_1oz_8ct_Carton_Buffalo_06012023.png', width=140, output_format='PNG')

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

# import streamlit as st
# from product_utils import products

# # Set the page layout to wide mode
# st.set_page_config(page_title='Wilde Wholesale',
#                    page_icon='assets/logo_wilde_chips.jpg',
#                    layout='wide',
#                    initial_sidebar_state='expanded'
# )

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

#         if qty_134 > 0:
#             cost_134 = qty_134 * product["price_134"]
#             total += cost_134
#             order_summary.append(f"{qty_134} - 1.34oz {product['name']}")

#         if qty_225 > 0:
#             cost_225 = qty_225 * product["price_225"]
#             total += cost_225
#             order_summary.append(f"{qty_225} - 2.25oz {product['name']}")

#     st.session_state["order_summary"] = order_summary
#     st.session_state["total_cost"] = total

# # Layout
# layout_cols = st.columns([1, 1, 1, 1])  # 4 columns layout

# # Move additional information to the top-left box
# with layout_cols[0]:  # First column in the top row
#     st.markdown('<center><h4>Sizes Available</h4><br><br>', unsafe_allow_html=True)
#     price_cols = st.columns([1, 1])
#     with price_cols[0]:
#         st.markdown(f"<u>2.25oz</u><br><br>${products[0]['price_225']}/cs", unsafe_allow_html=True)
#         st.markdown("12 units/cs", unsafe_allow_html=True)
#         st.image('assets/Wilde_Rendering_12ct_Buffalo_09152022.png', width=160, output_format='PNG')
#     with price_cols[1]:
#         st.markdown(f"<u>1.34oz</u><br><br>${products[0]['price_134']}/cs", unsafe_allow_html=True)
#         st.markdown("8 units/cs", unsafe_allow_html=True)
#         st.image('assets/Wilde_1oz_8ct_Carton_Buffalo_06012023.png', width=140, output_format='PNG')

# # Display products, starting from the second column
# for idx, product in enumerate(products):
#     col_idx = (idx + 1) % 4  # Shift products by 1 column
#     row_idx = (idx + 1) // 4

#     with layout_cols[col_idx]:
#         st.markdown(f"<h5 style='text-align: left;'>{product['name']}</h5>", unsafe_allow_html=True)
#         st.image(product["main_image"], width=150, caption=product["description"], output_format='PNG')
#         size_cols = st.columns([1, 1, 0.15])
#         with size_cols[0]:
#             st.number_input(
#                 f"2.25oz", min_value=0, value=0, step=1, key=f"qty_225_{idx}", on_change=update_order_summary
#             )
#         with size_cols[1]:
#             st.number_input(
#                 f"1.34oz", min_value=0, value=0, step=1, key=f"qty_134_{idx}", on_change=update_order_summary
#             )

# st.sidebar.image('assets/logo_wilde_chips.jpg')
# st.sidebar.divider()
# st.sidebar.markdown("<h4 style='text-align: left;'><u>Shopping Cart</u></h4>", unsafe_allow_html=True)

# for line in st.session_state["order_summary"]:
#     st.sidebar.markdown(line, unsafe_allow_html=True)
# st.sidebar.write('#')
# total_cols = st.sidebar.columns([1, 1])
# with total_cols[0]:
#     st.markdown(f"<h4 style='text-align: left;'> Order Total:</h4>", unsafe_allow_html=True)
# with total_cols[1]:
#     st.markdown(f"<h4 style='text-align: left;'>${st.session_state['total_cost']:.2f}</h4>", unsafe_allow_html=True)

# # Submit button
# if st.sidebar.button("Submit Order", use_container_width=True):
#     st.sidebar.success("Order submitted!")
#     st.sidebar.markdown("Thanks for your order. You'll get it when you get it. Now send us money.", unsafe_allow_html=True)

# # ---- REMOVE UNWANTED STREAMLIT STYLING ----
# hide_st_style = """
#             <style>
#             Main Menu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)
