"""empty message

Revision ID: 6235c54013b9
Revises: 93fc3e074dcc
Create Date: 2023-03-01 16:26:08.792673

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6235c54013b9'
down_revision = '93fc3e074dcc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('documents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filepath', sa.String(length=255), nullable=True),
    sa.Column('hash_doc', sa.String(length=120), nullable=True),
    sa.Column('date_inserted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_documents_date_inserted'), 'documents', ['date_inserted'], unique=False)
    op.add_column('assignments', sa.Column('department_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'assignments', 'departments', ['department_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'assignments', type_='foreignkey')
    op.drop_column('assignments', 'department_id')
    op.drop_index(op.f('ix_documents_date_inserted'), table_name='documents')
    op.drop_table('documents')
    # ### end Alembic commands ###
