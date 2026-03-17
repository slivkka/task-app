from tortoise import Model, fields


class Task(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    description = fields.TextField()
    status = fields.CharField(max_length=255, default='pending')

    user = fields.ForeignKeyField("models.User", related_name="tasks")

    class Meta:
        table = 'tasks'