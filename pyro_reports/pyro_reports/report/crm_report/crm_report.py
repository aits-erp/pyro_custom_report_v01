# import frappe


# def execute(filters=None):
#     columns = get_columns()
#     data = get_data(filters)

#     return columns, data


# def get_columns():
#     columns = [
#         {
#             "label": "SR NO.",
#             "fieldname": "sr_no",
#             "fieldtype": "Int",
#             "width": 80
#         },
#         {
#             "label": "ENQ DETAILS",
#             "fieldname": "enq_details",
#             "fieldtype": "Data",
#             "width": 250
#         },
#         {
#             "label": "LEAD",
#             "fieldname": "lead",
#             "fieldtype": "Data",
#             "width": 180
#         },
#         {
#             "label": "Enq Type",
#             "fieldname": "enq_type",
#             "fieldtype": "Data",
#             "width": 150
#         },
#         {
#             "label": "ENQ RECEIVED ON",
#             "fieldname": "enq_received_on",
#             "fieldtype": "Date",
#             "width": 130
#         },
#         {
#             "label": "QTN. NO",
#             "fieldname": "qtn_no",
#             "fieldtype": "Data",
#             "width": 120
#         },
#         {
#             "label": "QTN. DATE",
#             "fieldname": "qtn_date",
#             "fieldtype": "Date",
#             "width": 120
#         },
#         {
#             "label": "OFFER/QTN SENT ON DATE",
#             "fieldname": "offer_qtn_sent_on_date",
#             "fieldtype": "Date",
#             "width": 180
#         },
#         {
#             "label": "CUSTOMER",
#             "fieldname": "customer",
#             "fieldtype": "Data",
#             "width": 220
#         },
#         {
#             "label": "Offer Status",
#             "fieldname": "offer_status",
#             "fieldtype": "Data",
#             "width": 140
#         },
#         {
#             "label": "PLACE",
#             "fieldname": "place",
#             "fieldtype": "Data",
#             "width": 150
#         },
#         {
#             "label": "SALES REP.",
#             "fieldname": "sales_rep",
#             "fieldtype": "Data",
#             "width": 150
#         },
#         {
#             "label": "PROJECT/CLIENT",
#             "fieldname": "project_client",
#             "fieldtype": "Data",
#             "width": 180
#         },
#         {
#             "label": "ITEM/PRODUCT",
#             "fieldname": "item_product",
#             "fieldtype": "Data",
#             "width": 180
#         },
#         {
#             "label": "MATERIAL/SPECIAL DESIGN",
#             "fieldname": "material_special_design",
#             "fieldtype": "Data",
#             "width": 200
#         },
#         {
#             "label": "QTY OFFERED",
#             "fieldname": "qty_offered",
#             "fieldtype": "Float",
#             "width": 120
#         },
#         {
#             "label": "OFFER VALUE RS.",
#             "fieldname": "offer_value_rs",
#             "fieldtype": "Currency",
#             "width": 150
#         },
#         {
#             "label": "Expected in",
#             "fieldname": "expected_in",
#             "fieldtype": "Date",
#             "width": 130
#         },
#         {
#             "label": "CUSTOMER CONTACT PERSON",
#             "fieldname": "customer_contact_person",
#             "fieldtype": "Data",
#             "width": 220
#         },
#         {
#             "label": "CUSTOMER CONTACT NO.",
#             "fieldname": "customer_contact_no",
#             "fieldtype": "Data",
#             "width": 220
#         },
#         {
#             "label": "CUSTOMER EMAIL ID",
#             "fieldname": "customer_email_id",
#             "fieldtype": "Data",
#             "width": 220
#         },
#         {
#             "label": "PO NO",
#             "fieldname": "po_no",
#             "fieldtype": "Data",
#             "width": 180
#         },
#         {
#             "label": "PO DATE",
#             "fieldname": "po_date",
#             "fieldtype": "Date",
#             "width": 140
#         },
#         {
#             "label": "PO VALUE",
#             "fieldname": "po_value",
#             "fieldtype": "Currency",
#             "width": 140
#         },
#         {
#             "label": "PO Received",
#             "fieldname": "po_received",
#             "fieldtype": "Date",
#             "width": 140
#         },
#         {
#             "label": "Customer Type",
#             "fieldname": "custom_customer_type",
#             "fieldtype": "Data",
#             "width": 150
#         },
#         {
#             "label": "Group Unit",
#             "fieldname": "custom_group_unit",
#             "fieldtype": "Data",
#             "width": 150
#         },
#         {
#             "label": "Type of Entity",
#             "fieldname": "custom_type_of_entity",
#             "fieldtype": "Data",
#             "width": 150
#         },
#         {
#             "label": "Sales Person",
#             "fieldname": "custom_sales_person",
#             "fieldtype": "Link",
#             "options": "Sales Person",
#             "width": 150
#         },
#         {
#             "label": "Territory",
#             "fieldname": "territory",
#             "fieldtype": "Link",
#             "options": "Territory",
#             "width": 150
#         },
#         {
#             "label": "Date Follow Up-1",
#             "fieldname": "custom_date",
#             "fieldtype": "Date",
#             "width": 140
#         },
#         {
#             "label": "Date Follow Up-2",
#             "fieldname": "custom_date_follow_up2",
#             "fieldtype": "Date",
#             "width": 140
#         },
#         {
#             "label": "Next Action To Be Done",
#             "fieldname": "custom_next_action_to_be_done",
#             "fieldtype": "Data",
#             "width": 200
#         },
#         {
#             "label": "Follow Up-1",
#             "fieldname": "custom_follow_up1",
#             "fieldtype": "Data",
#             "width": 200
#         },
#         {
#             "label": "Follow Up-2",
#             "fieldname": "custom_follow_up2",
#             "fieldtype": "Data",
#             "width": 200
#         },
#         {
#             "label": "Outcome",
#             "fieldname": "custom_outcome",
#             "fieldtype": "Data",
#             "width": 200
#         }
#     ]

