from flask import Blueprint
from controllers.TransactionController import *
from controllers.CategoryController import *
from controllers.GoalController import *

web = Blueprint("web", __name__)

# Transactions
web.route("/transactions", methods=["GET"])(get_all_transactions)
web.route("/transactions/<int:id>", methods=["GET"])(get_transaction)
web.route("/transactions", methods=["POST"])(add_transaction)
web.route("/transactions/<int:id>", methods=["PUT"])(update_transaction)
web.route("/transactions/<int:id>", methods=["DELETE"])(delete_transaction)

# Categories
web.route("/categories", methods=["GET"])(get_all_categories)
web.route("/categories/<int:id>", methods=["GET"])(get_category)
web.route("/categories", methods=["POST"])(add_category)
web.route("/categories/<int:id>", methods=["PUT"])(update_category)
web.route("/categories/<int:id>", methods=["DELETE"])(delete_category)

# Goals
web.route("/goals", methods=["GET"])(get_all_goals)
web.route("/goals/<int:id>", methods=["GET"])(get_goal)
web.route("/goals", methods=["POST"])(add_goal)
web.route("/goals/<int:id>", methods=["PUT"])(update_goal)
web.route("/goals/<int:id>", methods=["DELETE"])(delete_goal)
