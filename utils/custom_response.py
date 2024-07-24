def gen_response(error, success, message="", data=None):
        return {
            "error": error,
            "success": success,
            "message": message,
            "data": data if data else {}
        }
# class Result:
#     # def __init__(self):
#     #     self.result_code = 0
#     #     self.result_obj = {}
#     #     self.result_row_count = 0
#     #     self.message = ""


#     # def get(self):
#     #     return {'code': self.result_code, 'object': self.result_obj,'row_count':self.result_row_count ,'message': self.message}

