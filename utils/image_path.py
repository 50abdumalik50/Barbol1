def upload_products(instance, filename):
    return f"products/{instance.product.title}/{filename}"


def upload_cakes(instance, filename):
    return f"cakes/{instance.cake.title}/{filename}"