from website import create_app, db
from website.models import Product

app = create_app()

with app.app_context():
    db.session.add(Product(name="Laptop", price=999))
    db.session.add(Product(name="Phone", price=499))
    db.session.add(Product(name="Headphones", price=199))
    db.session.commit()
