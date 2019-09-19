command = input("please select a humidity")


if the_humidity < 30:
    print("dry")
elif the_humidity > 60:
    print("high humidity")
elif the_humidity > 30 and the_humidity < 60:
    print("ok")
