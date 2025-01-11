frappe.ui.form.on('Friend Circle', {
    refresh(frm) {
        frm.set_query("friend", "friends", function(doc, cdt, cdn) {
            var selected_friends = doc.friends.map(row => row.friend);
            var excluded_emails = selected_friends.concat(frm.doc.user);

            return {
                filters: {
                    "ignore_user_type": 1,
                    "Email": ["not in", excluded_emails],
                    "Email": ["not in", frm.doc.user]

                }
            };
        });
    }
});