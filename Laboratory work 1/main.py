import click

from garden_area import *


@click.command()
@click.option('--collect', default='', help='Собрать рассаду или плоды дерева')
@click.option('--weed', default='', help='Прополоть')
@click.option('--water', default='', help="Полить")
@click.option('--cure', default='', help="Вылечить")
@click.option('--pests', default='', help="Избавиться от вредителей")
@click.option('--fertilizer', default='', help="Использовать удобрение")
@click.option('--seedlings_new', default='', help="Посадить новою рассаду")
@click.option('--tree_new', default='', help="Посадить новое дерево")
@click.option('--seedlings_del', default='', help="Выкопать рассаду")
@click.option('--tree_del', default='', help="Выкорчевать дерево")
@click.option('--info', is_flag=True, help="Информация о сегодняшнем дне")
@click.option('--new_day', is_flag=True, help="Перейти к следующему дню")
def main(collect, weed, water, cure, pests, fertilizer, seedlings_new, tree_new, seedlings_del, tree_del, info,
         new_day):
    if collect:
        GardenArea.make_action("collect", collect)
    elif weed:
        GardenArea.make_action("weed", weed)
    elif water:
        GardenArea.make_action("water", water)
    elif cure:
        GardenArea.make_action("cure", cure)
    elif pests:
        GardenArea.make_action("pests", pests)
    elif fertilizer:
        GardenArea.make_action("fertilizer", fertilizer)
    elif seedlings_new:
        GardenArea.make_action("seedlings_new", seedlings_new)
    elif tree_new:
        GardenArea.make_action("tree_new", tree_new)
    elif seedlings_del:
        GardenArea.make_action("seedlings_del", seedlings_del)
    elif tree_del:
        GardenArea.make_action("tree_del", tree_del)
    elif info:
        GardenArea.make_action("info")
    elif new_day:
        GardenArea.make_action("new_day")


if __name__ == '__main__':
    SeedBed()
    Orchard()
    main()
