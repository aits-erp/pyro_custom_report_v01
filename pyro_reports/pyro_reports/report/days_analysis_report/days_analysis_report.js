// Copyright (c) 2026, Krish and contributors
// For license information, please see license.txt

frappe.query_reports["Days Analysis Report"] = {
	filters: [
		{
			fieldname: "enquriry_type",
			label: __("Enquriry Type"),
			fieldtype: "Select",
			options: "\nMaintenance\nBudget\nProject\nOthers",
		},
	],

	// Makes the "No of offers" number clickable -> opens the matching Opportunity list
	formatter: function (value, row, column, data, default_formatter) {
		value = default_formatter(value, row, column, data);

		const type_map = {
			budget_offers: "Budget",
			project_offers: "Project",
			maintenance_offers: "Maintenance",
		};

		if (data && type_map[column.fieldname] && data[column.fieldname]) {
			const dates = JSON.stringify(["Between", [data.month_start, data.month_end]]);
			const url =
				`/app/opportunity?enquriry_type=${encodeURIComponent(type_map[column.fieldname])}` +
				`&custom_offer_qtn_sent_on_date=${encodeURIComponent(dates)}`;
			value = `<a href="${url}" target="_blank"><b>${data[column.fieldname]}</b></a>`;
		}
		return value;
	},
};