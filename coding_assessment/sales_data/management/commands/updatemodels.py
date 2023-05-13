from django.core.management.base import BaseCommand
import pandas as pd
from sales_data.models import Sales

class Command(BaseCommand):
    help = 'Import Data!'

    def handle(self, parser):
        pass

    def handle(self, *args, **options):
        # database backup connection
        df = pd.read_csv('xyz_sales_data.csv')
        for ORDER_ID, ORDER_DATE, CUSTOMER_ID, CUSTOMER_NAME, COUNTRY, REGION, CATEGORY, SUB_CATEGORY,\
             PRODUCT_NAME, SALES in zip(df.order_id, df.order_date, df.customer_id, df.customer_name, df.country, df.region,\
                 df.category, df.sub_category, df.product_name, df.sales):
                models = Sales(order_id=ORDER_ID, order_date=ORDER_DATE, customer_id=CUSTOMER_ID, customer_name=CUSTOMER_NAME,\
                    country=COUNTRY, region=REGION, category=CATEGORY, sub_category=SUB_CATEGORY,\
                        product_name=PRODUCT_NAME, sales=SALES)
                models.save()

