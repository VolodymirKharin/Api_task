from new_app.boards.models import Board



def parser_m(args):
    print(args)
    if args["name"] == 'crd' and args["op"] == 'gt':
        return Board.query.filter(Board.created_date > args["val"]).all()

    if args["name"] == 'crd' and args["op"] == 'lt':
        return Board.query.filter(Board.created_date < args["val"]).all()

    if args["name"] == 'mdd' and args["op"] == 'gt':
        return Board.query.filter(Board.modification_date > args["val"]).all()

    if args["name"] == 'mdd' and args["op"] == 'lt':
        return Board.query.filter(Board.modification_date < args["val"]).all()

    if args["name"] == 'st' and args["op"] == 'eq':
        return Board.query.filter(Board.status == args["val"]).all()