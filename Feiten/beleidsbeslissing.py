from flask_restful import Resource, Api, fields, marshal, reqparse, inputs, abort
import records
import pyodbc
from flasgger import swag_from

from queries import *
from helpers import *
from globals import db_connection_string, db_connection_settings
from uuid import UUID

resource_fields = {
    'UUID': UUIDfield,
    'Eigenaar_1': fields.String,
    'Eigenaar_2': fields.String,
    'Status': fields.String,
    'Titel': fields.String,
    'Omschrijving_Keuze':fields.String,
    'Omschrijving_Werking': fields.String,
    'Motivering': fields.String,
    'Aanleiding': fields.String,
    'Afweging': fields.String,
    'Verordening_Realisatie': fields.String,
    # Vanaf hier hebben we het over omgevingsbeleid objecten
    'Ambitie_Omschrijving': fields.String,
    'Werkingsgebieden':fields.List(UUIDfield, default=[], attribute='fk_WerkingsGebieden'),
    'BeleidsRelaties':fields.List(UUIDfield, default=[], attribute='fk_BeleidsRelaties'),
    'Verorderingen':fields.List(UUIDfield, default=[], attribute='fk_Verorderingen'),
    'Maatregelen':fields.List(UUIDfield, default=[], attribute='fk_Maatregelen'),
    'Beleids_regels':fields.List(UUIDfield, default=[], attribute='fk_BeleidsRegels'),
    'Themas':fields.List(UUIDfield, default=[], attribute='fk_Themas'),
    'Ambities':fields.List(UUIDfield, default=[], attribute='fk_Ambities'),
    'Doelen':fields.List(UUIDfield, default=[], attribute='fk_Doelen'),
    'Provinciale_belangen':fields.List(UUIDfield, default=[], attribute='fk_ProvincialeBelangen'),
    'Begin_Geldigheid': fields.DateTime(dt_format='iso8601'),
    'Eind_Geldigheid': fields.DateTime(dt_format='iso8601'),
    'Created_By': fields.String,
    'Created_Date': fields.DateTime(dt_format='iso8601'),
    'Modified_By': fields.String,
    'Modified_Date': fields.DateTime(dt_format='iso8601'),
    }

create_argparser= reqparse.RequestParser()
create_argparser.add_argument('Eigenaar_1', type=str, required=True)
create_argparser.add_argument('Eigenaar_2', type=str, required=True)
create_argparser.add_argument('Status', type=str, required=True)
create_argparser.add_argument('Titel', type=str, required=True)
create_argparser.add_argument('Omschrijving_Keuze', type=str)
create_argparser.add_argument('Omschrijving_Werking', type=str)
create_argparser.add_argument('Motivering', type=str)
create_argparser.add_argument('Aanleiding', type=str)
create_argparser.add_argument('Afweging', type=str)
create_argparser.add_argument('Verordening_Realisatie', type=str)
create_argparser.add_argument('Begin_Geldigheid', type=inputs.datetime_from_iso8601, required=True)
create_argparser.add_argument('Eind_Geldigheid', type=inputs.datetime_from_iso8601, required=True)
create_argparser.add_argument('Created_By', type=str, required=True)
create_argparser.add_argument('Created_Date', type=inputs.datetime_from_iso8601, required=True)

modify_argparser = reqparse.RequestParser()
modify_argparser.add_argument('Titel', type=str, help="{error_msg}: De titel van dit object")
modify_argparser.add_argument('Omschrijving', type=str, help="{error_msg}: De omschrijving van dit object")
modify_argparser.add_argument('Weblink', type=str, help="{error_msg}: De weblink van dit object")
modify_argparser.add_argument('Begin_Geldigheid', type=inputs.datetime_from_iso8601, help="{error_msg}: De datum waarop de geldigheid van dit object ingaat")
modify_argparser.add_argument('Eind_Geldigheid', type=inputs.datetime_from_iso8601, help="{error_msg}: De datum waarop de geldigheid van dit object eindigt")
modify_argparser.add_argument('Modified_By', type=str, help="{error_msg}: De gebruiker die dit object heeft aangepast", required=True)
modify_argparser.add_argument('Modified_Date', type=inputs.datetime_from_iso8601, help="{error_msg}: De datum waarop dit object is aangepast", required=True)