#     return columns


# def get_data(filters):
#     conditions = ""
#     values = {}

#     if filters.get("from_date"):
#         conditions += " AND COALESCE(op.transaction_date, DATE(op.creation)) >= %(from_date)s"
#         values["from_date"] = filters.get("from_date")

#     if filters.get("to_date"):
#         conditions += " AND COALESCE(op.transaction_date, DATE(op.creation)) <= %(to_date)s"
#         values["to_date"] = filters.get("to_date")

#     if filters.get("sales_rep"):
#         conditions += " AND op.custom_sales_rep = %(sales_rep)s"
#         values["sales_rep"] = filters.get("sales_rep")

#     if filters.get("customer"):
#         conditions += " AND op.customer_name = %(customer)s"
#         values["customer"] = filters.get("customer")

#     if filters.get("enq_type"):
#         conditions += " AND op.custom_enquriry_type = %(enq_type)s"
#         values["enq_type"] = filters.get("enq_type")

#     data = frappe.db.sql(f"""
#         SELECT

#             ROW_NUMBER() OVER(ORDER BY op.creation DESC) as sr_no,

#             op.custom_enq_details as enq_details,

#             op.party_name as lead,

#             op.custom_enquriry_type as enq_type,

#             COALESCE(op.transaction_date, DATE(op.creation)) as enq_received_on,

#             op.custom_quotation as qtn_no,

#             op.custom_qtn_date as qtn_date,

#             op.custom_offer_qtn_sent_on_date as offer_qtn_sent_on_date,

#             COALESCE(op.customer_name, op.party_name) as customer,

#             op.custom_offer_status_ as offer_status,

#             COALESCE(op.state, ld.state) as place,

#             op.custom_sales_rep as sales_rep,

#             op.custom_project_client as project_client,

#             op.custom_item_product as item_product,

#             op.custom_material_special_design as material_special_design,

#             op.custom_qty_offered as qty_offered,

#             op.custom_offer_value_rs as offer_value_rs,

#             op.expected_closing as expected_in,

#             COALESCE(op.contact_person, ld.lead_name) as customer_contact_person,

#             CONCAT_WS(
#                 ' / ',
#                 NULLIF(op.contact_mobile, ''),
#                 NULLIF(op.phone, ''),
#                 NULLIF(op.whatsapp, '')
#             ) as customer_contact_no,

#             COALESCE(op.contact_email, ld.email_id) as customer_email_id,

#             op.custom_po_no as po_no,

#             op.custom_po_date as po_date,

#             op.custom_po_value as po_value,

#             op.custom_po_received as po_received,

#             op.custom_customer_type as custom_customer_type,

#             op.custom_group_unit as custom_group_unit,

#             op.custom_type_of_entity as custom_type_of_entity,

#             op.custom_sales_person as custom_sales_person,

#             op.territory as territory,

#             op.custom_date as custom_date,

#             op.custom_date_follow_up2 as custom_date_follow_up2,

#             op.custom_next_action_to_be_done as custom_next_action_to_be_done,

#             op.custom_follow_up1 as custom_follow_up1,

#             op.custom_follow_up2 as custom_follow_up2,

#             op.custom_outcome as custom_outcome

#         FROM `tabOpportunity` op

#         LEFT JOIN `tabLead` ld
#         ON ld.name = op.party_name
#         AND op.opportunity_from = 'Lead'

#         WHERE op.docstatus < 2
#         {conditions}

#         ORDER BY sr_no ASC

#     """, values, as_dict=True)

#     return data

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)

    return columns, data


