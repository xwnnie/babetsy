from flask.cli import AppGroup
from .users import seed_users, undo_users
from .categories import seed_categories, undo_categories
from .products import seed_products, undo_products
from .orders import seed_orders, undo_orders
from .reviews import seed_reviews, undo_reviews
from .carts import seed_carts, undo_carts

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_categories()
    seed_products()
    seed_users()
    seed_orders()
    seed_reviews()
    seed_carts()


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_categories()
    undo_products()
    undo_users()
    undo_orders()
    undo_reviews()
    undo_carts()
