# Group11-PNP-Optimization

Source folder contains python source code for the program. 

Build contains a pre-built version of the program.

How to use:
- Copy Build directory over to your PC. Data and Images folders are required for the program to run. Import folder contains CSV files we want to run the program on. The program works on both "import" style csv files, and on files exported from K1830. The program takes 10-20 seconds to finish executing 1 optimiziation.

- Run K1830_opt.exe, We set up Example1.csv and Example2.csv to show how the program works for both input cases. The button at the top right runs the program optimization on the selected file. In the case of Example1, the  #Feeder, #Nozzle, #PCB, #Panel and #Mark sections are output based on what is in the csv files in the Data folder. If the nozzles don't match, then the program will decide on a different nozzle selection and change them automatically. If some component data is missing, they must be added to Compdata.csv. In the case of Example2, we just keep all the sections besides #comp the same and only change the feeders and nozzles order (The program should give a warning). The output csv file is stored in the output folder that the program automatically creates. 

- The second button does the same thing, but also runs a simulation. This was mainly created for our course presentation, but it gives an approximation of how much the nozzle arm is moving. Not tested extensively.

- last button exits the program.

- To run the optimization on a new file, simply copy to the import folder a new csv file in one of the 2 formats mentioned above.
