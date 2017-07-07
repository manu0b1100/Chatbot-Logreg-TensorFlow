from django.core.management.base import BaseCommand, CommandError
from chat_ml.Data.dataupdate import preprocessDataMaster,LogRegTraining,TensorTraining
class Command(BaseCommand):

    help = "update data"

    def handle(self, *args, **options):
        preprocessDataMaster()
        LogRegTraining()
        TensorTraining()

