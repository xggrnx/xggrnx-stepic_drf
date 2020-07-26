# Create your models here.

from lib.models import BaseModel


class RecipientModel(BaseModel):
    keys = [
        'info.surname', 'info.name', 'info.patronymic',
        'contacts.phoneNumber',
    ]


Recipient = RecipientModel('recipients')
