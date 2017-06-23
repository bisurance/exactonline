from .manager import Manager
from ..resource import GET


class GeneralJournalEntries(Manager):
	resource = 'generaljournalentry/GeneralJournalEntries'

	def resolveDeferredLines(self, entry):
		try:
			uri = entry['GeneralJournalEntryLines']['__deferred']['uri']
		except KeyError:
			return entry
		lines = self._api.restv1(GET(str(uri)))
		entry['GeneralJournalEntryLines'] = lines
		return entry

	def get(self, **kwargs):
		ret = Manager.filter(self, **kwargs)
		return self.resolveDeferredLines(ret)

	def filter(self, **kwargs):
		ret = Manager.filter(self, **kwargs)
		for entry in ret:
			self.resolveDeferredLines(entry)
		return ret

	def create(self, info, deferred=False):
		ret = Manager.create(self, info)
		if deferred:
			return self.resolveDeferredLines(ret)
		return ret
