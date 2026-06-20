import argparse
from logic.logic import Calculator


def main():
    calc = Calculator()

    parser = argparse.ArgumentParser(description="Simple calculator CLI")
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    parser.add_argument(
        "--op",
        choices=["add", "sub", "mul", "div"],
        required=True,
    )

    args = parser.parse_args()

    try:
        if args.op == "add":
            result = calc.add(args.a, args.b)
        elif args.op == "sub":
            result = calc.subtract(args.a, args.b)
        elif args.op == "mul":
            result = calc.multiply(args.a, args.b)
        elif args.op == "div":
            result = calc.divide(args.a, args.b)
        else:
            result = "Nieznana operacja"

        print(result)

    except ValueError as e:
        print(f"Błąd: {e}")


if __name__ == "__main__":
    main()
