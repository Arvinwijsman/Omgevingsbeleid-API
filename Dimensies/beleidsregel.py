from flask_restful import Resource, Api, fields, marshal, reqparse, inputs, abort
import records
import pyodbc
from flasgger import swag_from

from queries import *
from helpers import single_object_by_uuid, objects_from_query, related_objects_from_query, validate_UUID
from globals import db_connection_string, db_connection_settings
from uuid import UUID

resource_fields = {
    'UUID': fields.String,
    'Titel': fields.String,
    'Omschrijving':fields.String,
    'Weblink': fields.String,
    'Begin_Geldigheid': fields.DateTime(dt_format='iso8601'),
    'Eind_Geldigheid': fields.DateTime(dt_format='iso8601'),
    'Created_By': fields.String,
    'Created_Date': fields.DateTime(dt_format='iso8601'),
    'Modified_By': fields.String,
    'Modified_Date': fields.DateTime(dt_format='iso8601')}

create_argparser= reqparse.RequestParser()
create_argparser.add_argument('Titel', type=str, help="{error_msg}: De titel van dit object", required=True)
create_argparser.add_argument('Omschrijving', type=str, help="{error_msg}: De omschrijving van dit object", nullable=True)
create_argparser.add_argument('Weblink', type=str, help="{error_msg}: De weblink van dit object")
create_argparser.add_argument('Begin_Geldigheid', type=inputs.datetime_from_iso8601, help="{error_msg}: De datum waarop de geldigheid van dit object ingaat")
create_argparser.add_argument('Eind_Geldigheid', type=inputs.datetime_from_iso8601, help="{error_msg}: De datum waarop de geldigheid van dit object eindigt")
create_argparser.add_argument('Created_By', type=str, help="{error_msg}: De gebruiker die dit object heeft aangemaakt", required=True)
create_argparser.add_argument('Created_Date', type=inputs.datetime_from_iso8601, help="{error_msg}: De datum waarop dit object is aangemaakt", required=True)

modify_argparser = reqparse.RequestParser()
modify_argparser.add_argument('Titel', type=str, help="{error_msg}: De titel van dit object")
modify_argparser.add_argument('Omschrijving', type=str, help="{error_msg}: De omschrijving van dit object")
modify_argparser.add_argument('Weblink', type=str, help="{error_msg}: De weblink van dit object")
modify_argparser.add_argument('Begin_Geldigheid', type=inputs.datetime_from_iso8601, help="{error_msg}: De datum waarop de geldigheid van dit object ingaat")
modify_argparser.add_argument('Eind_Geldigheid', type=inputs.datetime_from_iso8601, help="{error_msg}: De datum waarop de geldigheid van dit object eindigt")
modify_argparser.add_argument('Modified_By', type=str, help="{error_msg}: De gebruiker die dit object heeft aangepast", required=True)
modify_argparser.add_argument('Modified_Date', type=inputs.datetime_from_iso8601, help="{error_msg}: De datum waarop dit object is aangepast", required=True)


class BeleidsRegel(Resource):
    """Deze resource vertegenwoordigd de Beleidsregels van de provincie"""
    @swag_from('beleidsregel.yml')
    def get(self, beleidsregel_uuid=None):
        if beleidsregel_uuid:
            val_beleidsregel_uuid = validate_UUID(beleidsregel_uuid)
            
            if not val_beleidsregel_uuid:
                return {'message': f"Waarde {beleidsregel_uuid} is geen geldige UUID"}, 400
            
            beleidsregel = single_object_by_uuid('BeleidsRegel', beleidsregel_op_uuid, uuid=beleidsregel_uuid)
            
            if not beleidsregel:
                return {'message': f"BeleidsRegel met UUID {beleidsregel_uuid} is niet gevonden"}, 400
            
            return marshal(beleidsregel.as_dict(), resource_fields)
        else:    
            beleidsregels = objects_from_query('BeleidsRegel', alle_beleidsregels)

            return marshal(list(map(lambda beleidsregel: beleidsregel.as_dict(), beleidsregels)), resource_fields)

    def post(self, beleidsregel_uuid=None):
        if beleidsregel_uuid:
            return {'message': "Methode POST niet geldig op een enkel object, verwijder identiteit uit URL"}, 400

        args = create_argparser.parse_args(strict=True)
        connection = pyodbc.connect(db_connection_settings)
        cursor = connection.cursor()
        cursor.execute(beleidsregel_aanmaken,
        args.Titel,
        args.Omschrijving,
        args.Weblink,
        args.Begin_Geldigheid,
        args.Eind_Geldigheid,
        args.Created_By,
        args.Created_Date,
        args.Created_By,
        args.Created_Date)
        new_uuid = cursor.fetchone()[0]
        connection.commit()
        return {"Resultaat_UUID": f"{new_uuid}"}
    
    def patch(self, beleidsregel_uuid=None):
        if not beleidsregel_uuid:
            return {'message': "Methode PATCH alleen geldig op een enkel object, voeg een identifier toe aan de URL"}, 400
        args = modify_argparser.parse_args(strict=True)
        val_beleidsregel_uuid = validate_UUID(beleidsregel_uuid)
        
        if not val_beleidsregel_uuid:
            return {'message': f"Waarde {beleidsregel_uuid} is geen geldige UUID"}, 400
        
        beleidsregel = single_object_by_uuid('BeleidsRegel', beleidsregel_op_uuid, uuid=beleidsregel_uuid)
        
        if not beleidsregel:
            return {'message': f"BeleidsRegel met UUID {beleidsregel_uuid} is niet gevonden"}, 400
            
        new_beleidsregel = beleidsregel.as_dict()
        for key in new_beleidsregel:
            if key in args and args[key]:
                new_beleidsregel[key] = args[key]
        
        connection = pyodbc.connect(db_connection_settings)
        cursor = connection.cursor()
        cursor.execute(
        beleidsregel_aanpassen,
        new_beleidsregel['ID'],
        new_beleidsregel['Titel'],
        new_beleidsregel['Omschrijving'],
        new_beleidsregel['Weblink'],
        new_beleidsregel['Begin_Geldigheid'],
        new_beleidsregel['Eind_Geldigheid'],
        new_beleidsregel['Created_By'],
        new_beleidsregel['Created_Date'],
        new_beleidsregel['Modified_By'],
        new_beleidsregel['Modified_Date'])
        new_uuid = cursor.fetchone()[0]
        connection.commit()
        return {"Resultaat_UUID": f"{new_uuid}"}


