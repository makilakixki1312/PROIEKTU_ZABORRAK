import os
import shutil


while True:

    try:
        karp = input("Sartu karpetaren bidea, hutsik utzi automatikoki sortzeko: ")
        if karp != "":
            b = karp
            os.mkdir(karp)
            print("\nKarpeta zuzen sortua!")
            break
        else:
            b = os.path.expanduser("~/Wazowski")
            os.mkdir(b)
            if os.path.expanduser("~").find('\\') != -1:
                print(os.path.expanduser("~") + "\\Wazowski karpeta sortua")
                break
            else:
                print(os.path.expanduser("~") + "/Wazowski karpeta sortua")
                break

    except KeyboardInterrupt:
        print("\nEragiketa ezeztatua")
        os._exit(1)

    except:
        if os.path.isdir(b) == True:
            print("Karpeta hau badago jadanik :'(")
        else:
            print("Ezin izan da karpeta sortu :'( ")

        while True:
            sarrera = input("Saiatu berriro? b/e: ")
            if sarrera == 'b' or sarrera == "bai" or sarrera == 'B' or sarrera == 'Bai':
                break
            elif sarrera == 'e' or sarrera == "ez" or input("Saiatu berriro? b/e: ") == 'E' or sarrera == 'Ez':
                os._exit(1)
            else:
                print("\nEz da ulertu jarritakoa...")

while True:
    try:
        argaz = input("Sartu Wazowski argazkiaren helbidea: ")
        if os.path.isfile(argaz) == False:
            print("Ezin izan da argazkia aurkitu")
            while True:
                sarrera = input("Saiatu berriro? b/e: ")
                if sarrera == 'b' or sarrera == "bai" or sarrera == 'B' or sarrera == 'Bai':
                    break
                elif sarrera == 'e' or sarrera == "ez" or input("Saiatu berriro? b/e: ") == 'E' or sarrera == 'Ez':
                    os._exit(1)
                else:
                    print("\nEz da ulertu jarritakoa...")
        else:
            while True:
                try:
                    kant = int(input("Sartu kopia kantitatea: "))
                except ValueError:
                    print("Ez da zenbaki bat")
                except KeyboardInterrupt:
                    print("\nEragiketa ezeztatua")
                    os._exit(1)
                break

    except KeyboardInterrupt:
        print("\nEragiketa ezeztatua")
        os._exit(1)
    except:
        print("Arazo ezezaguna")
        
    try:
        for i in range(1, kant + 1):
            a = shutil.copy(argaz, b + "/" + str(i) + ".jpg")
            print(a);

        print("Kopiaketa bukatua!")
        break
    except KeyboardInterrupt:
        print("\nEragiketa ezeztatua")
        os._exit(1)
    except:
        print("Ezin izan dira kopiak egin")
        while True:
            sarrera = input("Saiatu berriro? b/e: ")
            if sarrera == 'b' or sarrera == "bai" or sarrera == 'B' or sarrera == 'Bai':
                break
            elif sarrera == 'e' or sarrera == "ez" or input("Saiatu berriro? b/e: ") == 'E' or sarrera == 'Ez':
                os._exit(1)
            else:
                print("\nEz da ulertu jarritakoa...")