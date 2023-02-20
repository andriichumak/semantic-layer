from helpers.types import Dataset, Grain, Dimension, Fact, Join, MultiJoin

Customers = Dataset(
    id = 'customers',
    data_source = 'ecommerce.customers',
    title = 'Customers',
    description = 'Customers dimension',
    tags = [ 'ecommerce', 'customers' ],
    grain = Grain('customer_id'),
    fields = [
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
    
    grain = Grain('date'),
    fields = [
        Dimension('year'),
        Dimension('quarter'),
        Dimension('week'),
        Dimension('month'),
        Dimension('day'),
    ]
)

Products = Dataset('products', 'ecommerce.products', grain = Grain('product_id'), fields = [
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
    
    grain = Grain('promotion_id'),
    fields = [
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

    grain = Grain('order_id'),
    fields = [
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
