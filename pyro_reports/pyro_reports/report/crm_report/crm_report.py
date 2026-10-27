# import frappe


# def execute(filters=None):
#     filters = filters or {}
#     columns = get_columns()
#     data = get_data(filters)

#     # Total Offer Value
#     total_offer_value = sum((row.get("offer_value_rs") or 0) for row in data)

#     # Total row at the bottom
#     data.append({
#         "lead_owner": "TOTAL",
#         "offer_value_rs": total_offer_value
#     })

#     return columns, data


# def get_columns():
#     return [
#         {"label": "Lead Owner", "fieldname": "lead_owner", "fieldtype": "Data", "width": 150},                          # A
#         {"label": "Opportunity Owner", "fieldname": "opportunity_owner", "fieldtype": "Data", "width": 160},            # B
#         {"label": "ENQ DATE", "fieldname": "enq_date", "fieldtype": "Date", "width": 120},                              # C
#         {"label": "Customer Type", "fieldname": "customer_type", "fieldtype": "Data", "width": 150},                    # D
#         {"label": "Type of Entity", "fieldname": "type_of_entity", "fieldtype": "Data", "width": 150},                  # E
#         {"label": "Enq Type", "fieldname": "enq_type", "fieldtype": "Data", "width": 150},                              # F
#         {"label": "Group Unit", "fieldname": "group_unit", "fieldtype": "Data", "width": 150},                          # G
#         {"label": "ENQ RECEIVED ON DATE", "fieldname": "enq_received_on", "fieldtype": "Date", "width": 150},           # H
#         {"label": "ENQ. DUE DATE", "fieldname": "enq_due_date", "fieldtype": "Date", "width": 130},                     # I (blank)
#         {"label": "QTN. NO", "fieldname": "qtn_no", "fieldtype": "Data", "width": 120},                                 # J
#         {"label": "QTN. DATE", "fieldname": "qtn_date", "fieldtype": "Date", "width": 120},                             # K
#         {"label": "OFFER/QTN SENT ON DATE", "fieldname": "offer_qtn_sent_on_date", "fieldtype": "Date", "width": 180},  # L
#         {"label": "DAYS TAKEN TO SUBMIT THE OFFER", "fieldname": "days_taken_to_submit_offer", "fieldtype": "Int", "width": 200},  # M
#         {"label": "CUSTOMER", "fieldname": "customer", "fieldtype": "Data", "width": 220},                              # N
#         {"label": "Territory", "fieldname": "territory", "fieldtype": "Link", "options": "Territory", "width": 150},    # O
#         {"label": "SALES REP.", "fieldname": "sales_rep", "fieldtype": "Data", "width": 150},                           # P
#         {"label": "PROJECT/CLIENT", "fieldname": "project_client", "fieldtype": "Data", "width": 180},                  # Q
#         {"label": "ITEM/PRODUCT (OFFER)", "fieldname": "item_product", "fieldtype": "Data", "width": 180},              # R
#         {"label": "Category", "fieldname": "category", "fieldtype": "Data", "width": 150},                              # S
#         {"label": "MATERIAL/SPECIAL DESIGN", "fieldname": "material_special_design", "fieldtype": "Data", "width": 200},  # T
#         {"label": "QTY (OFFERED)", "fieldname": "qty_offered", "fieldtype": "Float", "width": 120},                     # U
#         {"label": "OFFER VALUE RS.", "fieldname": "offer_value_rs", "fieldtype": "Currency", "width": 150},             # V
#         {"label": "CUSTOMER CONTACT PERSON", "fieldname": "customer_contact_person", "fieldtype": "Data", "width": 220},  # W
#         {"label": "CUSTOMER CONTACT NO.", "fieldname": "customer_contact_no", "fieldtype": "Data", "width": 220},       # X
#         {"label": "CUSTOMER EMAIL ID", "fieldname": "customer_email_id", "fieldtype": "Data", "width": 220},            # Y
#         {"label": "PO NO/DATE", "fieldname": "po_no_date", "fieldtype": "Data", "width": 200},                          # Z
#         {"label": "PO VALUE", "fieldname": "po_value", "fieldtype": "Currency", "width": 140},                          # AA
#         {"label": "PO received", "fieldname": "po_received", "fieldtype": "Date", "width": 140},                        # AB
#         {"label": "Quoted Value", "fieldname": "quoted_value", "fieldtype": "Currency", "width": 140},                  # AC (blank)
#         {"label": "Order Lost", "fieldname": "order_lost", "fieldtype": "Data", "width": 140},                          # AD (blank)
#         {"label": "Date Follow Up 1", "fieldname": "date_follow_up1", "fieldtype": "Date", "width": 140},               # AE
#         {"label": "Follow Up 1", "fieldname": "follow_up1", "fieldtype": "Data", "width": 200},                         # AF
#         {"label": "Date Follow Up 2", "fieldname": "date_follow_up2", "fieldtype": "Date", "width": 140},               # AG
#         {"label": "Follow Up 2", "fieldname": "follow_up2", "fieldtype": "Data", "width": 200},                         # AH
#         {"label": "Next Action To Be Taken", "fieldname": "next_action", "fieldtype": "Data", "width": 200},            # AI
#         {"label": "Lead No ID", "fieldname": "lead_id", "fieldtype": "Link", "options": "Lead", "width": 160},          # AJ
#         {"label": "Opportunity No ID", "fieldname": "opportunity_id", "fieldtype": "Link", "options": "Opportunity", "width": 160},  # AK
#     ]


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
#         conditions += " AND op.enquriry_type = %(enq_type)s"
#         values["enq_type"] = filters.get("enq_type")

