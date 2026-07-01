// frappe.query_reports["crm_report"] = {
//     "filters": [
//         {
//             "fieldname": "from_date",
//             "label": "From Date",
//             "fieldtype": "Date"
//         },
//         {
//             "fieldname": "to_date",
//             "label": "To Date",
//             "fieldtype": "Date"
//         },
//         {
//             "fieldname": "customer",
//             "label": "Customer",
//             "fieldtype": "Data"
//         },
//         {
//             "fieldname": "sales_rep",
//             "label": "Sales Rep",
//             "fieldtype": "Data"
//         },
//         {
//             "fieldname": "enq_type",
//             "label": "Enquiry Type",
//             "fieldtype": "Data"
//         }
//     ]
// };


frappe.query_reports["crm_report"] = {
    "filters": [
        {
            "fieldname": "from_date",
            "label": "From Date",
            "fieldtype": "Date",
            "default": frappe.datetime.month_start(),
            "reqd": 1
        },
        {
            "fieldname": "to_date",
            "label": "To Date",
            "fieldtype": "Date",
            "default": frappe.datetime.get_today(),
            "reqd": 1
        },
        {
            "fieldname": "customer",
            "label": "Customer",
            "fieldtype": "Data"
        },
        {
            "fieldname": "sales_rep",
            "label": "Sales Rep",
            "fieldtype": "Data"
        },
        {
            "fieldname": "enq_type",
            "label": "Enquiry Type",
            "fieldtype": "Data"
        }
    ]
};