"""empty message

Revision ID: 2b26c46368ec
Revises: 
Create Date: 2022-05-03 11:17:42.873394

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

import app.util.sqlalchemy

# revision identifiers, used by Alembic.
revision = '2b26c46368ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    create_seq("seq_Gebruikers")
    op.create_table('Gebruikers',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Gebruikersnaam', sa.Unicode(length=50), nullable=False),
    sa.Column('Wachtwoord', sa.Unicode(), nullable=True),
    sa.Column('Rol', sa.Unicode(length=50), nullable=False),
    sa.Column('Email', sa.Unicode(length=265), nullable=True),
    sa.Column('Status', sa.Unicode(length=50), server_default=sa.text("('Actief')"), nullable=True),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Gebruikers]'), nullable=False),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Gebruikers'))
    )

    create_seq("seq_Ambities")
    op.create_table('Ambities',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Created_Date', sa.DateTime(), nullable=False),
    sa.Column('Modified_Date', sa.DateTime(), nullable=False),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Titel', sa.Unicode(length=150), nullable=False),
    sa.Column('Omschrijving', sa.Unicode(), nullable=True),
    sa.Column('Weblink', sa.Unicode(), nullable=True),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Ambities]'), nullable=False),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Ambities_Created_By')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Ambities_Modified_By')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Ambities'))
    )

    create_seq("seq_Belangen")
    op.create_table('Belangen',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Created_Date', sa.DateTime(), nullable=False),
    sa.Column('Modified_Date', sa.DateTime(), nullable=False),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Titel', sa.Unicode(length=150), nullable=False),
    sa.Column('Omschrijving', sa.Unicode(), nullable=True),
    sa.Column('Weblink', sa.Unicode(), nullable=True),
    sa.Column('Type', sa.Unicode(), nullable=True),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Belangen]'), nullable=False),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Belangen_Created_By')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Belangen_Modified_By')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Belangen'))
    )

    create_seq("seq_Beleidsdoelen")
    op.create_table('Beleidsdoelen',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Created_Date', sa.DateTime(), nullable=False),
    sa.Column('Modified_Date', sa.DateTime(), nullable=False),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Titel', sa.Unicode(length=150), nullable=False),
    sa.Column('Omschrijving', sa.Unicode(), nullable=True),
    sa.Column('Weblink', sa.Unicode(), nullable=True),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Beleidsdoelen]'), nullable=False),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Beleidsdoelen_Created_By')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Beleidsdoelen_Modified_By')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Beleidsdoelen'))
    )

    create_seq("seq_Beleidskeuzes")
    op.create_table('Beleidskeuzes',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Created_Date', sa.DateTime(), nullable=False),
    sa.Column('Modified_Date', sa.DateTime(), nullable=False),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Eigenaar_1', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Eigenaar_2', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Portefeuillehouder_1', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Portefeuillehouder_2', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Opdrachtgever', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Aanpassing_Op', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Titel', sa.Unicode(), nullable=False),
    sa.Column('Omschrijving_Keuze', sa.Unicode(), nullable=True),
    sa.Column('Omschrijving_Werking', sa.Unicode(), nullable=True),
    sa.Column('Provinciaal_Belang', sa.Unicode(), nullable=True),
    sa.Column('Aanleiding', sa.Unicode(), nullable=True),
    sa.Column('Afweging', sa.Unicode(), nullable=True),
    sa.Column('Besluitnummer', sa.Unicode(), nullable=True),
    sa.Column('Tags', sa.Unicode(), nullable=True),
    sa.Column('Status', sa.Unicode(length=50), nullable=False),
    sa.Column('Weblink', sa.Unicode(length=200), nullable=True),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Beleidskeuzes]'), nullable=False),
    sa.ForeignKeyConstraint(['Aanpassing_Op'], ['Beleidskeuzes.UUID'], name=op.f('FK_Beleidskeuzes_Aanpassing_Op')),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Beleidskeuzes_Created_By')),
    sa.ForeignKeyConstraint(['Eigenaar_1'], ['Gebruikers.UUID'], name=op.f('FK_Beleidskeuzes_Eigenaar_1')),
    sa.ForeignKeyConstraint(['Eigenaar_2'], ['Gebruikers.UUID'], name=op.f('FK_Beleidskeuzes_Eigenaar_2')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Beleidskeuzes_Modified_By')),
    sa.ForeignKeyConstraint(['Opdrachtgever'], ['Gebruikers.UUID'], name=op.f('FK_Beleidskeuzes_Opdrachtgever')),
    sa.ForeignKeyConstraint(['Portefeuillehouder_1'], ['Gebruikers.UUID'], name=op.f('FK_Beleidskeuzes_Portefeuillehouder_1')),
    sa.ForeignKeyConstraint(['Portefeuillehouder_2'], ['Gebruikers.UUID'], name=op.f('FK_Beleidskeuzes_Portefeuillehouder_2')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Beleidskeuzes'))
    )

    create_seq("seq_Beleidsmodules")
    op.create_table('Beleidsmodules',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Created_Date', sa.DateTime(), nullable=False),
    sa.Column('Modified_Date', sa.DateTime(), nullable=False),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Titel', sa.Unicode(length=150), nullable=False),
    sa.Column('Besluit_Datum', sa.DateTime(), nullable=True),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Beleidsmodules]'), nullable=False),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Beleidsmodules_Created_By')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Beleidsmodules_Modified_By')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Beleidsmodules'))
    )

    create_seq("seq_Beleidsprestaties")
    op.create_table('Beleidsprestaties',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Created_Date', sa.DateTime(), nullable=False),
    sa.Column('Modified_Date', sa.DateTime(), nullable=False),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Titel', sa.Unicode(length=150), nullable=False),
    sa.Column('Omschrijving', sa.Unicode(), nullable=True),
    sa.Column('Weblink', sa.Unicode(), nullable=True),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Beleidsprestaties]'), nullable=False),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Beleidsprestaties_Created_By')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Beleidsprestaties_Modified_By')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Beleidsprestaties'))
    )

    create_seq("seq_Beleidsregels")
    op.create_table('Beleidsregels',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Created_Date', sa.DateTime(), nullable=False),
    sa.Column('Modified_Date', sa.DateTime(), nullable=False),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Titel', sa.Unicode(length=150), nullable=False),
    sa.Column('Omschrijving', sa.Unicode(), nullable=True),
    sa.Column('Weblink', sa.Unicode(), nullable=True),
    sa.Column('Externe_URL', sa.String(length=300, collation='SQL_Latin1_General_CP1_CI_AS'), nullable=True),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Beleidsregels]'), nullable=False),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Beleidsregels_Created_By')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Beleidsregels_Modified_By')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Beleidsregels'))
    )

    create_seq("seq_Themas")
    op.create_table('Themas',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Created_Date', sa.DateTime(), nullable=False),
    sa.Column('Modified_Date', sa.DateTime(), nullable=False),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Titel', sa.Unicode(length=150), nullable=False),
    sa.Column('Omschrijving', sa.Unicode(), nullable=True),
    sa.Column('Weblink', sa.Unicode(), nullable=True),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Themas]'), nullable=False),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Themas_Created_By')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Themas_Modified_By')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Themas'))
    )

    create_seq("seq_Verordeningstructuur")
    op.create_table('Verordeningstructuur',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Created_Date', sa.DateTime(), nullable=False),
    sa.Column('Modified_Date', sa.DateTime(), nullable=False),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Titel', sa.Unicode(length=150), nullable=False),
    sa.Column('Structuur', mssql.XML(), nullable=False),
    sa.Column('Status', sa.Unicode(length=50), nullable=True),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Verordeningstructuur]'), nullable=False),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Verordeningstructuur_Created_By')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Verordeningstructuur_Modified_By')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Verordeningstructuur'))
    )

    create_seq("seq_Werkingsgebieden")
    op.create_table('Werkingsgebieden',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Created_Date', sa.DateTime(), nullable=False),
    sa.Column('Modified_Date', sa.DateTime(), nullable=False),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Werkingsgebied', sa.Unicode(), nullable=False),
    sa.Column('symbol', sa.Unicode(length=265), nullable=True),
    sa.Column('SHAPE', app.util.sqlalchemy.Geometry(), nullable=False),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Werkingsgebieden]'), nullable=False),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Werkingsgebieden_Created_By')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Werkingsgebieden_Modified_By')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Werkingsgebieden'))
    )

    op.create_table('Beleidskeuze_Ambities',
    sa.Column('Beleidskeuze_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Ambitie_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Koppeling_Omschrijving', sa.String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=True),
    sa.ForeignKeyConstraint(['Ambitie_UUID'], ['Ambities.UUID'], name=op.f('FK_Beleidskeuze_Ambities_Ambitie_UUID')),
    sa.ForeignKeyConstraint(['Beleidskeuze_UUID'], ['Beleidskeuzes.UUID'], name=op.f('FK_Beleidskeuze_Ambities_Beleidskeuze_UUID')),
    sa.PrimaryKeyConstraint('Beleidskeuze_UUID', 'Ambitie_UUID', name=op.f('PK_Beleidskeuze_Ambities'))
    )

    op.create_table('Beleidskeuze_Belangen',
    sa.Column('Beleidskeuze_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Belang_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Koppeling_Omschrijving', sa.String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=True),
    sa.ForeignKeyConstraint(['Belang_UUID'], ['Belangen.UUID'], name=op.f('FK_Beleidskeuze_Belangen_Belang_UUID')),
    sa.ForeignKeyConstraint(['Beleidskeuze_UUID'], ['Beleidskeuzes.UUID'], name=op.f('FK_Beleidskeuze_Belangen_Beleidskeuze_UUID')),
    sa.PrimaryKeyConstraint('Beleidskeuze_UUID', 'Belang_UUID', name=op.f('PK_Beleidskeuze_Belangen'))
    )

    op.create_table('Beleidskeuze_Beleidsdoelen',
    sa.Column('Beleidskeuze_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Beleidsdoel_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Koppeling_Omschrijving', sa.String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=True),
    sa.ForeignKeyConstraint(['Beleidsdoel_UUID'], ['Beleidsdoelen.UUID'], name=op.f('FK_Beleidskeuze_Beleidsdoelen_Beleidsdoel_UUID')),
    sa.ForeignKeyConstraint(['Beleidskeuze_UUID'], ['Beleidskeuzes.UUID'], name=op.f('FK_Beleidskeuze_Beleidsdoelen_Beleidskeuze_UUID')),
    sa.PrimaryKeyConstraint('Beleidskeuze_UUID', 'Beleidsdoel_UUID', name=op.f('PK_Beleidskeuze_Beleidsdoelen'))
    )

    op.create_table('Beleidskeuze_Beleidsprestaties',
    sa.Column('Beleidskeuze_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Beleidsprestatie_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Koppeling_Omschrijving', sa.String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=True),
    sa.ForeignKeyConstraint(['Beleidskeuze_UUID'], ['Beleidskeuzes.UUID'], name=op.f('FK_Beleidskeuze_Beleidsprestaties_Beleidskeuze_UUID')),
    sa.ForeignKeyConstraint(['Beleidsprestatie_UUID'], ['Beleidsprestaties.UUID'], name=op.f('FK_Beleidskeuze_Beleidsprestaties_Beleidsprestatie_UUID')),
    sa.PrimaryKeyConstraint('Beleidskeuze_UUID', 'Beleidsprestatie_UUID', name=op.f('PK_Beleidskeuze_Beleidsprestaties'))
    )

    op.create_table('Beleidskeuze_Beleidsregels',
    sa.Column('Beleidskeuze_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Beleidsregel_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Koppeling_Omschrijving', sa.String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=True),
    sa.ForeignKeyConstraint(['Beleidskeuze_UUID'], ['Beleidskeuzes.UUID'], name=op.f('FK_Beleidskeuze_Beleidsregels_Beleidskeuze_UUID')),
    sa.ForeignKeyConstraint(['Beleidsregel_UUID'], ['Beleidsregels.UUID'], name=op.f('FK_Beleidskeuze_Beleidsregels_Beleidsregel_UUID')),
    sa.PrimaryKeyConstraint('Beleidskeuze_UUID', 'Beleidsregel_UUID', name=op.f('PK_Beleidskeuze_Beleidsregels'))
    )

    op.create_table('Beleidskeuze_Themas',
    sa.Column('Beleidskeuze_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Thema_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Koppeling_Omschrijving', sa.String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=True),
    sa.ForeignKeyConstraint(['Beleidskeuze_UUID'], ['Beleidskeuzes.UUID'], name=op.f('FK_Beleidskeuze_Themas_Beleidskeuze_UUID')),
    sa.ForeignKeyConstraint(['Thema_UUID'], ['Themas.UUID'], name=op.f('FK_Beleidskeuze_Themas_Thema_UUID')),
    sa.PrimaryKeyConstraint('Beleidskeuze_UUID', 'Thema_UUID', name=op.f('PK_Beleidskeuze_Themas'))
    )

    op.create_table('Beleidskeuze_Werkingsgebieden',
    sa.Column('Beleidskeuze_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Werkingsgebied_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Koppeling_Omschrijving', sa.String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=True),
    sa.ForeignKeyConstraint(['Beleidskeuze_UUID'], ['Beleidskeuzes.UUID'], name=op.f('FK_Beleidskeuze_Werkingsgebieden_Beleidskeuze_UUID')),
    sa.ForeignKeyConstraint(['Werkingsgebied_UUID'], ['Werkingsgebieden.UUID'], name=op.f('FK_Beleidskeuze_Werkingsgebieden_Werkingsgebied_UUID')),
    sa.PrimaryKeyConstraint('Beleidskeuze_UUID', 'Werkingsgebied_UUID', name=op.f('PK_Beleidskeuze_Werkingsgebieden'))
    )

    op.create_table('Beleidsmodule_Beleidskeuzes',
    sa.Column('Beleidsmodule_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Beleidskeuze_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Koppeling_Omschrijving', sa.String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=True),
    sa.ForeignKeyConstraint(['Beleidskeuze_UUID'], ['Beleidskeuzes.UUID'], name=op.f('FK_Beleidsmodule_Beleidskeuzes_Beleidskeuze_UUID')),
    sa.ForeignKeyConstraint(['Beleidsmodule_UUID'], ['Beleidsmodules.UUID'], name=op.f('FK_Beleidsmodule_Beleidskeuzes_Beleidsmodule_UUID')),
    sa.PrimaryKeyConstraint('Beleidsmodule_UUID', 'Beleidskeuze_UUID', name=op.f('PK_Beleidsmodule_Beleidskeuzes'))
    )

    create_seq("seq_Beleidsrelaties")
    op.create_table('Beleidsrelaties',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=True),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=True),
    sa.Column('Created_Date', sa.DateTime(), nullable=True),
    sa.Column('Modified_Date', sa.DateTime(), nullable=True),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Omschrijving', sa.Unicode(), nullable=True),
    sa.Column('Status', sa.Unicode(length=50), nullable=True),
    sa.Column('Aanvraag_Datum', sa.DateTime(), nullable=True),
    sa.Column('Datum_Akkoord', sa.DateTime(), nullable=True),
    sa.Column('Titel', sa.Unicode(length=50), server_default=sa.text("('Titel')"), nullable=False),
    sa.Column('Van_Beleidskeuze', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Naar_Beleidskeuze', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Beleidsrelaties]'), nullable=False),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Beleidsrelaties_Created_By')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Beleidsrelaties_Modified_By')),
    sa.ForeignKeyConstraint(['Naar_Beleidskeuze'], ['Beleidskeuzes.UUID'], name=op.f('FK_Beleidsrelaties_Naar_Beleidskeuze')),
    sa.ForeignKeyConstraint(['Van_Beleidskeuze'], ['Beleidskeuzes.UUID'], name=op.f('FK_Beleidsrelaties_Van_Beleidskeuze')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Beleidsrelaties'))
    )

    create_seq("seq_Maatregelen")
    op.create_table('Maatregelen',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Created_Date', sa.DateTime(), nullable=False),
    sa.Column('Modified_Date', sa.DateTime(), nullable=False),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Titel', sa.Unicode(), nullable=False),
    sa.Column('Omschrijving', sa.Unicode(), nullable=True),
    sa.Column('Toelichting', sa.Unicode(), nullable=True),
    sa.Column('Toelichting_Raw', sa.Unicode(), nullable=True),
    sa.Column('Weblink', sa.Unicode(), nullable=True),
    sa.Column('Gebied', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Status', sa.Unicode(length=50), nullable=True),
    sa.Column('Gebied_Duiding', sa.Unicode(), nullable=True),
    sa.Column('Tags', sa.Unicode(), nullable=True),
    sa.Column('Aanpassing_Op', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Eigenaar_1', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Eigenaar_2', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Portefeuillehouder_1', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Portefeuillehouder_2', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Opdrachtgever', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Maatregelen]'), nullable=False),
    sa.ForeignKeyConstraint(['Aanpassing_Op'], ['Maatregelen.UUID'], name=op.f('FK_Maatregelen_Aanpassing_Op')),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Maatregelen_Created_By')),
    sa.ForeignKeyConstraint(['Eigenaar_1'], ['Gebruikers.UUID'], name=op.f('FK_Maatregelen_Eigenaar_1')),
    sa.ForeignKeyConstraint(['Eigenaar_2'], ['Gebruikers.UUID'], name=op.f('FK_Maatregelen_Eigenaar_2')),
    sa.ForeignKeyConstraint(['Gebied'], ['Werkingsgebieden.UUID'], name=op.f('FK_Maatregelen_Gebied')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Maatregelen_Modified_By')),
    sa.ForeignKeyConstraint(['Opdrachtgever'], ['Gebruikers.UUID'], name=op.f('FK_Maatregelen_Opdrachtgever')),
    sa.ForeignKeyConstraint(['Portefeuillehouder_1'], ['Gebruikers.UUID'], name=op.f('FK_Maatregelen_Portefeuillehouder_1')),
    sa.ForeignKeyConstraint(['Portefeuillehouder_2'], ['Gebruikers.UUID'], name=op.f('FK_Maatregelen_Portefeuillehouder_2')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Maatregelen'))
    )

    create_seq("seq_Onderverdeling")
    op.create_table('Onderverdeling',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Created_Date', sa.DateTime(), nullable=False),
    sa.Column('Modified_Date', sa.DateTime(), nullable=False),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Onderverdeling', sa.Unicode(), nullable=False),
    sa.Column('symbol', sa.Unicode(length=265), nullable=True),
    sa.Column('Werkingsgebied', sa.Unicode(length=256), nullable=True),
    sa.Column('UUID_Werkingsgebied', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('SHAPE', app.util.sqlalchemy.Geometry(), nullable=False),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Onderverdeling]'), nullable=False),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Onderverdeling_Created_By')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Onderverdeling_Modified_By')),
    sa.ForeignKeyConstraint(['UUID_Werkingsgebied'], ['Werkingsgebieden.UUID'], name=op.f('FK_Onderverdeling_UUID_Werkingsgebied')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Onderverdeling'))
    )

    create_seq("seq_Verordeningen")
    op.create_table('Verordeningen',
    sa.Column('UUID', mssql.UNIQUEIDENTIFIER(), server_default=sa.text('(newid())'), nullable=False),
    sa.Column('Begin_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Eind_Geldigheid', sa.DateTime(), nullable=False),
    sa.Column('Created_Date', sa.DateTime(), nullable=False),
    sa.Column('Modified_Date', sa.DateTime(), nullable=False),
    sa.Column('Created_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Modified_By', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Portefeuillehouder_1', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Portefeuillehouder_2', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Eigenaar_1', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Eigenaar_2', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Opdrachtgever', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Titel', sa.Unicode(), nullable=True),
    sa.Column('Inhoud', sa.Unicode(), nullable=True),
    sa.Column('Weblink', sa.Unicode(), nullable=True),
    sa.Column('Status', sa.Unicode(length=50), nullable=False),
    sa.Column('Type', sa.Unicode(), nullable=False),
    sa.Column('Gebied', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('Volgnummer', sa.Unicode(), nullable=False),
    sa.Column('ID', sa.Integer(), server_default=sa.text('NEXT VALUE FOR [seq_Verordeningen]'), nullable=False),
    sa.ForeignKeyConstraint(['Created_By'], ['Gebruikers.UUID'], name=op.f('FK_Verordeningen_Created_By')),
    sa.ForeignKeyConstraint(['Eigenaar_1'], ['Gebruikers.UUID'], name=op.f('FK_Verordeningen_Eigenaar_1')),
    sa.ForeignKeyConstraint(['Eigenaar_2'], ['Gebruikers.UUID'], name=op.f('FK_Verordeningen_Eigenaar_2')),
    sa.ForeignKeyConstraint(['Gebied'], ['Werkingsgebieden.UUID'], name=op.f('FK_Verordeningen_Gebied')),
    sa.ForeignKeyConstraint(['Modified_By'], ['Gebruikers.UUID'], name=op.f('FK_Verordeningen_Modified_By')),
    sa.ForeignKeyConstraint(['Opdrachtgever'], ['Gebruikers.UUID'], name=op.f('FK_Verordeningen_Opdrachtgever')),
    sa.ForeignKeyConstraint(['Portefeuillehouder_1'], ['Gebruikers.UUID'], name=op.f('FK_Verordeningen_Portefeuillehouder_1')),
    sa.ForeignKeyConstraint(['Portefeuillehouder_2'], ['Gebruikers.UUID'], name=op.f('FK_Verordeningen_Portefeuillehouder_2')),
    sa.PrimaryKeyConstraint('UUID', name=op.f('PK_Verordeningen'))
    )

    op.create_table('Beleidskeuze_Maatregelen',
    sa.Column('Beleidskeuze_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Maatregel_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Koppeling_Omschrijving', sa.String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=True),
    sa.ForeignKeyConstraint(['Beleidskeuze_UUID'], ['Beleidskeuzes.UUID'], name=op.f('FK_Beleidskeuze_Maatregelen_Beleidskeuze_UUID')),
    sa.ForeignKeyConstraint(['Maatregel_UUID'], ['Maatregelen.UUID'], name=op.f('FK_Beleidskeuze_Maatregelen_Maatregel_UUID')),
    sa.PrimaryKeyConstraint('Beleidskeuze_UUID', 'Maatregel_UUID', name=op.f('PK_Beleidskeuze_Maatregelen'))
    )

    op.create_table('Beleidskeuze_Verordeningen',
    sa.Column('Beleidskeuze_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Verordening_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Koppeling_Omschrijving', sa.String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=True),
    sa.ForeignKeyConstraint(['Beleidskeuze_UUID'], ['Beleidskeuzes.UUID'], name=op.f('FK_Beleidskeuze_Verordeningen_Beleidskeuze_UUID')),
    sa.ForeignKeyConstraint(['Verordening_UUID'], ['Verordeningen.UUID'], name=op.f('FK_Beleidskeuze_Verordeningen_Verordening_UUID')),
    sa.PrimaryKeyConstraint('Beleidskeuze_UUID', 'Verordening_UUID', name=op.f('PK_Beleidskeuze_Verordeningen'))
    )

    op.create_table('Beleidsmodule_Maatregelen',
    sa.Column('Beleidsmodule_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Maatregel_UUID', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('Koppeling_Omschrijving', sa.String(collation='SQL_Latin1_General_CP1_CI_AS'), nullable=True),
    sa.ForeignKeyConstraint(['Beleidsmodule_UUID'], ['Beleidsmodules.UUID'], name=op.f('FK_Beleidsmodule_Maatregelen_Beleidsmodule_UUID')),
    sa.ForeignKeyConstraint(['Maatregel_UUID'], ['Maatregelen.UUID'], name=op.f('FK_Beleidsmodule_Maatregelen_Maatregel_UUID')),
    sa.PrimaryKeyConstraint('Beleidsmodule_UUID', 'Maatregel_UUID', name=op.f('PK_Beleidsmodule_Maatregelen'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Beleidsmodule_Maatregelen')
    op.drop_table('Beleidskeuze_Verordeningen')
    op.drop_table('Beleidskeuze_Maatregelen')
    op.drop_table('Verordeningen')
    op.drop_table('Onderverdeling')
    op.drop_table('Maatregelen')
    op.drop_table('Beleidsrelaties')
    op.drop_table('Beleidsmodule_Beleidskeuzes')
    op.drop_table('Beleidskeuze_Werkingsgebieden')
    op.drop_table('Beleidskeuze_Themas')
    op.drop_table('Beleidskeuze_Beleidsregels')
    op.drop_table('Beleidskeuze_Beleidsprestaties')
    op.drop_table('Beleidskeuze_Beleidsdoelen')
    op.drop_table('Beleidskeuze_Belangen')
    op.drop_table('Beleidskeuze_Ambities')
    op.drop_table('Werkingsgebieden')
    op.drop_table('Verordeningstructuur')
    op.drop_table('Themas')
    op.drop_table('Beleidsregels')
    op.drop_table('Beleidsprestaties')
    op.drop_table('Beleidsmodules')
    op.drop_table('Beleidskeuzes')
    op.drop_table('Beleidsdoelen')
    op.drop_table('Belangen')
    op.drop_table('Ambities')
    op.drop_table('Gebruikers')
    # ### end Alembic commands ###


def dialect_supports_sequences():
    return op._proxy.migration_context.dialect.supports_sequences


def dialect_supports_geometry_index():
    return op._proxy.migration_context.dialect.name == 'mssql'


def create_seq(name):
    if dialect_supports_sequences():
        op.execute(sa.schema.CreateSequence(sa.schema.Sequence(name)))


def drop_seq(name):
    if dialect_supports_sequences():
        op.execute(sa.schema.DropSequence(sa.schema.Sequence(name)))
