from wtforms import FieldList
from wtforms.utils import unset_value


def initialize():
    def prepend_entry(self):
        """Add an empty entry to the start of this FieldList."""

        assert (
            not self.max_entries or len(
                self.entries) < self.max_entries
        ), "You cannot have more than max_entries entries in this FieldList"
        index = self.last_index + 1
        self.last_index = index
        name = f"{self.short_name}{self._separator}{index}"
        id = f"{self.id}{self._separator}{index}"
        field = self.unbound_field.bind(
            form=None,
            name=name,
            prefix=self._prefix,
            id=id,
            _meta=self.meta,
            translations=self._translations,
        )
        field.process(None, unset_value)
        self.entries.insert(0, field)
        return field

    FieldList.prepend_entry = prepend_entry
