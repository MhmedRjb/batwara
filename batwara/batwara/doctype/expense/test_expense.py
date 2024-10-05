# Copyright (c) 2024, mhmed rjb and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

import frappe
from frappe.tests.utils import FrappeTestCase

class TestExpense(FrappeTestCase):
    def test_equal_split_calculation(self):
        # Create test users if they do not exist
        if not frappe.db.exists("User", "test1@gmail.com"):
            user1 = frappe.get_doc({
                "doctype": "User",
                "email": "test1@gmail.com",
                "first_name": "test",
            }).insert()
  
        if not frappe.db.exists("User", "test2@gmail.com"):
            user2 = frappe.get_doc({
                "doctype": "User",
                "email": "test2@gmail.com",
                "first_name": "test1",
            }).insert()
  
        # Create test expense
        test_expense = frappe.get_doc({
            "doctype": "Expense",
            "paid_by": "nada@gmail.com",
            "amount": 100,	
            "splits": [
                {
                    "user": "test1@gmail.com"
                },
                {
                    "user": "test2@gmail.com"
                }
            ],
            "description": "Test Expense",
            "split_method": "Equally",
            "currency": "USD"
        }).insert()
  
        self.assertEqual(test_expense.splits[0].amount, 50)
        self.assertEqual(test_expense.splits[1].amount, 50)