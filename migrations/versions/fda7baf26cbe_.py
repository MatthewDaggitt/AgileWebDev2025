"""empty message

Revision ID: fda7baf26cbe
Revises: f998ec2e4f0f
Create Date: 2025-05-08 16:33:31.507579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fda7baf26cbe'
down_revision = 'f998ec2e4f0f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.drop_column('student_one')
        batch_op.drop_column('student_two')
        batch_op.drop_column('student_four')
        batch_op.drop_column('student_three')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('student_three', sa.VARCHAR(length=8), nullable=False))
        batch_op.add_column(sa.Column('student_four', sa.VARCHAR(length=8), nullable=False))
        batch_op.add_column(sa.Column('student_two', sa.VARCHAR(length=8), nullable=False))
        batch_op.add_column(sa.Column('student_one', sa.VARCHAR(length=8), nullable=False))

    op.drop_table('student')
    # ### end Alembic commands ###
