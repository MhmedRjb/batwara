# Copyright (c) 2024, mhmed rjb and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

class TestExpense(FrappeTestCase):
	def test_equal_split_calculation(self):
		#create a test users before
		test_expense = frappe.get_doc({
			"doctype": "Expense",
			"paid_by": "nada@gmail.com",
			"amount": 100,	
			"splits": [
				{
					"user": "yomna@gmail.com"
					
				},
				{
					"user": "menna@gmail.com"
				}
    
			],
			"description": "Test Expense",
			"split_method": "Equally",
			"currency": "USD"
			
		}).insert()
  
		self.assertEqual(test_expense.splits[0].amount, 50)
		self.assertEqual(test_expense.splits[1].amount, 50)
