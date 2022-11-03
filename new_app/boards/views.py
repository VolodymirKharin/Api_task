from flask import Response, Blueprint
from flask_restful import Resource, marshal_with
from webargs import fields
from webargs.flaskparser import use_args, abort
from new_app.boards.serializers import board_serializer, task_serializer
from new_app import db, api
from new_app.boards.functions import parser_m
from new_app.boards.models import Board, Task


boards = Blueprint('boards', __name__)

def get_bool(var: str):
    if var.lower() == 'true':
        return True
    elif var.lower() == 'false':
        return False
    return abort(404)

class BoardList(Resource):
    @marshal_with(board_serializer)
    @use_args({"name": fields.Str(),
               "op": fields.Str(),
               "val": fields.Str()
               }, location="query")
    def get(self, args):
        if not args:
            return Board.query.order_by(Board.id).all()
        return parser_m(args)


class TaskDetail(Resource):
    @marshal_with(task_serializer)
    def get(self, task_id=None):
        return Task.query.get_or_404(task_id)

    @use_args({"execution_status": fields.Bool(required=True)}, location="json")
    def put(self, *args, **kwargs):
        execution_status = args[0]["execution_status"]
        task_id = kwargs['task_id']
        task = Task.query.get_or_404(task_id)
        board_fk = task.board_fk
        if execution_status:
            db.session.query(Board).filter_by(id=int(board_fk)).update({'status': 'ARCHIVED'})
        else:
            db.session.query(Board).filter_by(id=int(board_fk)).update({'status': 'OPEN'})
        db.session.query(Task).filter_by(id=int(task_id)).update({'execution_status': execution_status})
        db.session.commit()
        return Response(status=204)

    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        board_fk = task.board_fk
        board = Board.query.get_or_404(board_fk)
        db.session.delete(board)
        db.session.commit()
        return Response(status=204)

class TaskList(Resource):
    @marshal_with(task_serializer)
    @use_args({"status": fields.String()}, location="query")
    def get(self, args=None):
        if not args:
            tasks = Task.query.order_by(Task.id).all()
        else:
            tasks = Task.query.filter(Task.execution_status == args["status"]).order_by(Task.id).all()
        return tasks

    @use_args({"text": fields.Str(required=True)}, location="json")
    def post(self, args):
        text = args["text"]
        board = Board()
        task = Task(text=text, board=board)
        db.session.add(board)
        db.session.add(task)
        db.session.commit()
        return Response(status=201)


#'/task/filter/created_date/?name=name&op=op&val=val
api.add_resource(BoardList, '/boards/')
api.add_resource(TaskList, '/tasks/')
api.add_resource(TaskDetail, '/task/<int:task_id>')


