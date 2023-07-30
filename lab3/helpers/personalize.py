import json
import pandas as pd
import requests


def get_product_recommendations(user_id, use_personalize_api, api_key, api_endpoint_name):
    """
    Get product recommendations for a given user.

    Parameters
    ----------
    user_id : int
        User ID to get recommendations for.
    use_personalize_api : bool
        Whether to use the personalize API.
    api_key : str
        The API key.
    api_endpoint_name : str
        The API URL.

    Returns
    -------
    list
        List of products' IDs.
    """
    try:
        if use_personalize_api:
            # get recommendations from the personalize API
            personalize_url = api_endpoint_name + f'?user_id={user_id}'

            response = requests.get(
                personalize_url,
                headers={
                    'accept': 'application/json',
                    'X-API-Key': api_key
                }
            )    
            recommendations = json.loads(response.content.decode('utf-8'))
            recommendations = [rec["itemId"] for rec in recommendations][:1]
        else:
            # load example recommendations from a csv file
            df = pd.read_csv('./data/example_recommendations_retail.csv')
            df = df[df.user_id == user_id]
            recommendations = list(df.item_id.values[:1])
        return recommendations
    
    except Exception as err:
        print(err)