from helpers.types import Dataset, Grain, Dimension, Fact, Join, MultiJoin

Customers = Dataset(
    id = 'customers',
    data_source = 'ecommerce.customers',
    title = 'Customers',
    description = 'Customers dimension',
    tags = [ 'ecommerce', 'customers' ],
    fields = [
        Grain('customer_id'),
        Fact('age'),
        Dimension('full_name'),
        Dimension('gender')
    ]
)

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

Products = Dataset('products', 'ecommerce.products', fields = [
    Grain('product_id'),
    Fact('unit_price'),
    Dimension('name'),
    Dimention('product_line')
])

Promotions = Dataset(
    'promotions',
    'ecommerce.promotions',

    title = 'Promotions',
    description = 'Ads and promotions dimension',
    tags = [ 'ecommerce', 'promo', 'ads' ],
    
    fields = [
        Grain('promotion_id'),
        Dimension('promo_name'),
        Dimension('ad_type'),
        Dimension(
            'coupon_type',
            title = 'Voucher type',
            description = 'A type of the coupon used, e.g. "discount", "3 for the price of 2" etc.'
        ),
        Dimension('price_reduction_type')
    ]
)

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
        MultiJoin(dataset = Products, using = 'product_id'),
        Join(Customers, 'customer_id'),
        Join(Dates, 'date'),
        Join(Promotions, 'promotion_id')
    ]
)
