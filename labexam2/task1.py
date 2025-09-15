def update_stock(product_id, qty, stock_dict):
    """
    Updates the stock quantity for a given product.

    Parameters:
        product_id (str): The ID of the product to update.
        qty (int): The quantity to subtract from the current stock.
        stock_dict (dict): Dictionary containing product IDs as keys and their stock quantities as values.

    Returns:
        dict: Updated stock dictionary. If product_id is not found, no changes are made.
              Stock value will never go negative.
    """
    # Check if the product_id exists in the stock dictionary
    if product_id in stock_dict:
        # Subtract qty from the current stock
        stock_dict[product_id] -= qty
        # Ensure stock never goes negative
        if stock_dict[product_id] < 0:
            stock_dict[product_id] = 0
    # If product_id not in stock_dict, do nothing
    return stock_dict  # Stock never goes negative

# Sample Input
result = update_stock("P01", 3, {"P01": 5})
print(result)  # Sample Output: {"P01": 2}