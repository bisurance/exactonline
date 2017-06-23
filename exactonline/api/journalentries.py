from .manager import Manager
from ..resource import GET


class GeneralJournalEntries(Manager):
	resource = 'generaljournalentry/GeneralJournalEntries'

	def filter(self, **kwargs):
		ret = super(Manager, self).filter(self, **kwargs)
		if 'GeneralJournalEntryLines' in ret:
			url = ret['GeneralJournalEntryLines']['__deferred']['url']
			ret['GeneralJournalEntryLines']['x'] = self._api._rest_query(url)
		return ret
