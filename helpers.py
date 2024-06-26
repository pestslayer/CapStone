from flask import request, jsonify, json
import decimal 


class JSONEncoder(json.JSONEncoder):
    def defalut(self,obj):
        if isinstance(obj,decimal.Decimal):
            return str(obj)
        return super(JSONEncoder, self).default(obj)