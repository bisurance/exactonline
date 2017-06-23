from .manager import Manager
from ..resource import GET


class GeneralJournalEntries(Manager):
	resource = 'generaljournalentry/GeneralJournalEntries'

	def filter(self, **kwargs):
		ret = Manager.filter(self, **kwargs)  #super(GeneralJournalEntries, self).filter(**kwargs)
		uri = ret['GeneralJournalEntryLines']['__deferred']['uri']
		lines = self._api.restv1(GET(str(uri)))
		ret['GeneralJournalEntryLines']['x'] = lines
		return ret