class BeleidsBeslissing(Resource):
    """Deze resource vertegenwoordigd de Beleidsregels van de provincie"""
    # @swag_from('provinciaalbelang.yml')
    def get(self, beleidsbeslissing_uuid=None):
        if beleidsbeslissing_uuid:
            val_beleidsbeslissing_uuid = validate_UUID(beleidsbeslissing_uuid)
            
            if not val_beleidsbeslissing_uuid:
                return {'message': f"Waarde {beleidsbeslissing_uuid} is geen geldige UUID"}, 400
            
            beleidsbeslissing = single_object_by_uuid('BeleidsBeslissing', beleidsbeslissing_op_uuid, uuid=beleidsbeslissing_uuid)
            
            if not beleidsbeslissing:
                return {'message': f"BeleidsBeslissing met UUID {beleidsbeslissing_uuid} is niet gevonden"}, 400
            
            flat_obs = flatten_obs(beleidsbeslissing_uuid)
            beleidsbeslissing = {**flat_obs, **beleidsbeslissing.as_dict()}
            print(beleidsbeslissing)
            return marshal(beleidsbeslissing, resource_fields)
        else:    
            beleidsbeslissingen = objects_from_query('BeleidsBeslissing', alle_beleidsbeslissingen)

            return marshal(list(map(lambda beleidsbeslissing: beleidsbeslissing.as_dict(), beleidsbeslissingen)), resource_fields)

    def post(self, beleidsbeslissing_uuid=None):
        if beleidsbeslissing_uuid:
            return {'message': "Methode POST niet geldig op een enkel object, verwijder identiteit uit URL"}, 400

        args = create_argparser.parse_args(strict=True)
        connection = pyodbc.connect(db_connection_settings)
        cursor = connection.cursor()
        cursor.execute(beleidsbeslissing_aanmaken,
        args.Eigenaar_1,
        args.Eigenaar_2,
        args.Status,
        args.Titel,
        args.Omschrijving_Keuze,
        args.Omschrijving_Werking,
        args.Motivering,
        args.Aanleiding,
        args.Afweging,
        args.Verordening_Realisatie,
        args.Begin_Geldigheid,
        args.Eind_Geldigheid,
        args.Created_By,
        args.Created_Date,
        args.Created_By,
        args.Created_Date)
        new_uuid = cursor.fetchone()[0]
        connection.commit()
        return {"Resultaat_UUID": f"{new_uuid}"}
    
    # def patch(self, provinciaalbelang_uuid=None):
        # if not provinciaalbelang_uuid:
            # return {'message': "Methode PATCH alleen geldig op een enkel object, voeg een identifier toe aan de URL"}, 400
        # args = modify_argparser.parse_args(strict=True)
        # val_provinciaalbelang_uuid = validate_UUID(provinciaalbelang_uuid)
        
        # if not val_provinciaalbelang_uuid:
            # return {'message': f"Waarde {provinciaalbelang_uuid} is geen geldige UUID"}, 400
        
        # provinciaalbelang = single_object_by_uuid('Provinciaalbelang', provinciaalbelang_op_uuid, uuid=provinciaalbelang_uuid)
        
        # if not provinciaalbelang:
            # return {'message': f"BeleidsRegel met UUID {provinciaalbelang_uuid} is niet gevonden"}, 400
            
        # new_provinciaalbelang = provinciaalbelang.as_dict()
        # for key in new_provinciaalbelang:
            # if key in args and args[key]:
                # new_provinciaalbelang[key] = args[key]
        
        # connection = pyodbc.connect(db_connection_settings)
        # cursor = connection.cursor()
        # cursor.execute(
        # provinciaalbelang_aanpassen,
        # new_provinciaalbelang['ID'],
        # new_provinciaalbelang['Titel'],
        # new_provinciaalbelang['Omschrijving'],
        # new_provinciaalbelang['Weblink'],
        # new_provinciaalbelang['Begin_Geldigheid'],
        # new_provinciaalbelang['Eind_Geldigheid'],
        # new_provinciaalbelang['Created_By'],
        # new_provinciaalbelang['Created_Date'],
        # new_provinciaalbelang['Modified_By'],
        # new_provinciaalbelang['Modified_Date'])
        # new_uuid = cursor.fetchone()[0]
        # connection.commit()
        # return {"Resultaat_UUID": f"{new_uuid}"}