#     data = frappe.db.sql(f"""
#         SELECT
#             COALESCE(lu.full_name, ld.lead_owner) as lead_owner,
#             COALESCE(ou.full_name, op.opportunity_owner) as opportunity_owner,
#             op.transaction_date as enq_date,
#             op.custom_customer_type as customer_type,
#             op.custom_type_of_entity as type_of_entity,
#             op.enquriry_type as enq_type,
#             op.custom_group_unit as group_unit,
#             COALESCE(op.transaction_date, DATE(op.creation)) as enq_received_on,

#             NULL as enq_due_date,

#             op.custom_quotation as qtn_no,
#             op.custom_qtn_date as qtn_date,
#             op.custom_offer_qtn_sent_on_date as offer_qtn_sent_on_date,

#             CASE
#                 WHEN op.custom_offer_qtn_sent_on_date IS NOT NULL
#                 THEN DATEDIFF(
#                     op.custom_offer_qtn_sent_on_date,
#                     COALESCE(op.transaction_date, DATE(op.creation))
#                 ) + 1
#                 ELSE NULL
#             END as days_taken_to_submit_offer,

#             COALESCE(op.customer_name, op.party_name) as customer,
#             op.territory as territory,
#             op.custom_sales_person as sales_rep,
#             op.custom_project_client as project_client,
#             op.custom_item_product as item_product,

#             op.custom_order_booking_category as category,

#             op.custom_material_special_design as material_special_design,
#             op.custom_qty_offered as qty_offered,
#             op.custom_offer_value_rs as offer_value_rs,
#             COALESCE(op.contact_person, ld.lead_name) as customer_contact_person,

#             CONCAT_WS(
#                 ' / ',
#                 NULLIF(op.contact_mobile, ''),
#                 NULLIF(op.phone, ''),
#                 NULLIF(op.whatsapp, '')
#             ) as customer_contact_no,

#             COALESCE(op.contact_email, ld.email_id) as customer_email_id,

#             CONCAT_WS(
#                 ' / ',
#                 NULLIF(op.custom_po_no, ''),
#                 DATE_FORMAT(op.custom_po_date, '%%d-%%m-%%Y')
#             ) as po_no_date,

#             op.custom_po_value as po_value,
#             op.custom_po_received as po_received,

#             NULL as quoted_value,
#             NULL as order_lost,

#             op.custom_date as date_follow_up1,
#             op.custom_follow_up1 as follow_up1,
#             op.custom_date_follow_up2 as date_follow_up2,
#             op.custom_follow_up2 as follow_up2,
#             op.custom_next_action_to_be_done as next_action,

#             ld.name as lead_id,
#             op.name as opportunity_id

#         FROM `tabOpportunity` op
#         LEFT JOIN `tabLead` ld
#             ON ld.name = op.party_name
#             AND op.opportunity_from = 'Lead'
#         LEFT JOIN `tabUser` lu
#             ON lu.name = ld.lead_owner
#         LEFT JOIN `tabUser` ou
#             ON ou.name = op.opportunity_owner

#         WHERE op.docstatus < 2
#         {conditions}

#         ORDER BY op.creation DESC
#     """, values, as_dict=True)

