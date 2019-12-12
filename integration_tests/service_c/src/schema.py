from graphene import ObjectType, String, Int, Field
from graphene_federation import build_schema, extend, external


class Creds(ObjectType):
    token = String(required=True)


@extend(fields='id')
class Thread(ObjectType):
    id = external(Int(required=True))
    creds = Field(Creds)

    def resolve_creds(self, info):
        return Creds(token=f'some_secret_token_for_{self.id}')


schema = build_schema(types=[Thread])
