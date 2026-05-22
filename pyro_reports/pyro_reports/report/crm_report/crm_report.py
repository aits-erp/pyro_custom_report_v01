import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)

    return columns, data


def get_columns():
    columns = [
        {
            "label": "SR NO.",
            "fieldname": "sr_no",
            "fieldtype": "Int",
            "width": 80
        },
        {
            "label": "ENQ DETAILS",
            "fieldname": "enq_details",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": "Pyro Allied/Pyro Goa",
            "fieldname": "pyro_allied_pyro_goa",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "Customer Type",
            "fieldname": "customer_type",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Private - P OR Govt - G",
            "fieldname": "private_or_govt",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "Enq Type",
            "fieldname": "enq_type",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "ENQ RECEIVED ON",
            "fieldname": "enq_received_on",
            "fieldtype": "Date",
            "width": 130
        },
        {
            "label": "QTN. NO",
            "fieldname": "qtn_no",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": "QTN. DATE",
            "fieldname": "qtn_date",
            "fieldtype": "Date",
            "width": 120
        },
        {
            "label": "OFFER/QTN SENT ON DATE",
            "fieldname": "offer_qtn_sent_on_date",
            "fieldtype": "Date",
            "width": 180
        },
        {
            "label": "CUSTOMER",
            "fieldname": "customer",
            "fieldtype": "Data",
            "width": 220
        },
        {
            "label": "Offer Status",
            "fieldname": "offer_status",
            "fieldtype": "Data",
            "width": 140
        },
        {
            "label": "PLACE",
            "fieldname": "place",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "SALES REP.",
            "fieldname": "sales_rep",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "PROJECT/CLIENT",
            "fieldname": "project_client",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "ITEM/PRODUCT",
            "fieldname": "item_product",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "MATERIAL/SPECIAL DESIGN",
            "fieldname": "material_special_design",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "QTY OFFERED",
            "fieldname": "qty_offered",
            "fieldtype": "Float",
            "width": 120
        },
        {
            "label": "OFFER VALUE RS.",
            "fieldname": "offer_value_rs",
            "fieldtype": "Currency",
            "width": 150
        },
        {
            "label": "Expected in",
            "fieldname": "expected_in",
            "fieldtype": "Date",
            "width": 130
        },
        {
            "label": "CUSTOMER CONTACT PERSON",
            "fieldname": "customer_contact_person",
            "fieldtype": "Data",
            "width": 220
        },
        {
            "label": "CUSTOMER CONTACT NO.",
            "fieldname": "customer_contact_no",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "CUSTOMER EMAIL ID",
            "fieldname": "customer_email_id",
            "fieldtype": "Data",
            "width": 220
        },
        {
            "label": "PO NO / DATE",
            "fieldname": "po_no_date",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "PO VALUE",
            "fieldname": "po_value",
            "fieldtype": "Currency",
            "width": 140
        },
        {
            "label": "PO Received",
            "fieldname": "po_received",
            "fieldtype": "Date",
            "width": 140
        }
    ]

    return columns


def get_data(filters):
    conditions = ""

    if filters.get("from_date"):
        conditions += f" AND op.transaction_date >= '{filters.get('from_date')}'"

    if filters.get("to_date"):
        conditions += f" AND op.transaction_date <= '{filters.get('to_date')}'"

    data = frappe.db.sql(f"""
        SELECT
            ROW_NUMBER() OVER() as sr_no,

            op.custom_enq_details as enq_details,
            op.custom_pyro_alliedpyro_goa as pyro_allied_pyro_goa,

            '' as customer_type,

            op.custom_private__p_or_govt__g as private_or_govt,

            ld.custom_enquriry_type as enq_type,
            op.transaction_date as enq_received_on,

            op.custom_quotation as qtn_no,

            op.custom_qtn_date as qtn_date,

            op.custom_offer_qtn_sent_on_date as offer_qtn_sent_on_date,

            op.customer_name as customer,

            op.custom_offer_status_ as offer_status,

            COALESCE(op.city, ld.city) as place,

            op.custom_sales_rep as sales_rep,

            op.custom_project_client as project_client,

            op.custom_item_product as item_product,

            op.custom_material_special_design as material_special_design,

            op.custom_qty_offered as qty_offered,

            op.custom_offer_value_rs as offer_value_rs,

            op.expected_closing as expected_in,

            COALESCE(op.contact_person, ld.lead_name) as customer_contact_person,

            COALESCE(op.contact_mobile, ld.custom_phone_no) as customer_contact_no,

            COALESCE(op.contact_email, ld.email_id) as customer_email_id,

            CONCAT(
                IFNULL(op.custom_po_no, ''),
                ' / ',
                IFNULL(op.custom_po_date, '')
            ) as po_no_date,

            op.custom_po_value as po_value,

            op.custom_po_received as po_received

        FROM `tabOpportunity` op

        LEFT JOIN `tabLead` ld
        ON op.lead = ld.name

        WHERE op.docstatus < 2
        {conditions}

        ORDER BY op.creation DESC
    """, as_dict=True)

    return data