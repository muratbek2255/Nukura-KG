from celery import Celery
from celery.utils.log import get_task_logger

celery = Celery("core", broker='amqp://guest:guest@127.0.0.1:5672', result_backend='redis://localhost:6379/0', include=["services.billing", "models", "config"])


class CeleryConfig:
    celery_store_errors_even_if_ignored = True
    task_create_missing_queues = True
    task_store_errors_even_if_ignored = True
    task_ignore_result = False
    task_serializer = "pickle"
    result_serializer = "pickle"
    event_serializer = "json"
    accept_content = ["pickle", "application/json", "application/x-python-serialize"]
    result_accept_content = ["pickle", "application/json", "application/x-python-serialize"]


celery.config_from_object(CeleryConfig)
celery_log = get_task_logger(__name__)
