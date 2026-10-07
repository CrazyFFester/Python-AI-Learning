user_input = input()
ext_point = 0
for i, v in enumerate(user_input):
    if v == ".":
        ext_point = i

user_input = user_input[ext_point+1:]

match (user_input):
    case "gif":
        print("GIF file")
    case "jpg":
        print("JPG file")
    case "jpeg":
        print("JPEG file")
    case "png":
        print("PNG file")
    case "pdf":
        print("PDF file")
    case "txt":
        print("TEXT file")
    case "zip":
        print("Zipped File")