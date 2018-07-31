from repocribro.extending import Extension


class RepocribroBadges(Extension):
    #: Name of pages extension
    NAME = 'badges'
    #: Category of pages extension
    CATEGORY = 'basic'
    #: Author of pages extension
    AUTHOR = 'Marek Suchánek'
    #: GitHub URL of pages extension
    GH_URL = 'https://github.com/MarekSuchanek/repocribro-badges'
    #: Priority of pages extension
    PRIORITY = 10

    # TODO: role for badge-assigner

    # TODO: model of badge related to repository

    # TODO: interface to add badge to repository (with preview)

    # TODO: list badges on repository detail

    # TODO: generate badge for using it externally (linkable)


def make_extension(*args, **kwargs):
    return RepocribroBadges(*args, **kwargs)
