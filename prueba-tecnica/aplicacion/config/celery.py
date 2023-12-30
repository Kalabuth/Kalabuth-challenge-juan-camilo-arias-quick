import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prueba.settings')

app = Celery('aplicacion', backend='rpc://', broker='redis://redis:6379', include=['aplicacion.task'])
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')