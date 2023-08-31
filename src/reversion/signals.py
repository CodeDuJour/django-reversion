from django.dispatch.dispatcher import Signal


# Version management signals.
pre_revision_commit = Signal()
post_revision_commit = Signal()
