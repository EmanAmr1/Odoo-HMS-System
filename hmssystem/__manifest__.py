{
  'name':'hms',
  'description':'hms system',
  'author':'iti',
  'depends':['base'],
  'data':['views/hms_system_views.xml',
          'views/hms_department_views.xml',
          'views/hms_doctors_views.xml',
          'views/hms_customers_views.xml',
          'views/res_groups.xml',
          'security/ir.model.access.csv',
          'reports/hms_patient_template.xml',
          'reports/report.xml'
          ]
}