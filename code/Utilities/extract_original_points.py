# Imports
import math
import pandas as pd
import argparse


# Rounding Function
def round_half_up(n, decimals=3):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


if __name__ == "__main__":
    # Command line arg code
    parser = argparse.ArgumentParser(description='Atutorial of argparse!')
    parser.add_argument("--i", help = "Input file. Should be the picking_list from CC. Make sure to include the whole path to the file along with the file name")
    parser.add_argument("--d", help = "Original LiDAR data file that the points came from")
    parser.add_argument("--o", help = "Output file. Make sure to include the whole path if you want it in a different directory")

    args = parser.parse_args()
    input_file = args.i
    output_file = args.o
    data_file = args.d
    if input_file is None:
        input_file = input("Enter input file: ")

    if output_file is None:
        output_file = input("Enter output file: ")

    if data_file is None:
        data_file = input("Enter output file: ")

    # Read in point_picking list and modify dataframe by setting columns, changing ID column to dtype = string, and making rounding Easting, Northing, Altitude, and retro to 3 decimal points. 
    # The reason that I have to round is because, I believe, when it reads in values from the csv it converts it to int64 which makes it add these trailing decimal points. If I could make it just read in
    # the points without the trailing decimals, then this would be much faster
    print("Reading CC point list")
    picking_list = pd.read_csv(input_file, sep = " ", header = None)
    picking_list.columns = ["Easting", "Northing", "Altitude", "Retro"]
    print("Reading original data")

    # This data frame holds the original, unadulterated LiDAR data
    df = pd.read_csv(data_file, sep = " ")

    df = df.astype({'ID': str})
    # Figure out how to get rid of this code. Takes a lot of time.
    df['Easting'] = df['Easting'].apply(round_half_up)
    df['Northing'] = df['Northing'].apply(round_half_up)
    df['Altitude'] = df['Altitude'].apply(round_half_up)
    df['Retro'] = df['Retro'].apply(round_half_up)

    # Create output dataframe
    df2 = pd.DataFrame(columns = df.columns)

    print("Searching for points")
    # Actually finding the original points
    for index_main, row_main in picking_list.iterrows():
        easting_upper = row_main['Easting'] + 1.0
        easting_lower = row_main['Easting'] - 1.0
        northing_upper = row_main['Northing'] + 1.0
        northing_lower = row_main['Northing'] - 1.0
        altitude_upper = row_main['Altitude'] + 1.0
        altitude_lower = row_main['Altitude'] - 1.0
        df_temp = df.loc[(df['Easting'] > easting_lower) & (df['Easting'] < easting_upper) & (df['Northing'] > northing_lower) & (df['Northing'] < northing_upper) & (df['Altitude'] > altitude_lower) & (df['Altitude'] < altitude_upper)]
        
        for index, row in df_temp.iterrows():
            if (math.isclose(row['Easting'], row_main['Easting'], abs_tol = 0.001) and math.isclose(row['Northing'], row_main['Northing'], abs_tol = 0.001) and math.isclose(row['Altitude'], row_main['Altitude'], abs_tol = 0.001)):
                #print('true')
                df2 = df2.append(row)
                break

    # print(df2['ID'].str.contains('2191709').any())

    # Write found points out to .txt file
    # print("Writing to output file")
    # df2.to_csv(output_file, sep = ' ', index = False)

    # Go get original values from LiDAR file and write those to a new file
    print("Found points. Extracting original values and writing them to a new file")
    f = open(data_file, "r")
    f.readline()

    newf = open(output_file,"w")
    newf.write("ID Easting Northing Altitude Retro Angle Distance UTC Long Lat\n")

    min = int(df2['ID'].min()) - 100
    max = int(df2['ID'].max()) + 100
    orig_point_index = int(df['ID'].min())
  
    for i, line in enumerate(f):
        offset = i + orig_point_index

        if offset > min and offset < max:
            line_data = line.split(" ")
            if df2['ID'].str.contains(line_data[0]).any():
                #Write out all values to the new file
                newf.write(line)
        
    print('Finished extracting points')
    newf.close()
    f.close()






