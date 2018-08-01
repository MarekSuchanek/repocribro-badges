import flask


#: Badges controller blueprint
badges = flask.Blueprint('badges', __name__, url_prefix='/badges')


@badges.route('/<hash>.svg')
def show_badge(hash):
    # TODO: get badge from DB
    # TODO: return svg badge or 404
    ...

