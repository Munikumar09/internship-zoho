def main():
    user_input=input("file name: ")
    print(get_filetype(user_input))
def get_filetype(file:str) ->str:
    extension=((file.split("."))[-1]).lower().strip()
    filetype="application/octet-stream"
    match extension:
        case "gif":
            filetype="image/gif"
        case "jpg" | "jpeg":
            filetype="image/jpeg"
        case "png":
            filetype="image/png"
        case "pdf":
            filetype="application/pdf"
        case "txt":
            filetype="text/plain"
        case "zip":
            filetype="application/zip"
    return filetype
main()