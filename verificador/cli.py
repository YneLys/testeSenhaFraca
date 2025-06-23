import argparse
from verificador.checker import verificar_sha1, verificar_brute

def iniciar_cli():
    parser = argparse.ArgumentParser(description="Verificador de Senhas Fracas")
    parser.add_argument("--arquivo", required=True, help="Caminho do arquivo CSV com senhas")
    parser.add_argument("--modo", choices=["sha1", "brute"], required=True, help="Modo de verificação")

    args = parser.parse_args()

    if args.modo == "sha1":
        verificar_sha1(args.arquivo)
    elif args.modo == "brute":
        verificar_brute(args.arquivo)
