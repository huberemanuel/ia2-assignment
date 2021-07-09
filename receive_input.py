def main():
    print("Aversão ou afinidade ao risco")
    print("-" * 20)
    print(
        """
    Você está jogando um jogo no estilo Show do Milhão apresentado por Silvio Santos,
    então acumula o prêmio de 1 milhão de reais. Silvio, te oferece uma nova proposta,
    se você jogar uma moeda e cair coroa irá receber mais R$ 2,5 milhões de reais
    (adicionais), mas se cair cara irá perder toda a quantia acumulada.
    Talvez você não aceite ela sendo que já possui R$ 1 milhão em mãos, mas para
    quais valores você aceitaria este risco?

    Obs: É uma moeda justa, portanto você possui 50% de chances de ganhar ou perder
    o prêmio adicional.
    """
    )

    users = {}
    values = [
        (100, 250),
        (500, 1250),
        (1000, 2500),
        (10000, 25000),
        (50000, 125000),
        (500000, 1250000),
        (1000000, 2500000),
        (10000000, 25000000),
    ]
    while True:
        print("Recebendo dados do usuário {}".format(len(values)))
        user_name = input("Insira o nome do usuário: ")
        users[user_name] = []
        print("Responda as seguintes afirmações com S para sim ou N para não")
        for lower, higher in values:
            res = input(
                "Se você tiver acumulado R$ {}, aceita arriscar pelo prêmio adicional de R$ {}? ".format(
                    lower, higher
                )
            ).lower()
            users[user_name].append(res == "s")
        op = input("Deseja inserir os dados de mais um usuário (S/N)? ")
        if op.lower() == "n":
            break

    print("Exibindo as respostas coletadas dos usuários:")
    for user, options in users.items():
        print("Usuário: {}".format(user))
        for option, (lower, higher) in zip(options, values):
            if not option:
                print("Não ", end="")
            print(
                "aceita arriscar R$ {} para poder receber o adicional de R$ {} ".format(
                    lower, higher
                )
            )


if __name__ == "__main__":
    main()
