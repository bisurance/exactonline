from .manager import Manager
from ..resource import GET


class Journals(Manager):
    resource = 'generaljournalentry/GeneralJournalEntries'
