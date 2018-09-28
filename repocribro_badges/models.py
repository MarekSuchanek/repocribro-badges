import datetime
import sqlalchemy


from repocribro.database import db
from repocribro.models import SearchableMixin, SerializableMixin,\
                              Repository, UserAccount


class Badge(db.Model, SearchableMixin, SerializableMixin):
    """Release from GitHub"""
    __tablename__ = 'Badge'
    __searchable__ = ['name', 'value']
    __serializable__ = ['id', 'hash', 'name', 'style', 'colorhex',
                        'issued_at', 'assigner_id', 'repository_id']
    #: Unique identifier of the page
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    #: URL slug for the page
    hash = sqlalchemy.Column(sqlalchemy.String(100), unique=True)
    #: Title of the page
    name = sqlalchemy.Column(sqlalchemy.UnicodeText)
    #: HTML page contents
    value = sqlalchemy.Column(sqlalchemy.UnicodeText)
    #: HTML page contents
    style = sqlalchemy.Column(sqlalchemy.String(100))
    #: HTML page contents
    colorhex = sqlalchemy.Column(sqlalchemy.String(7))
    #: Timestamp when assigned
    issued_at = sqlalchemy.Column(sqlalchemy.DateTime(),
                                  default=datetime.datetime.utcnow)
    #: ID of user's account within app
    assigner_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('UserAccount.id')
    )
    #: User's account within app
    assigner = sqlalchemy.orm.relationship(
        'UserAccount', back_populates='assigned_badges'
    )
    #: ID of the repository where release belongs to
    repository_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('Repository.id')
    )
    #: Repository where release belongs to
    repository = sqlalchemy.orm.relationship(
        'Repository', back_populates='badges'
    )

    def __repr__(self):
        """Standard string representation of DB object
        :return: Unique string representation
        :rtype: str
        """
        return '<Badge {} (#{})>'.format(self.hash, self.id)


# TODO: add to core model?
Repository.badges = sqlalchemy.orm.relationship(
    'Badge', back_populates='repository',
    cascade='all, delete-orphan'
)
UserAccount.assigned_badges = sqlalchemy.orm.relationship(
    'UserAccount', back_populates='assigner',
    cascade='all, delete-orphan'
)