def get_columns():
    columns = [
        {
            "label": "Lead Owner",
            "fieldname": "lead_owner",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Lead No (ID)",
            "fieldname": "lead_id",
            "fieldtype": "Link",
            "options": "Lead",
            "width": 160
        },
        {
            "label": "Opportunity No (ID)",
            "fieldname": "opportunity_id",
            "fieldtype": "Link",
            "options": "Opportunity",
            "width": 160
        },
        {
            "label": "ENQ DETAILS",
            "fieldname": "enq_details",
            "fieldtype": "Data",
            "width": 250
        },
        {
            "label": "LEAD",
            "fieldname": "lead",
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
            "width": 220
        },
        {
            "label": "CUSTOMER EMAIL ID",
            "fieldname": "customer_email_id",
            "fieldtype": "Data",
            "width": 220
        },
        {
            "label": "PO NO",
            "fieldname": "po_no",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "PO DATE",
            "fieldname": "po_date",
            "fieldtype": "Date",
            "width": 140
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
        },
        {
            "label": "Customer Type",
            "fieldname": "custom_customer_type",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Group Unit",
            "fieldname": "custom_group_unit",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Type of Entity",
            "fieldname": "custom_type_of_entity",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Sales Person",
            "fieldname": "custom_sales_person",
            "fieldtype": "Link",
            "options": "Sales Person",
            "width": 150
        },
        {
            "label": "Territory",
            "fieldname": "territory",
            "fieldtype": "Link",
            "options": "Territory",
            "width": 150
        },
        {
            "label": "Date Follow Up-1",
            "fieldname": "custom_date",
            "fieldtype": "Date",
            "width": 140
        },
        {
            "label": "Date Follow Up-2",
            "fieldname": "custom_date_follow_up2",
            "fieldtype": "Date",
            "width": 140
        },
        {
            "label": "Next Action To Be Done",
            "fieldname": "custom_next_action_to_be_done",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Follow Up-1",
            "fieldname": "custom_follow_up1",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Follow Up-2",
            "fieldname": "custom_follow_up2",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Outcome",
            "fieldname": "custom_outcome",
            "fieldtype": "Data",
            "width": 200
        }
    ]

    return columns


def get_data(filters):
    conditions = ""
    values = {}

    if filters.get("from_date"):
        conditions += " AND COALESCE(op.transaction_date, DATE(op.creation)) >= %(from_date)s"
        values["from_date"] = filters.get("from_date")

    if filters.get("to_date"):
        conditions += " AND COALESCE(op.transaction_date, DATE(op.creation)) <= %(to_date)s"
        values["to_date"] = filters.get("to_date")

    if filters.get("sales_rep"):
        conditions += " AND op.custom_sales_rep = %(sales_rep)s"
        values["sales_rep"] = filters.get("sales_rep")

    if filters.get("customer"):
        conditions += " AND op.customer_name = %(customer)s"
        values["customer"] = filters.get("customer")

    if filters.get("enq_type"):
        conditions += " AND op.custom_enquriry_type = %(enq_type)s"
        values["enq_type"] = filters.get("enq_type")

    data = frappe.db.sql(f"""
        SELECT

            ld.lead_owner as lead_owner,

            op.party_name as lead_id,

            op.name as opportunity_id,

            op.custom_enq_details as enq_details,

            op.party_name as lead,

            op.custom_enquriry_type as enq_type,

            COALESCE(op.transaction_date, DATE(op.creation)) as enq_received_on,

            op.custom_quotation as qtn_no,

            op.custom_qtn_date as qtn_date,

            op.custom_offer_qtn_sent_on_date as offer_qtn_sent_on_date,

            COALESCE(op.customer_name, op.party_name) as customer,

            op.custom_offer_status_ as offer_status,

            COALESCE(op.state, ld.state) as place,

            op.custom_sales_rep as sales_rep,

            op.custom_project_client as project_client,

            op.custom_item_product as item_product,

            op.custom_material_special_design as material_special_design,

            op.custom_qty_offered as qty_offered,

            op.custom_offer_value_rs as offer_value_rs,

            op.expected_closing as expected_in,

            COALESCE(op.contact_person, ld.lead_name) as customer_contact_person,

            CONCAT_WS(
                ' / ',
                NULLIF(op.contact_mobile, ''),
                NULLIF(op.phone, ''),
                NULLIF(op.whatsapp, '')
            ) as customer_contact_no,

            COALESCE(op.contact_email, ld.email_id) as customer_email_id,

            op.custom_po_no as po_no,

            op.custom_po_date as po_date,

            op.custom_po_value as po_value,

            op.custom_po_received as po_received,

            op.custom_customer_type as custom_customer_type,

            op.custom_group_unit as custom_group_unit,

            op.custom_type_of_entity as custom_type_of_entity,

            op.custom_sales_person as custom_sales_person,

            op.territory as territory,

            op.custom_date as custom_date,

            op.custom_date_follow_up2 as custom_date_follow_up2,

            op.custom_next_action_to_be_done as custom_next_action_to_be_done,

            op.custom_follow_up1 as custom_follow_up1,

            op.custom_follow_up2 as custom_follow_up2,

            op.custom_outcome as custom_outcome

        FROM `tabOpportunity` op

        LEFT JOIN `tabLead` ld
        ON ld.name = op.party_name
        AND op.opportunity_from = 'Lead'

        WHERE op.docstatus < 2
        {conditions}

        ORDER BY op.creation DESC

    """, values, as_dict=True)

    return data