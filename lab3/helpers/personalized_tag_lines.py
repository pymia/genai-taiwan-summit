def get_user(user_id, users_metadata_df):
    # Fetch by user id as the key
    user = users_metadata_df[users_metadata_df['USER_ID'] == user_id]
    
    # Grab metadata we're interested in
    age_description = user['AGE'].values[0]
    gender = user['GENDER'].values[0]
    if gender == 'M':
        gender_description = "Male"
    else:
        gender_description = "Female"

    return age_description, gender_description

def get_product(product_id, products_metadata_json):
    # Fetch by item id as the key
    product = products_metadata_json[products_metadata_json['ITEM_ID'] == product_id]
    
    # Grab metadata we're interested in
    price = product.PRICE.values[0]
    category_lv1 = product.CATEGORY_L1.values[0]
    category_lv2 = product.CATEGORY_L2.values[0]
    description = product.PRODUCT_DESCRIPTION.values[0]
    product_info = {
        'category':category_lv1,
        'subcategory':category_lv2,
        'price':price,
        'description':description
    }
    
    return product_info


