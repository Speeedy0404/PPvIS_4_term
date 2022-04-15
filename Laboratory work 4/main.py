from garden_area import *
import click


@click.command()
@click.option('--collect', is_flag=True, help='Собрать рассаду или плоды дерева')
@click.option('--weed', is_flag=True, help='Прополоть')
@click.option('--water', is_flag=True, help="Полить")
@click.option('--cure', is_flag=True, help="Вылечить")
@click.option('--pests', is_flag=True, help="Избавиться от вредителей")
@click.option('--fertilizer', is_flag=True, help="Использовать удобрение")
@click.option('--seedlingsnew', is_flag=True, help="Посадить новою рассаду")
@click.option('--treenew', is_flag=True, help="Посадить новое дерево")
@click.option('--seedlingsdel', is_flag=True, help="Выкопать рассаду")
@click.option('--treedel', is_flag=True, help="Выкорчевать дерево")
@click.option('--info', is_flag=True, help="Информация о сегодняшнем дне")
@click.option('--newday', is_flag=True, help="Перейти к следующему дню")
def main(collect, weed, water, cure, pests, fertilizer, seedlingsnew, treenew, seedlingsdel, treedel, info, newday):
    my_garden = GardenArea("Престиж", collect, weed, water, cure, pests, fertilizer, seedlingsnew, treenew,
                           seedlingsdel, treedel, info, newday)


if __name__ == '__main__':
    main()
