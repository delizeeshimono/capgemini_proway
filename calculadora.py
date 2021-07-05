import argparse
import math

MAX_SHARE = 3


def get_clicks(views: int) -> int:
    """
    Calculates the number of clicks based in the number of views.
    """
    return int(math.floor(views * 0.12))


def get_shares_by_clicks(clicks: int) -> int:
    """
    Calculates number of shares given a number of clicks.
    """
    return int(math.floor(clicks * 0.15))


def get_views_by_share(shares: int) -> int:
    """
    Given a number of shares, calculates the number of views.
    """
    return shares * 40


def main(valor: int):
    result = valor*40
    cycle_views = result
    for cycle in range(MAX_SHARE):
        clicks = get_clicks(cycle_views)
        shares = get_shares_by_clicks(clicks)
        new_views = get_views_by_share(shares)
        result += new_views
        cycle_views = new_views

    print(f"Estimativa de visualizações: {result}")


def check_positive(value):
    """
    Checks if an argument from argparse is a positive int and raises
    an exception otherwise.
    """
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(
            "%s não é positivo. Use apenas inteiros positivos." % value)
    return ivalue


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Calcula o número aproximado de Visualizações de um anúncio.')
    parser.add_argument('--valor', type=check_positive,
                        help='Valor em Reais (somente parte inteira, sem centavos)')
    args = parser.parse_args()
    main(args.valor)
