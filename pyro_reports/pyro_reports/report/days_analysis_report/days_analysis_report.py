# Copyright (c) 2026, Krish and contributors
# For license information, please see license.txt

# import frappe

import frappe
from frappe import _
from frappe.utils import add_days, get_last_day, getdate, today
from datetime import date

TYPE_FIELD = "enquriry_type"
QTN_DATE_FIELD = "custom_qtn_date"
SENT_DATE_FIELD = "custom_offer_qtn_sent_on_date"

# (key, column group heading, value in the Enquriry Type field)
TYPES = [
	("budget", "BUDGETORY", "Budget"),
	("project", "PROJECT", "Project"),
	("maintenance", "E (Maintenance)", "Maintenance"),
]

# Same order as the Excel sheet
MONTH_ORDER = [4, 5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3]
MONTH_NAMES = {
	1: "JANUARY", 2: "FEBRUARY", 3: "MARCH", 4: "APRIL", 5: "MAY", 6: "JUNE",
	7: "JULY", 8: "AUGUST", 9: "SEPTEMBER", 10: "OCTOBER", 11: "NOVEMBER", 12: "DECEMBER",
}

WEEKLY_OFF = (6,)  # 6 = Sunday. Use (5, 6) if Saturday is also off


def execute(filters=None):
	filters = frappe._dict(filters or {})
	return get_columns(), get_data(filters)


def get_columns():
	columns = [
		{"label": _("MONTH"), "fieldname": "month", "fieldtype": "Data", "width": 130}
	]
	for key, heading, _val in TYPES:
		columns.append({
			"label": _("{0} - No of offers").format(heading),
			"fieldname": f"{key}_offers",
			"fieldtype": "Int",
			"width": 150,
		})
		columns.append({
			"label": _("{0} - Average No of dayes taken in submission").format(heading),
			"fieldname": f"{key}_days",
			"fieldtype": "Float",
			"precision": 0,
			"width": 250,
		})
	columns.append({"label": _("TOTAL"), "fieldname": "total", "fieldtype": "Int", "width": 90})
	return columns


def working_days(start, end):
	"""Working days from start to end (start not counted, weekly offs skipped)."""
	start, end = getdate(start), getdate(end)
	count, d = 0, start
	while d < end:
		d = getdate(add_days(d, 1))
		if d.weekday() not in WEEKLY_OFF:
			count += 1
	return count


def get_fiscal_year_start():
	t = getdate(today())
	return t.year if t.month >= 4 else t.year - 1


def get_data(filters):
	fy = get_fiscal_year_start()
	fy_start, fy_end = date(fy, 4, 1), date(fy + 1, 3, 31)

	opp_filters = {SENT_DATE_FIELD: ["between", [fy_start, fy_end]]}
	if filters.get(TYPE_FIELD):
		opp_filters[TYPE_FIELD] = filters.get(TYPE_FIELD)

	opportunities = frappe.get_list(
		"Opportunity",
		filters=opp_filters,
		fields=["name", TYPE_FIELD, QTN_DATE_FIELD, SENT_DATE_FIELD],
		limit_page_length=0,
	)

	type_to_key = {val: key for key, _h, val in TYPES}

	# stats[month][key] = {"count": offers, "days_sum": total days, "days_cnt": offers having both dates}
	stats = {
		m: {key: {"count": 0, "days_sum": 0, "days_cnt": 0} for key, _h, _v in TYPES}
		for m in MONTH_ORDER
	}

	for opp in opportunities:
		key = type_to_key.get(opp.get(TYPE_FIELD))
		if not key:
			continue  # e.g. "Others" has no column in this report layout

		sent = getdate(opp.get(SENT_DATE_FIELD))
		bucket = stats[sent.month][key]
		bucket["count"] += 1

		if opp.get(QTN_DATE_FIELD):
			qtn = getdate(opp.get(QTN_DATE_FIELD))
			bucket["days_sum"] += working_days(qtn, sent)
			bucket["days_cnt"] += 1

	data = []
	for m in MONTH_ORDER:
		year = fy if m >= 4 else fy + 1
		month_start = date(year, m, 1)

		row = {
			"month": MONTH_NAMES[m],
			"month_start": str(month_start),                 # used by the clickable link in JS
			"month_end": str(get_last_day(month_start)),     # (not shown as a column)
		}
		total = 0
		for key, _h, _v in TYPES:
			b = stats[m][key]
			row[f"{key}_offers"] = b["count"] or None
			row[f"{key}_days"] = round(b["days_sum"] / b["days_cnt"]) if b["days_cnt"] else None
			total += b["count"]
		row["total"] = total
		data.append(row)

	return data