def myFunc():
    print("Hello world!")



if __name__ == "__main__":
    # If this code is directly executed by running the file its present in
    print("We are directly running this code")
    myFunc()
    print(__name__)  #__name__ ka mtlb h jaha ye run hoga uss file ka naam prinnt krega but hum chahte h ki agar hum import krre h to aur file ka naam main h to uss file mae ye na chale isliye if conndition lagadi