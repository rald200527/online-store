from flask import Blueprint, render_template, session, redirect, url_for
from flask_login import login_required
from .models import Product

views = Blueprint('views', __name__)

# STORE / HOME PAGE
from flask_login import login_required

@views.route('/')
@login_required
def store():
    products = Product.query.all()
    return render_template('store.html', products=products)



# ADD TO CART
@views.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    return redirect(url_for('views.store'))


# CART PAGE
@views.route('/cart')
@login_required
def cart():
    cart_ids = session.get('cart', [])

    if not cart_ids:
        return render_template('cart.html', products=[], total=0)

    products = Product.query.filter(Product.id.in_(cart_ids)).all()
    total = sum(p.price for p in products)

    return render_template('cart.html', products=products, total=total)
