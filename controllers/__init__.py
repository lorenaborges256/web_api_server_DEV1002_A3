from controllers.products_controller import products
from controllers.suppliers_controller import suppliers
from controllers.categories_controller import categories
from controllers.product_supplier_controller import products_suppliers

registerable_controllers = [
    products,
    suppliers,
    categories,
    products_suppliers
]