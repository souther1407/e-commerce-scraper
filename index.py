from scrapper import Scrapper
import argparse
from constants import *
parser = argparse.ArgumentParser(
    description="""Permite realizar web scraping en diferentes tiendas online para obtener precios,
                   y otras estadisticas útiles""",

)
parser.add_argument("-p", "--producto", type=str,
                    help="el producto a buscar",
                    required=True)
parser.add_argument("-o", "--ordenar", type=str,
                    help="ordena los resultados por precio o titulo",
                    choices=[SORT_TITLE_ASC, SORT_TITLE_DESC,
                             SORT_PRICE_ASC, SORT_PRICE_DESC, NO_SORT],
                    required=False,
                    default=NO_SORT)
parser.add_argument("-m", "--mercado", type=str,
                    choices=["mercadolibre", "amazon", "fullhard"],
                    default="mercadolibre",
                    required=False,
                    help="selecciona el mercado que querés consultar")

args = parser.parse_args()

# %20 es el espacio en las urls


scrapper = Scrapper()

scrapper.getResults(product=args.producto, orders=args)
