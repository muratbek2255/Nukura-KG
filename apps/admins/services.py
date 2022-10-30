import asyncio
from asyncio import Queue


async def process_billing(query_list):
    """Billing service"""
    billing_list = []

    async def extract_billing(qlist, q: Queue):
        assigned_billing = {}
        for record in qlist:
            await asyncio.sleep(2)
            assigned_billing['admin_name'] = "{}".format(record.username)
            if not len(record.children) == 0:
                assigned_billing['billing_items'] = record.children
            else:
                assigned_billing['billing_items'] = None

            await q.put(assigned_billing)

    async def build_billing_sheet(q: Queue):
        while True:
            await asyncio.sleep(2)
            assigned_billing = await q.get()
            name = assigned_billing['admin_name']
            billing_items = assigned_billing['billing_items']
            if not billing_items == None:
                for item in billing_items:
                    billing_list.append({'admin_name': name, 'billing': item})
            else:
                billing_list.append({'admin_name': name, 'billing': None})
            q.task_done()

    q = asyncio.Queue()
    build_sheet = asyncio.create_task(build_billing_sheet(q))
    await asyncio.gather(asyncio.create_task(extract_billing(query_list, q)))

    await q.join()
    build_sheet.cancel()
    return billing_list
