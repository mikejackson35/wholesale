import streamlit as st

# Set the page layout to wide mode
st.set_page_config(layout="wide")

# Define product details
products = [
    {"name": "Buffalo", "main_image": "assets/Wilde_1.34oz_Buffalo_WithoutShadow_02242023.png", "description": "Tangy buffalo meets spicy cayenne pepper for a mouthwatering flavor that packs a punch. It's everything you love about wing night, minus the sauce-covered fingers.", "price": 13.60},
    {"name": "Chicken & Waffles", "main_image": "assets/Wilde_1.34oz_CW_WithoutShadow_02242023.png", "description": "These Chicken & Waffles Protein Chips are equal parts savory and sweet—with a hint of buttery maple syrup—all wrapped into one crunchy, low-carb bite.", "price": 13.60},
    {"name": "BBQ", "main_image": "assets/Wilde_1.34oz_BBQ_WithoutShadow_02242023.png", "description": "Savory, slow-cooked chicken breast meets tangy BBQ resulting in truly unreal flavor. These BBQ Chicken Protein Chips will be the MVP of your next tailgate.", "price": 13.60},
    {"name": "Sea Salt Vinegar", "main_image": "assets/Wilde_1.34oz_SSV_WithoutShadow_02242023.png", "description": "Our crispy Sea Salt & Vinegar Protein Chips have that added zest to make your mouth pucker with each bite and keep you reaching back in the bag for more.", "price": 13.60},
    {"name": "Himalayan Pink Salt", "main_image": "assets/Wilde_1.34oz_Pink_WithoutShadow_02242023.png", "description": "The simplicity and crunch of a traditional potato chip, minus the potatoes. Our Himalayan Pink Salt Protein Chips deliver flavor AND nutrition.", "price": 13.60},
    {"name": "Spicy Queso", "main_image": "assets/Wilde_1.34oz_NashvilleHot_WithoutShadow_02242023.png", "description":"Hints of smoked chipotle and roasted jalapeño blend with a delicious melty, aged cheddar cheese to create the perfect snack with just the right amount of heat.", "price": 13.60},
    {"name": "Nashville Hot", "main_image": "assets/Wilde_1.34oz_NashvilleHot_WithoutShadow_02242023.png", "description": "With the perfect blend of aged Tabasco red peppers and paprika, our Nashville Hot Protein Chips bring the heat and flavor from the Music City's most famous dish.", "price": 13.60},
]

# Form for ordering products
with st.form("order_form"):
    # Add the company logo and title in the first column
    row1_cols = st.columns(5)  # 5 columns in row 1

    with row1_cols[0]:  # First column for logo and title
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.image('assets/logo_wilde_chips.jpg', width=200)
        st.markdown("<h4 style='text-align: left;'>Wholesale</h4>", unsafe_allow_html=True)

    # Columns 2-4 for the first 3 products
    for idx, product in enumerate(products[:3]):
        with row1_cols[idx + 1]:
            st.markdown(f"<h4 style='text-align: left;'>{product['name']}</h4>", unsafe_allow_html=True)
            st.image(product["main_image"], width=200)
            desc_cols = st.columns([3,1])
            with desc_cols[0]:
                st.write(product["description"])
            with desc_cols[1]:
                st.write(" ")
            size_cols = st.columns([2,2,1])
            with size_cols[0]:
                st.number_input(f"1.34oz", min_value=0, value=0, step=1, key=f"qty_134_{idx}")
            with size_cols[1]:
                st.number_input(f"2.25oz", min_value=0, value=0, step=1, key=f"qty_225_{idx}")

    # Fifth column (column 5 in row 1) for the order summary placeholder
    with row1_cols[4]:
        st.header("Order Summary")
        summary_placeholder = st.empty()

    # Row 2: Display the remaining 4 products
    row2_cols = st.columns(5)  # Only 4 columns in row 2
    for idx, product in enumerate(products[3:]):
        with row2_cols[idx]:
            st.markdown(f"<h4 style='text-align: left;'>{product['name']}</h4>", unsafe_allow_html=True)
            st.image(product["main_image"], width=200)
            desc_cols = st.columns([3,1])
            with desc_cols[0]:
                st.write(product["description"])
            with desc_cols[1]:
                st.write(" ")
            size_cols = st.columns([2,2,1])
            with size_cols[0]:
                st.number_input(f"1.34oz", min_value=0, value=0, step=1, key=f"qty_134_{idx + 3}")
            with size_cols[1]:
                st.number_input(f"2.25oz", min_value=0, value=0, step=1, key=f"qty_225_{idx + 3}")
    # Fifth column (column 5 in row 1) for the order summary placeholder
    with row2_cols[4]:
        total_placeholder = st.empty()

    # Submit button
    submitted = st.form_submit_button("Submit Order")

# Display the order summary in column 5 of row 1
if submitted:
    with summary_placeholder.container():
        total = 0
        for idx, product in enumerate(products):
            qty_134 = st.session_state[f"qty_134_{idx}"]
            qty_225 = st.session_state[f"qty_225_{idx}"]

            # Display individual breakdown for 1.34oz
            if qty_134 > 0:
                cost_134 = product["price"] * qty_134
                total += cost_134
                st.write(f"{product['name']} (1.34oz)<br> {qty_134} x ${product['price']:.2f} = ${cost_134:.2f}",unsafe_allow_html=True)

            # Display individual breakdown for 2.25oz
            if qty_225 > 0:
                cost_225 = product["price"] * qty_225
                total += cost_225
                st.markdown(f"{product['name']} (2.25oz)<br> {qty_225} x ${product['price']:.2f} = ${cost_225:.2f}",unsafe_allow_html=True)

    with total_placeholder:
        # Display total cost outside the loop
        st.markdown(f"Total Cost:<h3> ${total:.2f}",unsafe_allow_html=True)

# ---- REMOVE UNWANTED STREAMLIT STYLING ----
hide_st_style = """
            <style>
            Main Menu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
            
st.markdown(hide_st_style, unsafe_allow_html=True)
