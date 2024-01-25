def calculate_packages(num_people,hotdogs_per_person):
    hotdogs_per_person = 10
    buns_per_packages = 8
    total_hotdogs=num_people*hotdogs_per_person
    hotdog_packages = math.ceil(total_hotdogs/hotdog_packages)
    hotdogs_leftover = (hotdog_packages*hotdog_per_package)-total_hotdogs
    total_buns = num_people*hotdogs_per_person
    buns_packages = math.ceil(total_buns/buns_per_packages)
    buns_leftover = (buns_packages*buns_per_packages)
    buns_leftover = (buns_packages*buns_per_packages)-total_buns
    print("Minimum number of hotdog packages required:",hotdog_packages)
    print("Minimum number of bun packages required:",buns_packages)
    print("Number of bun leftover:",buns_leftover)
    num_people = int(input("Enter the number of people attending the cookout:"))
    hotdogs_per_person = int(input("Enter the number of hotdogs each person will be given:"))
