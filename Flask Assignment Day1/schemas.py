from marshmallow import Schema, fields  # marshmallow에서 Schema와 fields를 임포트합니다.

class BookSchema(Schema):  # BookSchema 클래스를 정의하며 Schema를 상속받습니다.
    id = fields.Int(dump_only=True)  # id 필드를 정수형으로 정의하며, dump_only로 설정하여 읽기 전용으로 만듭니다.
    title = fields.String(required=True)  # title 필드를 문자열형으로 정의하며, 필수 입력으로 설정합니다.
    author = fields.String(required=True)  # author 필드를 문자열형으로 정의하며, 필수 입력으로 설정합니다.