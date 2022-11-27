def main():
    while True:
        try:
            szam1 = float(input("1. szam: "))
            szam2 = float(input("2. szam: "))
            result = szam1 / szam2
            print('Az osztas eredmenye: {0:.2f}'.format(result))
            print('-' * 10)
        except ZeroDivisionError as e:
            print("Hiba: 0ra nem lehet osztani")
        except ValueError as e:
            print("Adjá mán egy számot more!")
        except KeyboardInterrupt as e:
            print("Vege")
            break
#####

if __name__ == "__main__":
    main()