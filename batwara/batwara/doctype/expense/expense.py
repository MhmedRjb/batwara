# Copyright (c) 2024, mhmed rjb and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Expense(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from batwara.batwara.doctype.expense_split.expense_split import ExpenseSplit
		from frappe.types import DF

		amended_from: DF.Link | None
		amount: DF.Currency
		currency: DF.Link
		date: DF.Date | None
		description: DF.Data
		note: DF.SmallText | None
		paid_by: DF.Link
		split_method: DF.Literal["Equally", "Manual"]
		splits: DF.Table[ExpenseSplit]
	# end: auto-generated types

	def validate(self):
			self.apply_split()
   
	def apply_split(self):
		if self.split_method == "Equally":
				self.calculate_equal_split()
		else:
			pass
	
	def calculate_equal_split(self):
		num_splits=len(self.splits)
		splits_amount = self.amount / num_splits
	
		for split in self.splits:
			split.amount = splits_amount
