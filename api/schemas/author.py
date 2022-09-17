from api import ma
from api.models.author import AuthorModel


class AuthorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AuthorModel
        exclude = ('id',) # указываем, какие поля мы не хотим видеть
        #include = ('name',)


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)
