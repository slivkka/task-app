from tortoise import fields, Model


class RefreshToken(Model):
    id = fields.IntField(pk=True)
    user = fields.CharField(max_length=255)
    token = fields.CharField(max_length=1000)
    expires_at = fields.DatetimeField()
    is_revoked = fields.BooleanField (default=False)
    created_at = fields.DatetimeField(auto_now_add=True)