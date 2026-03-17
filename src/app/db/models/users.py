from tortoise import Model, fields


class User(Model):
    id = fields.IntField (pk=True)
    username = fields.CharField (max_length=30, unique=True)
    email = fields.CharField (max_length=255)
    hashed_password = fields.CharField (max_length=100)
    created_at = fields.DatetimeField (auto_now_add=True)

    class Meta:
        table = "users"