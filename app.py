#!/usr/bin/env python
# encoding: utf-8
"""
#-------------------------------------------------------------------
#                                                                   
#                   @Project Name : chat-resume                 
#                                                                   
#                   @File Name    : app.py                      
#                                                                   
#                   @Programmer   : zhanglu                          
#                                                                     
#                   @Start Date   : 2023/5/23 13:06                 
#                                                                   
#                   @Last Update  : 2023/5/23 13:06                 
#                   
#                   @Description  : 
#                                                                   
#-------------------------------------------------------------------
# Classes:                                                          
#                                                                   
#-------------------------------------------------------------------
"""
from flask import jsonify, Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

api_response = {"respCode": 100, "respMsg": "success"}


class Positions(Resource):
    """
    position
    """

    def get(self):
        return jsonify({})

    def post(self):
        """
        create a new position
        :return:
        """
        data = request.get_json()
        position_name = data.get('name')
        job_detail = data.get('job_detail')
        print(position_name, job_detail)
        return jsonify(api_response)

    def put(self):
        return jsonify({})


class PositionResumes(Resource):
    def get(self, position_id):
        return jsonify({})

    def post(self, position_id):
        return jsonify({})


api.add_resource(Positions, '/positions')
api.add_resource(PositionResumes, '/positions/<int:position_id>/resumes')

if __name__ == '__main__':
    app.run()
