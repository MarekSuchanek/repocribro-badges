import flask

from ..models import Badge


#: Badges controller blueprint
badges = flask.Blueprint('badges', __name__, url_prefix='/badges')


@badges.route('/<hash>.svg')
def show_badge(hash):
    # TODO: get badge from DB or 404
    badge = Badge()
    return flask.render_template(f'badges/{badge.style}.svg',
                                 name=badge.name, value=badge.value,
                                 color=badge.colorhex)


# TODO: security
@badges.route('/create', method=['POST'])
def create_badge():
    # TODO get from form and create or return form with errors
    # TODO generate unique hash
    return flask.redirect(...) # TODO: to badge repo


@badges.route('/<hash>/delete', method=['GET', 'DELETE'])
def delete_badge():
    # TODO get badge from DB or 404
    # TODO delete badge
    return flask.redirect(...) # TODO: to badge repo
