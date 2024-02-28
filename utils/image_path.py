def upload_products(instance, filename):
    return f"products/{instance.product.title}/{filename}"