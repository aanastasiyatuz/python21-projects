from peewee import Model

class BaseSerializer:
    class Meta:
        fields = []
        model = Model

    def serialize_obj(self, obj):
        fields = self.Meta.fields
        representation = {}
        for field in fields:
            data = getattr(obj, field)
            representation[field] = str(data)
        return representation
    
    def serialize_queryset(self, queryset=None):
        if queryset is None:
            queryset = self.Meta.model.select()
        representation = []
        for obj in queryset:
            representation.append(self.serialize_obj(obj))
        return representation
