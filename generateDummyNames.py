
interests = ["Outdoor Sports", "Gaming", "Coding", "Drawing/Painting", "Writing","Reading", "Travelling", "Music",
                 "Indoor Sports", "Arts and Crafts", "Action Movies", "Romance Movies", "Exercising", "Cooking",
                 "photography", "Watching Theatre"]


def generate_interests():
    import random
    bool_interests = [False]*len(interests)
    for i in range(random.randint(0,4)):
        bool_interests[random.randint(0,len(interests)-1)] = True
    return bool_interests


def generate_social_medias(name,lastname):
    import random
    # Social Media format: Instagram Snapchat Discord Facebook
    social_medias = ['']*4
    for i in range(len(social_medias)):
        if random.random() > 0.5:
            if i == 0:
                social_medias[i] = "https://instagram.com/"+name+"."+lastname
            elif i == 1:
                social_medias[i] = name+lastname+str(random.randint(0, 1000))
            elif i == 2:
                social_medias[i] = name+lastname+"#"+str(random.randint(1000,9999))
            elif i == 3:
                social_medias[i] = "https://facebook.com/"+name+lastname
    return social_medias


def generate_dummy_classes():
    import random
    classes = []
    for i in range(random.randint(1,5)):
        j = random.randint(100, 999)
        if j not in classes:
            classes.append(j)
        else:
            i -= 1
    return classes


def generate_dummy_names():
    import random

    first_names = ["Sarah", "Emily", "Emma", "Jessica", "Hannah", "Samantha", "Catherine", "Rachel", "Jade","Amy", "Julia",
               "Laurence","Audrey","Camille","Megan","Madison", "Marie","Gabrielle", "Ashley", "Taylor","Kayla","Maude",
               "Vanessa", "Alex", "Nathan","Simon","William","David","Nicolas","Samuel","Gabriel","Kevin","Charles",
               "Antoine","Jordan","Eric","Alexandre","vincent","Adam","Brandon","Ryan","Michael","Ben","Etienne","John",
               "Ethan","Karanpal","Oscar","Vansh","Alec"]

    last_names = ["Smith","Brown","Tremblay","Martin","Roy","Wilson","Macdonald","Gagnon","Johnson","Taylor","Cote",
              "Campbell","Anderson","Leblanc","Lee","Jones","White","Williams","Miller","Thompson","Gauthier","Young",
              "Van","Morin","Bouchard","Scott","Stewart","Belanger","Reid","Pelletier","Moore","Lavoie","King",
              "Robinson","Levesque","Murphy","Fortin","Gagne","Wong","Clark","Johnston","Clarke","Ross","Walker",
              "Thomas","Boucher","Landry","Kelly","Bergeron","Davis","Mitchell","Murray","Poirier","Mcdonald","Richard",
              "Wright","Girard","Lewis","Baker","Roberts","Simard","Graham","Caron","Harris","Jackson","Green",
              "Beaulieu","Fraser","Fournier","Kennedy","Hall","Hill","Chan","Wood","Lapointe","Ouellet","Bell","Dube",
              "Allen","Adams","Cloutier","Bennett","Lefebvre","Watson","Robertson","Walsh","Collins","Evans","Hebert",
              "Hamilton","Cameron","Desjardins","Russell","Nadeau","Cook","Michaud","Morrison","Singh","Grant","Parsons",
              "Sekhon","Ryu","Srivastav","Siala","Zaiane"]

    majors = ["Computer Science", "Art","Design","English","poliSci","Math","Biology","Physics","Engineering","Chemistry"]

    clubs = ["Club 1", "Club 2","Club 3","Club 4"]
    print("Generating Dummy Users")
    with open("DummyNames.csv", "w") as f:
        # f.truncate(0)  # clear previous contents
        for i in range(5000):
            fname = random.choice(first_names)
            lname = random.choice(last_names)
            f.write(str(fname+" "+lname+"%"+str(123000+i)+"%"+ "test_password" +"%"
                        + random.choice(majors)+"%"+str(generate_interests())+"%"+str(generate_social_medias(fname, lname))+"%"+random.choice(clubs)+"%"+str(generate_dummy_classes())+"\n"))
    print("done")


