from models import User, Product, Comment

user1 = User("test@gmail.com", "hello", "female")
user1.register("123456789", "123456789")
user1.login("123456789")

product1 = Product("Iphone 10", 12345, "...", 10)

comment1 = Comment(user1, product1, "Оч классный телефон")
print(comment1)