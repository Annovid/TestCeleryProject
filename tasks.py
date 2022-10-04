from proj import celery_app
from alchemy import insert_into_main_table


@celery_app.task()
def edit_text(text):
    result = text.lower()
    insert_into_main_table(result)
    return result
