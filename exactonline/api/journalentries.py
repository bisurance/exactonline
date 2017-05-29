from .manager import Manager
from ..resource import GET


class GeneralJournalEntries(Manager):
	resource = 'generaljournalentry/GeneralJournalEntries'

	def all():
		return self.filter(select='Created')
