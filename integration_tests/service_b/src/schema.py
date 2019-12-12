from graphene import ObjectType, String, Int
from graphene_federation import build_schema, key


@key(fields='id')
class FileNode(ObjectType):
    id = Int(required=True)
    url = String(required=True)

    def __resolve_reference(self, info, **kwargs):
        # todo test raise exception here
        return FileNode(id=self.id, url=f'files.com/{self.id}')


types = [
    FileNode,
]

schema = build_schema(types=types)
