"""Seed legends data

Revision ID: a0f80308994f
Revises: 
Create Date: 2025-03-04 23:05:43.550356

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0f80308994f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    INSERT INTO legends (name, category, description, image_url, legend_date, province, canton, district, created_at)
    VALUES
      ('La Tulevieja', 'Mito', 'Leyenda sobre una mujer encantada que deambula por las noches.', 'https://example.com/images/tulevieja.jpg', '2020-05-10', 'San José', 'Desamparados', 'San Miguel', CURRENT_DATE),
      ('El Cadejos', 'Mito', 'Fábula sobre un perro demoníaco...', 'https://example.com/images/cadejos.jpg', '2021-07-15', 'Alajuela', 'San Ramón', 'Sarchí', CURRENT_DATE),
      ('La Llorona', 'Mito', 'Trágica historia de una mujer...', 'https://example.com/images/llorona.jpg', '2019-03-22', 'Cartago', 'Paraíso', 'La Unión', CURRENT_DATE),
      ('El Chupacabras', 'Mito', 'Relato de una criatura que ataca animales de granja.', 'https://example.com/images/chupacabras.jpg', '2022-01-05', 'Heredia', 'Barva', 'San Pablo', CURRENT_DATE),
      ('La Siguanaba', 'Mito', 'Fantasma femenino que aparece en la noche...', 'https://example.com/images/siguanaba.jpg', '2021-11-11', 'San José', 'Desamparados', 'San Juan', CURRENT_DATE),
      ('El Duende', 'Mito', 'Pequeño ser travieso...', 'https://example.com/images/duende.jpg', '2020-09-30', 'Guanacaste', 'Liberia', 'Nicoya', CURRENT_DATE),
      ('La Ciguapa', 'Leyenda', 'Mujer misteriosa con pies al revés...', 'https://example.com/images/ciguapa.jpg', '2018-06-18', 'Puntarenas', 'Quepos', 'Parrita', CURRENT_DATE),
      ('El Fantasma de la Carreta', 'Leyenda', 'Historia de un antiguo conductor...', 'https://example.com/images/fantasma_carreta.jpg', '2017-12-12', 'San José', 'Alajuelita', 'San Isidro', CURRENT_DATE),
      ('La Dama de Blanco', 'Leyenda', 'Figura espectral vestida de blanco...', 'https://example.com/images/dama_blanco.jpg', '2020-02-29', 'Limón', 'Pococí', 'Guácimo', CURRENT_DATE),
      ('El Gigante del Valle', 'Leyenda', 'Relato sobre un ser enorme...', 'https://example.com/images/gigante_valle.jpg', '2019-08-08', 'San José', 'Escazú', 'San Rafael', CURRENT_DATE);
    """)


def downgrade() -> None:
    op.execute("""
    DELETE FROM legends
    WHERE name IN (
      'La Tulevieja',
      'El Cadejos',
      'La Llorona',
      'El Chupacabras',
      'La Siguanaba',
      'El Duende',
      'La Ciguapa',
      'El Fantasma de la Carreta',
      'La Dama de Blanco',
      'El Gigante del Valle'
    );
    """)
