def main():
    comparar_extensions(receber_nome())


def receber_nome():
    file_name = input("File name: ").lower()
    return file_name


def comparar_extensions(nome_arquivo):
    e = ""
    if ".gif" in nome_arquivo:
        e = "image/gif"
    elif ".jpg" in nome_arquivo or "jpeg" in nome_arquivo:
        e = "image/jpeg"
    elif ".png" in nome_arquivo:
        e = "image/png"
    elif ".pdf" in nome_arquivo:
        e = "application/pdf"
    elif ".txt" in nome_arquivo:
        e = "text/plain"
    elif ".zip" in nome_arquivo:
        e = "application/zip"
    else:
        e = "application/octet-stream"

    print(e)


main()
