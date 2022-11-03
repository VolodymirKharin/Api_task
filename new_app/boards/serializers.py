from flask_restful import fields as fr_field

task_serializer = {
  'id': fr_field.Integer,
  'created_date': fr_field.DateTime(dt_format='iso8601'),
  'modification_date': fr_field.DateTime(dt_format='iso8601'),
  'execution_status': fr_field.Boolean,
  'text': fr_field.String,
}

board_serializer = {
  'id': fr_field.Integer,
  'created_date': fr_field.DateTime(dt_format='iso8601'),
  'modification_date': fr_field.DateTime(dt_format='iso8601'),
  'status': fr_field.String
}
