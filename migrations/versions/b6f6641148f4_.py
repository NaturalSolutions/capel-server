"""empty message

Revision ID: b6f6641148f4
Revises: 
Create Date: 2018-05-30 10:47:46.555222

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b6f6641148f4'
down_revision = None
branch_labels = None
depends_on = None
import geoalchemy2

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.drop_table('spatial_ref_sys')
    op.drop_table('coeurs')
    op.drop_table('sites')
    op.add_column('divesites', sa.Column('category', sa.String(), nullable=True))
    op.add_column('divesites', sa.Column('geom_mp', geoalchemy2.types.Geometry(geometry_type='MULTIPOINT'), nullable=True))
    op.add_column('divesites', sa.Column('geom_poly', geoalchemy2.types.Geometry(geometry_type='MULTIPOLYGON'), nullable=True))
    op.add_column('divesites', sa.Column('latitude', sa.String(), nullable=True))
    op.add_column('divesites', sa.Column('longitude', sa.String(), nullable=True))
    op.add_column('divesites', sa.Column('name', sa.String(), nullable=True))
    op.add_column('divesites', sa.Column('status', sa.String(), nullable=True))
    op.drop_index('idx_divesites_geom', table_name='divesites')
    op.drop_column('divesites', 'geom')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('divesites', sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='POLYGON'), autoincrement=False, nullable=True))
    op.create_index('idx_divesites_geom', 'divesites', ['geom'], unique=False)
    op.drop_column('divesites', 'status')
    op.drop_column('divesites', 'name')
    op.drop_column('divesites', 'longitude')
    op.drop_column('divesites', 'latitude')
    op.drop_column('divesites', 'geom_poly')
    op.drop_column('divesites', 'geom_mp')
    op.drop_column('divesites', 'category')
    op.create_table('sites',
    sa.Column('id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='MULTIPOINT', srid=4326), autoincrement=False, nullable=True),
    sa.Column('source', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('nom_site_p', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('lat', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('long', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('numerisati', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('precision', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('ssm', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('reg_dept', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('classe_m', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('type_site', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('dispo_amar', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('expo_vents', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('site_abrit', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('freq_nb_pl', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('interet_pl', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('habitats_p', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('etat_conse', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('perim_prot', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('struct_ges', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('conflits_u', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('sensib', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('prof_min', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('prof_max', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('naturel', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('artificiel', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('encadre', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('acces_libr', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('nivminreq', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('actconcern', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('mesenplace', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('etatconser', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('criteco', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('pressplong', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('pressautus', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('critusages', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('valpaysag', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('connaiseco', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('connaisusa', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('critconnai', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('critgest', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('nivenjeux', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('enjeux', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('indiceprio', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('priorite', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('interpgest', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('interpconn', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('interpusag', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('categorie', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('refdocgest', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('refpublisc', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('refquest', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('refbddlign', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('refcoorgps', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('date', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('id_site', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('interet', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='sites_pkey')
    )
    op.create_table('coeurs',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('geom', geoalchemy2.types.Geometry(geometry_type='MULTIPOLYGON', srid=4326), autoincrement=False, nullable=True),
    sa.Column('objectid', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('amp_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('mpa_name', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('mpa_orinam', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('des_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('des_desigf', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('des_desigt', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('mpa_status', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('mpa_stat_1', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('desmpa_des', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('mpa_wdpaid', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('mpa_wdpapi', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('mpa_mnhnid', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('mpa_marine', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('mpa_calcar', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('mpa_calcma', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('mpa_repare', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('mpa_repmar', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('mpa_foruma', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('mpa_url', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('mpa_update', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('mpa_dateen', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('iucn_idiuc', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('subloc_cod', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('subloc_nam', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('country_pi', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('country_is', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.Column('country__1', sa.VARCHAR(length=254), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='coeurs_pkey')
    )
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('(srid > 0) AND (srid <= 998999)', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    )
    # ### end Alembic commands ###
