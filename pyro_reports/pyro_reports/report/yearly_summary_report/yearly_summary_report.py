# Copyright (c) 2026, Sukku and contributors
# For license information, please see license.txt

# import frappe

import frappe
from frappe.utils import flt, getdate

# ---------------------------------------------------------------------------
# CONFIG - change here only if your fieldnames are different
# ---------------------------------------------------------------------------
OFFER_VALUE_FIELD = "custom_offer_value_rs"      # Opportunity: OFFER VALUE RS.
PO_VALUE_FIELD = "custom_po_value"               # Opportunity: PO VALUE  -> "value of orders"
SALES_PERSON_FIELDS = ["custom_sales_person", "sales_person"]  # first one that exists is used
LOST_STATUS = "Lost"

# Financial year order: APRIL .. MARCH
MONTHS = [
	("APRIL", 4), ("MAY", 5), ("JUNE", 6), ("JULY", 7), ("AUG", 8), ("SEPT", 9),
	("OCT", 10), ("NOV", 11), ("DEC", 12), ("JAN", 1), ("FEB", 2), ("MARCH", 3),
]


def execute(filters=None):
	filters = frappe._dict(filters or {})
	return get_columns(), get_data(filters)


def get_columns():
	columns = [
		{"label": "Month", "fieldname": "particulars", "fieldtype": "Data", "width": 190}
	]
	for label, num in MONTHS:
		columns.append(
			{"label": label, "fieldname": f"m{num}", "fieldtype": "Data", "width": 115, "align": "right"}
		)
	columns.append({"label": "TOTAL", "fieldname": "total", "fieldtype": "Data", "width": 125, "align": "right"})
	return columns


def get_sales_person_field():
	meta = frappe.get_meta("Opportunity")
	for f in SALES_PERSON_FIELDS:
		if meta.has_field(f):
			return f
	return None


def get_data(filters):
	# ---------------- 1. Opportunities (filtered) ----------------
	opp_filters = {}
	if filters.get("from_date") and filters.get("to_date"):
		opp_filters["transaction_date"] = ["between", [filters.from_date, filters.to_date]]
	elif filters.get("from_date"):
		opp_filters["transaction_date"] = [">=", filters.from_date]
	elif filters.get("to_date"):
		opp_filters["transaction_date"] = ["<=", filters.to_date]

	if filters.get("customer"):
		opp_filters["opportunity_from"] = "Customer"
		opp_filters["party_name"] = filters.customer
	if filters.get("territory"):
		opp_filters["territory"] = filters.territory
	sp_field = get_sales_person_field()
	if filters.get("sales_person") and sp_field:
		opp_filters[sp_field] = filters.sales_person

	opps = frappe.get_all(
		"Opportunity",
		filters=opp_filters,
		fields=["name", "transaction_date", "status", OFFER_VALUE_FIELD, PO_VALUE_FIELD],
	)

	# ---------------- 2. Orders received (Opportunity -> Quotation -> Sales Order) ----------------
	opps_with_order = set()
	if opps:
		rows = frappe.db.sql(
			"""
			SELECT DISTINCT q.opportunity
			FROM `tabQuotation` q
			INNER JOIN `tabSales Order Item` soi ON soi.prevdoc_docname = q.name
			INNER JOIN `tabSales Order` so ON so.name = soi.parent
			WHERE so.docstatus = 1
				AND q.docstatus < 2
				AND q.opportunity IN %(opps)s
			""",
			{"opps": tuple(o.name for o in opps)},
			as_dict=True,
		)
		opps_with_order = {r.opportunity for r in rows}

	# ---------------- 3. Month-wise aggregation ----------------
	keys = [num for _, num in MONTHS]
	z = lambda: {k: 0 for k in keys}
	sent, orders, lost = z(), z(), z()
	offer_val, order_val, lost_val = z(), z(), z()

	for o in opps:
		if not o.transaction_date:
			continue
		m = getdate(o.transaction_date).month
		sent[m] += 1
		offer_val[m] += flt(o.get(OFFER_VALUE_FIELD))

		# value of orders = PO VALUE entered on the Opportunity
		order_val[m] += flt(o.get(PO_VALUE_FIELD))

		if o.name in opps_with_order:
			orders[m] += 1

		if o.status == LOST_STATUS:
			lost[m] += 1
			lost_val[m] += flt(o.get(OFFER_VALUE_FIELD))

	# ---------------- 4. Build rows ----------------
	def with_total(d):
		d = dict(d)
		d["total"] = sum(d.values())
		return d

	sent, orders, lost = with_total(sent), with_total(orders), with_total(lost)
	offer_val, order_val, lost_val = with_total(offer_val), with_total(order_val), with_total(lost_val)
	cols = keys + ["total"]

	def num_row(label, src, money=False):
		row = {"particulars": label}
		for c in cols:
			row[col_name(c)] = fmt_money(src[c]) if money else str(int(src[c]))
		return row

	def pct_row(label, num, den):
		row = {"particulars": label}
		for c in cols:
			row[col_name(c)] = pct(num[c], den[c])
		return row

	return [
		num_row("No of offers sent", sent),
		num_row("No of orders received", orders),
		pct_row("% conversion", orders, sent),
		num_row("No of offers lost", lost),
		pct_row("% conversion", lost, sent),
		{},  # blank separator row
		num_row("value of offers", offer_val, money=True),
		num_row("value of orders", order_val, money=True),
		pct_row("% conversion", order_val, offer_val),
		num_row("value of offers lost", lost_val, money=True),
		pct_row("% conversion", lost_val, offer_val),
	]


def col_name(c):
	return "total" if c == "total" else f"m{c}"


def pct(num, den):
	if not den:
		return "0%"
	return f"{round(num / den * 100)}%"


def fmt_money(n):
	"""Indian digit grouping (12,34,567) without decimals."""
	n = int(round(flt(n)))
	sign = "-" if n < 0 else ""
	s = str(abs(n))
	if len(s) <= 3:
		return sign + s
	head, tail = s[:-3], s[-3:]
	parts = []
	while len(head) > 2:
		parts.insert(0, head[-2:])
		head = head[:-2]
	if head:
		parts.insert(0, head)
	return sign + ",".join(parts) + "," + tail