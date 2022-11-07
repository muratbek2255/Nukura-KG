import os
import asyncio

from core.celery import celery, celery_log


async def generate_billing_sheet(billing_date, query_list):
    filepath = os.getcwd() + '/data/billing-' + str(billing_date) +'.csv'
    with open(filepath, mode="a") as sheet:
        for vendor in query_list:
            billing = vendor.children
            for record in billing:
                if billing_date == record.date_billed:
                    entry = ";".join(
                        [str(record.date_billed), vendor.account_name, vendor.account_number, str(record.payable),
                         str(record.total_issues)])
                    sheet.write(entry)
                await asyncio.sleep(1)


async def create_total_payables_year(billing_date, query_list):
    total = 0.0
    for vendor in query_list:
        billing = vendor.children
        for record in billing:
            if billing_date == record.date_billed:
                total += record.payable
                await asyncio.sleep(1)
    print(total)


@celery.task(name="services.billing.tasks.create_total_payables_year_celery", auto_retry=[ValueError, TypeError],
             max_tries=5)
def create_total_payables_year_celery(billing_date, query_list):
    total = 0.0
    for vendor in query_list:
        billing = vendor.children
        for record in billing:
            if billing_date == record.date_billed:
                total += record.payable
    celery_log.info('computed result: ' + str(total))
    return total
