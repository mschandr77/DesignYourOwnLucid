
def airModel():
    userModel = input("What trim of the Lucid Air will you be purchasing today?")
    if userModel == "Air Pure":
        airPure = 69900
        print("Your air pure model of your chosen trim currently costs: " + str(airPure) + ".")
    elif userModel == "Air Touring":
        airTouring = 78900
        print("Your air touring model of your chosen trim currently costs: " + str(airTouring) + ".")
    elif userModel == "Air Grand Touring":
        air_grand_touring = 110900
        print("Your air grand touring model of your chosen trim currently costs: " + str(air_grand_touring) + ".")
    elif userModel == "Air Sapphire":
        airSapphire = 249000
        print("Your air sapphire model of your chosen trim currently costs: " + str(airSapphire) + ".")
    else:
        print("Enter a valid trim for your Lucid Air model.")
    selectColor = input("What preferred color would you like, for your car,from the following options: Stellar White Metallic, Infinite Black Metallic, Cosmos Silver Metallic, Quantam Grey Metallic, Zenith Red Metallic, or Fanthom Blue Metallic")
    airPure = 0
    airTouring = 0
    air_grand_touring = 0
    airSapphire = 0
    if selectColor == "Stellar White Metallic":
        swmPure = airPure + 0
        swmTouring = airTouring + 0
        swmGT = air_grand_touring + 0
        swmAS = airSapphire + 0
    elif selectColor == "Infinite Black Metallic":
        ibmPure = airPure + 0
        ibmTouring = airTouring + 0
        ibmGT = air_grand_touring + 0
        ibmAS = airSapphire + 0
    elif selectColor == "Cosmos Silver Metallic":
        csmPure = airPure + 800
        csmTouring = airTouring + 800
        csmGT =  air_grand_touring + 800
        csmAS = airSapphire + 800
    elif selectColor == "Quantum Grey Metallic":
        qgmPure = airPure + 800
        qgmTouring = airTouring + 800
        qgmGT = air_grand_touring + 800
        qgmAS = airSapphire + 800
    elif selectColor == "Zenith Red Metallic":
        zrmPure = airPure + 800
        zrmTouring = airTouring + 800
        zrmGT = air_grand_touring + 800
        zrmAS = airSapphire + 800
    elif selectColor == "Fanthom Blue Metallic":
        fbmPure = airPure + 800
        fbmTouring = airTouring + 800
        fbmGT = air_grand_touring + 800
        fbmAS = airSapphire + 800
    else:
        print("Choose from one of six potential color palettes.")
    chosenAppearance = input("Choose either the base appearance or purchase the premium appearance.")
    airTouring = 0
    air_grand_touring = 0
    airSapphire = 0
    if chosenAppearance == "Platinum with Aluminum Roof":
        parPure = airPure + 0
        parTouring = airTouring + 0
        parGT = air_grand_touring + 0
        parAS = airSapphire + 0
    elif chosenAppearance == "Pure Stealth with Aluminum Roof":
        psarPure = airPure + 1750
        psarTouring = airTouring + 1750
        psarGT = air_grand_touring + 1750
        psarAS = airSapphire + 1750
    chosenWheels = input("Choose either the base 19'' Aero Range wheels or the 20'' Aero Lite (RWD Version) wheels.")
    if chosenWheels == "19'' Aero Range":
        narPure = airPure + 0
        narTouring = airTouring + 0
        narGT = air_grand_touring + 0
        narAS = airSapphire + 0
    elif chosenWheels == "20'' Aero Lite (RWD Version)":
        tarPure = airPure + 1750
        tarTouring = airTouring + 1750
        tarGT = air_grand_touring + 1750
        tarAS = airSapphire + 1750
    else:
        print("Please choose either the base 19'' Aero Range set of wheels or the 20'' Aero Lite (RWD) Version set of wheels.")
    chosenInterior = input("Please choose either the Mojave PurLuxe Leather Alternative or Santa Cruz Leather interior option.")
    tarPure = 0
    tarTouring = 0
    tarGT = 0
    tarAS = 0
    if chosenInterior == "Mojave Purluxe Leather Alternative":
        mojavePure = tarPure + 0
        mojaveTouring = tarTouring + 0
        mojaveGT = tarGT + 0
        mojaveAS = tarAS + 0
    if chosenInterior == "Santa Cruz Leather":
        mojavePure = tarPure + 3000
        mojaveTouring = tarTouring + 3000
        mojaveGT = tarGT + 3000
        mojaveAS = tarAS + 3000
    else:
        print("Please choose either the Mojave PurLuxe Leather Alternative or Santa Cruz Leather interior option.")

    firstFeature = input("Please choose either the DreamDrive Premium driver assistance system or the advanced DreamDrive Pro driver assistance system.")
    if firstFeature == "DreamDrive Premium":
        dasPure = mojavePure + 0
        dasTouring = mojaveTouring + 0
        dasGT = mojaveGT + 0
        dasAS = mojaveAS + 0
    elif firstFeature == "DreamDrive Pro":
        dasPure = mojavePure + 2500
        dasTouring = mojaveTouring + 2500
        dasGT = mojaveGT + 2500
        dasAS = mojaveAS + 2500
    else:
        print("Please choose either the DreamDrive Premium driver assistance system or the advanced DreamDrive Pro driver assistance system.")
    secondFeature = input("Please choose either the included Surreal Sound system or the premium Surreal Sound Pro system.")
    dasPure = 0
    dasTouring = 0
    if secondFeature == "Surreal Sound":
        ssPure = dasPure + 0
        ssTouring = dasTouring + 0
        ssGT = mojaveGT + 0
        ssAS = mojaveAS + 0
    elif secondFeature == "Surreal Sound Pro":
        ssPure = dasPure + 2900
        ssTouring = dasTouring + 2900
        ssGT = mojaveGT + 2900
        ssAS = mojaveAS + 2900
    else:
        print("Please choose either the included Surreal Sound system or the premium Surreal Sound Pro system.")
    thirdFeature = input("Please choose either the 12-way Power Heated Front Seats or the 20-Way Power Heated Front Seats With Ventilation And Massage option.")
    if thirdFeature == "12-Way Power Heated Front Seats":
        seatingPure = ssPure + 0
        seatingTouring = ssTouring + 0
        seatingGT = ssGT + 0
        seatingAS = ssAS + 0
    elif thirdFeature == "20-Way Power Heated Front Seats With Ventilation and Massage":
        seatingPure = ssPure + 3750
        seatingTouring = ssTouring + 3750
        seatingGT = ssGT + 3750
        seatingAS = ssAS + 3750
    else:
        print("Please choose either the 12-way Power Heated Front Seats or the 20-Way Power Heated Front Seats With Ventilation And Massage option.")
    fourthFeature = input("Would you like the extra Comfort and Convenience Package?")
    if fourthFeature == "yes":
        ccpPure = seatingPure + 2500
        ccpTouring = seatingTouring + 2500
        ccpGT = seatingGT + 2500
        ccpAS = seatingAS + 2500
    else:
        print("Please select a preference for the Comfort and Convenience Package")
    print("Your Lucid Air Pure model currently has the total cost of:$ " + str(ccpPure) + ".")
    print("Your Lucid Air Touring model currently has the total cost of:$ " + str(ccpTouring) + ".")
    print("Your Lucid Air Grand Touring model currently has the total cost of :$ " + str(ccpGT) + ".")
    print("Your Lucid Air Sapphire model currently has the total cost of :$" + str(ccpAS) + ".")

airModel()