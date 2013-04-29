##
# Copyright (c) 2013 Sprymix Inc.
# All rights reserved.
#
# See LICENSE for details.
##


from metamagic.node.schema._objects import ClassObject, resolve_name
from metamagic.utils.fs import nodesystem


class FS(metaclass=ClassObject, baseclass=nodesystem.FSSystem):
    @classmethod
    def _apply_data(cls, dct, *, data, context):
        buckets = {}

        for bucket, spec in data.items():
            bucket_cls = resolve_name(context, bucket)
            buckets[bucket_cls] = spec['backends']

        dct['class_buckets'] = buckets
