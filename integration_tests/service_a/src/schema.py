from graphene import ObjectType, String, Int, List, NonNull, Field
from graphene_federation import build_schema, extend, external


@extend(fields='id')
class FileNode(ObjectType):
    id = external(Int(required=True))


class Message(ObjectType):
    id = Int(required=True)
    thread_id = Int(required=True)
    text = String(required=True)
    files = List(NonNull(FileNode))

    def resolve_files(self, info):
        return [FileNode(id=self.thread_id * 3)]


class Thread(ObjectType):
    id = Int(required=True)
    messages = List(NonNull(Message))

    def resolve_messages(self, info):
        return [
            Message(
                id=1,
                thread_id=self.id,
                text=f'text for message in thread {self.id}'
            )
        ]


class Query(ObjectType):
    thread = Field(Thread, id=Int(required=True))

    def resolve_thread(root, info, id):
        if id == 3:
            raise Exception('No access')
        return Thread(id=id)


schema = build_schema(query=Query)