#     return data

import frappe


def execute(filters=None):
    filters = filters or {}
    columns = get_columns()
    data = get_data(filters)

    # Show Opportunity details only once (on the first item row).
    # Later item rows of the same Opportunity keep only Items and Qty.
    keep_fields = ("items", "items_qty")
    previous_opportunity = None
    for row in data:
        current_opportunity = row.get("opportunity_id")
        if current_opportunity == previous_opportunity:
            for key in list(row.keys()):
                if key not in keep_fields:
                    row[key] = None
        else:
            previous_opportunity = current_opportunity

    # Total Offer Value (blank rows count as 0, so each Opportunity is counted once)
    total_offer_value = sum((row.get("offer_value_rs") or 0) for row in data)

    # Total row at the bottom
    data.append({
        "lead_owner": "TOTAL",
        "offer_value_rs": total_offer_value
    })

    return columns, data


def get_columns():
    return [
        {"label": "Lead Owner", "fieldname": "lead_owner", "fieldtype": "Data", "width": 150},
        {"label": "Opportunity Owner", "fieldname": "opportunity_owner", "fieldtype": "Data", "width": 160},
        {"label": "ENQ DATE", "fieldname": "enq_date", "fieldtype": "Date", "width": 120},
        {"label": "Customer Type", "fieldname": "customer_type", "fieldtype": "Data", "width": 150},
        {"label": "Type of Entity", "fieldname": "type_of_entity", "fieldtype": "Data", "width": 150},
        {"label": "Enq Type", "fieldname": "enq_type", "fieldtype": "Data", "width": 150},
        {"label": "Group Unit", "fieldname": "group_unit", "fieldtype": "Data", "width": 150},
        {"label": "ENQ RECEIVED ON DATE", "fieldname": "enq_received_on", "fieldtype": "Date", "width": 150},
        {"label": "ENQ. DUE DATE", "fieldname": "enq_due_date", "fieldtype": "Date", "width": 130},
        {"label": "QTN. NO", "fieldname": "qtn_no", "fieldtype": "Data", "width": 120},
        {"label": "QTN. DATE", "fieldname": "qtn_date", "fieldtype": "Date", "width": 120},
        {"label": "OFFER/QTN SENT ON DATE", "fieldname": "offer_qtn_sent_on_date", "fieldtype": "Date", "width": 180},
        {"label": "DAYS TAKEN TO SUBMIT THE OFFER", "fieldname": "days_taken_to_submit_offer", "fieldtype": "Int", "width": 200},
        {"label": "CUSTOMER", "fieldname": "customer", "fieldtype": "Data", "width": 220},
        {"label": "Territory", "fieldname": "territory", "fieldtype": "Link", "options": "Territory", "width": 150},
        {"label": "SALES REP.", "fieldname": "sales_rep", "fieldtype": "Data", "width": 150},
        {"label": "PROJECT/CLIENT", "fieldname": "project_client", "fieldtype": "Data", "width": 180},
        {"label": "Items", "fieldname": "items", "fieldtype": "Data", "width": 220},
        {"label": "Qty", "fieldname": "items_qty", "fieldtype": "Data", "width": 100},
        {"label": "Category", "fieldname": "category", "fieldtype": "Data", "width": 150},
        {"label": "MATERIAL/SPECIAL DESIGN", "fieldname": "material_special_design", "fieldtype": "Data", "width": 200},
        {"label": "QTY (OFFERED)", "fieldname": "qty_offered", "fieldtype": "Float", "width": 120},
        {"label": "OFFER VALUE RS.", "fieldname": "offer_value_rs", "fieldtype": "Currency", "width": 150},
        {"label": "CUSTOMER CONTACT PERSON", "fieldname": "customer_contact_person", "fieldtype": "Data", "width": 220},
        {"label": "CUSTOMER CONTACT NO.", "fieldname": "customer_contact_no", "fieldtype": "Data", "width": 220},
        {"label": "CUSTOMER EMAIL ID", "fieldname": "customer_email_id", "fieldtype": "Data", "width": 220},
        {"label": "PO NO/DATE", "fieldname": "po_no_date", "fieldtype": "Data", "width": 200},
        {"label": "PO VALUE", "fieldname": "po_value", "fieldtype": "Currency", "width": 140},
        {"label": "PO received", "fieldname": "po_received", "fieldtype": "Date", "width": 140},
        {"label": "Quoted Value", "fieldname": "quoted_value", "fieldtype": "Currency", "width": 140},
        {"label": "Order Lost", "fieldname": "order_lost", "fieldtype": "Data", "width": 140},
        {"label": "Date Follow Up 1", "fieldname": "date_follow_up1", "fieldtype": "Date", "width": 140},
        {"label": "Follow Up 1", "fieldname": "follow_up1", "fieldtype": "Data", "width": 200},
        {"label": "Date Follow Up 2", "fieldname": "date_follow_up2", "fieldtype": "Date", "width": 140},
        {"label": "Follow Up 2", "fieldname": "follow_up2", "fieldtype": "Data", "width": 200},
        {"label": "Next Action To Be Taken", "fieldname": "next_action", "fieldtype": "Data", "width": 200},
        {"label": "Lead No ID", "fieldname": "lead_id", "fieldtype": "Link", "options": "Lead", "width": 160},
        {"label": "Opportunity No ID", "fieldname": "opportunity_id", "fieldtype": "Link", "options": "Opportunity", "width": 160},
    ]


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
        conditions += " AND op.enquriry_type = %(enq_type)s"
        values["enq_type"] = filters.get("enq_type")

    data = frappe.db.sql(f"""
        SELECT
            COALESCE(lu.full_name, ld.lead_owner) as lead_owner,
            COALESCE(ou.full_name, op.opportunity_owner) as opportunity_owner,
            op.transaction_date as enq_date,
            op.custom_customer_type as customer_type,
            op.custom_type_of_entity as type_of_entity,
            op.enquriry_type as enq_type,
            op.custom_group_unit as group_unit,
            COALESCE(op.transaction_date, DATE(op.creation)) as enq_received_on,

            NULL as enq_due_date,

            op.custom_quotation as qtn_no,
            op.custom_qtn_date as qtn_date,
            op.custom_offer_qtn_sent_on_date as offer_qtn_sent_on_date,

            CASE
                WHEN op.custom_offer_qtn_sent_on_date IS NOT NULL
                THEN DATEDIFF(
                    op.custom_offer_qtn_sent_on_date,
                    COALESCE(op.transaction_date, DATE(op.creation))
                ) + 1
                ELSE NULL
            END as days_taken_to_submit_offer,

            COALESCE(op.customer_name, op.party_name) as customer,
            op.territory as territory,
            op.custom_sales_person as sales_rep,
            op.custom_project_client as project_client,

            oi.item_code as items,
            TRIM(TRAILING '.' FROM TRIM(TRAILING '0' FROM oi.qty)) as items_qty,

            op.custom_order_booking_category as category,

            op.custom_material_special_design as material_special_design,
            op.custom_qty_offered as qty_offered,
            op.custom_offer_value_rs as offer_value_rs,
            COALESCE(op.contact_person, ld.lead_name) as customer_contact_person,

            CONCAT_WS(
                ' / ',
                NULLIF(op.contact_mobile, ''),
                NULLIF(op.phone, ''),
                NULLIF(op.whatsapp, '')
            ) as customer_contact_no,

            COALESCE(op.contact_email, ld.email_id) as customer_email_id,

            CONCAT_WS(
                ' / ',
                NULLIF(op.custom_po_no, ''),
                DATE_FORMAT(op.custom_po_date, '%%d-%%m-%%Y')
            ) as po_no_date,

            op.custom_po_value as po_value,
            op.custom_po_received as po_received,

            NULL as quoted_value,
            NULL as order_lost,

            op.custom_date as date_follow_up1,
            op.custom_follow_up1 as follow_up1,
            op.custom_date_follow_up2 as date_follow_up2,
            op.custom_follow_up2 as follow_up2,
            op.custom_next_action_to_be_done as next_action,

            ld.name as lead_id,
            op.name as opportunity_id

        FROM `tabOpportunity` op
        LEFT JOIN `tabLead` ld
            ON ld.name = op.party_name
            AND op.opportunity_from = 'Lead'
        LEFT JOIN `tabUser` lu
            ON lu.name = ld.lead_owner
        LEFT JOIN `tabUser` ou
            ON ou.name = op.opportunity_owner
        LEFT JOIN `tabOpportunity Item` oi
            ON oi.parent = op.name
            AND oi.parenttype = 'Opportunity'

        WHERE op.docstatus < 2
        {conditions}

        ORDER BY op.creation DESC, op.name, oi.idx
    """, values, as_dict=True)

    return data