import streamlit as st

# Define product details
products = [
    {
        "name": "Buffalo", 
        "main_image": "assets\Wilde_1.34oz_Buffalo_WithoutShadow_02242023.png",
        "image_225": "assets/Wilde_1oz_8ct_Carton_Buffalo_06012023.png",
        "image_134": "assets/Wilde_Rendering_12ct_Buffalo_09152022.png",
        "description": "Description Here", 
        "price_134": 13.60,
        "price_225": 37.20
        },
    {
        "name": "Chicken & Waffles",
        "main_image": "assets\Wilde_1.34oz_CW_WithoutShadow_02242023.png",
        "image_225": "assets/Wilde_1oz_8ct_Carton_CW_06012023.png",
        "image_134": "assets/Wilde_Rendering_12ct_CW_09152022.png",
        "description": "Description Here", 
        "price_134": 13.60,
        "price_225": 37.20
        },
    {
        "name": "BBQ", 
        "main_image": "assets\Wilde_1.34oz_BBQ_WithoutShadow_02242023.png",
        "image_225": "assets/Wilde_1oz_8ct_Carton_BBQ_06012023.png",
        "image_134": "assets/Wilde_Rendering_12ct_BBQ_02292024.png",
        "description": "Description Here", 
        "price_134": 13.60,
        "price_225": 37.20
        },
    {
        "name": "Sea Salt & Vinegar", 
        "main_image": "assets\Wilde_1.34oz_SSV_WithoutShadow_02242023.png",
        "image_225": "assets/Wilde_1oz_8ct_Carton_SSV_06012023.png",
        "image_134": "assets/Wilde_Rendering_12ct_SSV_09152022.png",
        "description": "Description Here", 
        "price_134": 13.60,
        "price_225": 37.20
        },
    {
        "name": "Himalayan Pink Salt", 
        "main_image": "assets\Wilde_1.34oz_Pink_WithoutShadow_02242023.png",
        "image_225": "assets/Wilde_1oz_8ct_Carton_Pink_06012023.png",
        "image_134": "assets/Wilde_Rendering_12ct_Pink_09152022.png", 
        "description": "Description Here", 
        "price_134": 13.60,
        "price_225": 37.20
        },
    {
        "name": "Spicy Queso", 
        "main_image": "assets\Wilde_1.34oz_Buffalo_WithoutShadow_02242023.png",
        "image_225": "assets/Wilde_1oz_8ct_Carton_SQ_12052023.png",
        "image_134": "assets/Wilde_Rendering_12ct_SQ_04052024.png",
        "description": "Description Here", 
        "price_134": 13.60,
        "price_225": 37.20
        },
    {
        "name": "Nashville Hot", 
        "main_image": "assets\Wilde_1.34oz_NashvilleHot_WithoutShadow_02242023.png",
        "image_225": "assets/Wilde_1oz_8ct_Carton_Nashville_06012023.png",
        "image_134": "assets/Wilde_Rendering_12ct_NH_04082024.png",
        "description": "Description Here", 
        "price_134": 13.60,
        "price_225": 37.20
        },
]