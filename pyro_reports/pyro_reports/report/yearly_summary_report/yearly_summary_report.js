// Copyright (c) 2026, Krish and contributors
// For license information, please see license.txt

// Copyright (c) 2026, Pyro Electric Instruments
frappe.query_reports["Yearly Summary Report"] = {
	filters: [
		{
			fieldname: "from_date",
			label: __("From Date"),
			fieldtype: "Date",
			reqd: 1,
			default: get_fy_start(),
		},
		{
			fieldname: "to_date",
			label: __("To Date"),
			fieldtype: "Date",
			reqd: 1,
			default: get_fy_end(),
		},
		{
			fieldname: "customer",
			label: __("Customer"),
			fieldtype: "Link",
			options: "Customer",
		},
		{
			fieldname: "territory",
			label: __("Territory"),
			fieldtype: "Link",
			options: "Territory",
		},
		{
			fieldname: "sales_person",
			label: __("Sales Person"),
			fieldtype: "Link",
			options: "Sales Person",
		},
	],
};

// Financial year = 1 April to 31 March
function get_fy_start() {
	const today = frappe.datetime.get_today();
	const year = parseInt(today.substring(0, 4));
	const month = parseInt(today.substring(5, 7));
	return `${month >= 4 ? year : year - 1}-04-01`;
}

function get_fy_end() {
	const today = frappe.datetime.get_today();
	const year = parseInt(today.substring(0, 4));
	const month = parseInt(today.substring(5, 7));
	return `${month >= 4 ? year + 1 : year}-03-31`;
}