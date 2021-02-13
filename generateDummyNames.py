def generate_dummy_names():
    import random
    first_names = ["Sarah", "Emily", "Emma", "Jessica", "Hannah", "Samantha", "Catherine", "Rachel", "Jade","Amy", "Julia",
               "Laurence","Audrey","Camille","Megan","Madison", "Marie","Gabrielle", "Ashley", "Taylor","Kayla","Maude",
               "Vanessa", "Alex", "Nathan","Simon","William","David","Nicolas","Samuel","Gabriel","Kevin","Charles",
               "Antoine","Jordan","Eric","Alexandre","vincent","Adam","Brandon","Ryan","Michael","Ben","Etienne","John",
               "Ethan"]
    last_names = ["Smith","Brown","Tremblay","Martin","Roy","Wilson","Macdonald","Gagnon","Johnson","Taylor","Cote",
              "Campbell","Anderson","Leblanc","Lee","Jones","White","Williams","Miller","Thompson","Gauthier","Young",
              "Van","Morin","Bouchard","Scott","Stewart","Belanger","Reid","Pelletier","Moore","Lavoie","King",
              "Robinson","Levesque","Murphy","Fortin","Gagne","Wong","Clark","Johnston","Clarke","Ross","Walker",
              "Thomas","Boucher","Landry","Kelly","Bergeron","Davis","Mitchell","Murray","Poirier","Mcdonald","Richard",
              "Wright","Girard","Lewis","Baker","Roberts","Simard","Graham","Caron","Harris","Jackson","Green",
              "Beaulieu","Fraser","Fournier","Kennedy","Hall","Hill","Chan","Wood","Lapointe","Ouellet","Bell","Dube",
              "Allen","Adams","Cloutier","Bennett","Lefebvre","Watson","Robertson","Walsh","Collins","Evans","Hebert",
              "Hamilton","Cameron","Desjardins","Russell","Nadeau","Cook","Michaud","Morrison","Singh","Grant","Parsons"]

    faculties = ["Computer Science", "Art","Design","English","poliSci","Math","Biology","Physics","Engineering","Chemistry"]
    interests = ["Skiing","Gaming","Coding","Drawing","Painting","Writing","Reading"]
    clubs = ["Club 1", "Club 2","Club 3","Club 4"]



    with open("DummyNames.csv", "w") as f:
        pwstring = "abcdefghizklmnopqrstuvwxyz"
        # f.truncate(0)  # clear previous contents
        for i in range(5000):
            fname = random.choice(first_names)
            lname = random.choice(last_names)
            f.write(str(fname+" "+lname+","+str(123000+i)+","+(''.join(pwstring) for i in range(10))+","
                        +random.choice(faculties)+","+random.choice(interests)+","+"https://instagram.com/"+
                        fname+lname+","+random.choice(clubs)+","+"Dummy Class ID"))
    print("done")
