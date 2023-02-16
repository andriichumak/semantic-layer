from helpers.types import Dataset, Attribute, Fact, Join

Products = Dataset(
    id = 'products',
    data_source = 'ecommerce.products',

    fields = [
        Grain('product_id')
    ],

    include_all_fields = true
)

Customers = Dataset('customers', 'ecommerce.customers', fields = [ Grain('customer_id') ], include_all_fields = true)

Dates = Dataset(
    id = 'dates',
    data_source = 'ecommerce.dates',

    title = 'Order date',
    description = 'Defines date / time dimension',
    tags = [ 'ecommerce', 'date' ],
    
    fields = [
        Grain('date'),
        Dimension('year'),
        Dimension('quarter'),
        Dimension('week'),
        Dimension('month'),
        Dimension('day'),
    ]
)

Promotions = Dataset('promotions', 'ecommerce.promotions', fields = [ Grain('promotion_id') ], include_all_fields = true)

Orders = Dataset(
    id = 'orders',
    data_source = 'ecommerce.orders',

    title = 'Orders',
    description = 'Dataset with facts, containing a list of orders',
    tags = [ 'ecommerce', 'orders' ],

    fields = [
        Grain('order_id'),
        Fact(
            id = 'revenue',
            title = 'Revenue',
            description = 'A total revenue for the order',
            tags = [ 'ecommerce', 'revenue' ],
            source_column = 'revenue'
        ),
        Fact('units_sold')
    ],

    joins = [
        Join(dataset = Products, using = 'product_id', multivalue = false),
        Join(Customers, 'customer_id'),
        Join(Dates, 'date'),
        Join(Promotions, 'promotion_id')
    ]
)
