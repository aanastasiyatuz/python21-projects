import permissions

class Category:
    objects = []

    def __init__(self, title):
        self.title = title
        Category.objects.append(self)
    
    def __str__(self):
        return self.title

class Product:
    objects = []
    _id = 0

    def __init__(self, title, price, description, quantity, category):
        self.id = Product._id
        self.title = title
        self.price = price
        self.desc = description
        self.quantity = quantity
        self.category = category
        Product.objects.append(self)
        Product._id += 1

    def __str__(self):
        return f"{self.title} [{self.quantity}] - ${self.price}\n({self.desc[:20]})"

class Comment:
    objects = []

    def __init__(self, user, product, body):
        permissions.login_required(user)
        from datetime import datetime
        self.user = user
        self.product = product
        self.body = body
        self.created_at = datetime.now()
        Comment.objects.append(self)
    
    def __str__(self):
        return f"{self.user.email} - [{self.created_at}] - {self.body}"
