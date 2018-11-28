import flask

from repocribro.security import permissions

from repocribro_badges.models import Badge


#: Badges controller blueprint
badges = flask.Blueprint('badges', __name__, url_prefix='/badges')


@badges.route('/<badge_hash>.svg', methods=['GET'])
def show_badge(badge_hash):
    db = flask.current_app.container.get('db')
    badge = db.session.query(Badge).filter_by(hash=badge_hash).first()
    if badge is None:
        badge = Badge('badge', 'not found', 'flat', '#aaaaaa')
    return flask.render_template(f'badges/{badge.style}.svg',
                                 name=badge.name, value=badge.value,
                                 color=badge.colorhex)


@badges.route('/create', methods=['POST'])
@permissions.roles.badger.require(403)
def create_badge():
    badge = Badge(...)
    # TODO get from form and create or return form with errors
    # TODO generate unique hash
    login, reponame = badge.repository.full_name.split('/')
    return flask.redirect(
        flask.url_for('core.repo',
                      login=login, reponame=reponame,
                      tab='pages')
    )


@badges.route('/<badge_hash>/delete', methods=['GET', 'DELETE'])
@permissions.roles.badger.require(403)
def delete_badge(badge_hash):
    db = flask.current_app.container.get('db')

    badge = db.session.query(Badge).filter_by(hash=badge_hash).first()
    if badge is None:
        flask.abort(404)

    db.session.delete(badge)
    db.session.commit()
    flask.flash('Badge has been deleted.', 'success')
    login, reponame = badge.repository.full_name.split('/')
    return flask.redirect(
        flask.url_for('core.repo',
                      login=login, reponame=reponame,
                      tab='pages')
    )
