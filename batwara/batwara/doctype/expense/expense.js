// Copyright (c) 2024, mhmed rjb and contributors
// For license information, please see license.txt

frappe.ui.form.on("Expense", {
	onload(frm) {
        frm.set_query("employee", function() {
            return {
                filters: {
                    "ignore_user_type": 1
                }
            }
        }
    )}
});
