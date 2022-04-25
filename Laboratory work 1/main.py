from garden_area import *
import click


@click.command()
@click.option('--collect', is_flag=True, help='Собрать рассаду или плоды дерева')
@click.option('--weed', is_flag=True, help='Прополоть')
@click.option('--water', is_flag=True, help="Полить")
@click.option('--cure', is_flag=True, help="Вылечить")
@click.option('--pests', is_flag=True, help="Избавиться от вредителей")
@click.option('--fertilizer', is_flag=True, help="Использовать удобрение")
@click.option('--seedlings_new', is_flag=True, help="Посадить новою рассаду")
@click.option('--tree_new', is_flag=True, help="Посадить новое дерево")
@click.option('--seedlings_del', is_flag=True, help="Выкопать рассаду")
@click.option('--tree_del', is_flag=True, help="Выкорчевать дерево")
@click.option('--info', is_flag=True, help="Информация о сегодняшнем дне")
@click.option('--new_day', is_flag=True, help="Перейти к следующему дню")
def main(collect, weed, water, cure, pests, fertilizer, seedlings_new, tree_new, seedlings_del, tree_del, info,
         new_day):
    if collect:
        GardenArea.make_action("collect")
    elif weed:
        GardenArea.make_action("weed")
    elif water:
        GardenArea.make_action("water")
    elif cure:
        GardenArea.make_action("cure")
    elif pests:
        GardenArea.make_action("pests")
    elif fertilizer:
        GardenArea.make_action("fertilizer")
    elif seedlings_new:
        GardenArea.make_action("seedlings_new")
    elif tree_new:
        GardenArea.make_action("tree_new")
    elif seedlings_del:
        GardenArea.make_action("seedlings_del")
    elif tree_del:
        GardenArea.make_action("tree_del")
    elif info:
        GardenArea.make_action("info")
    elif new_day:
        GardenArea.make_action("new_day")


if __name__ == '__main__':
    SeedBed()
    Orchard()
    main()
