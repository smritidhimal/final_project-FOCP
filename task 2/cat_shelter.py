import sys

def analyze_log(file_path):
    """
    Analyzes a cat log file and prints statistics about cat visits.

    This function takes a file path as a parameter, reads the content of the log file,
    and analyzes the data to print statistics about cat visits, intruding cats, total time in the house,
    and visit lengths.

    Parameters:
    - file_path (str): The path to the cat log file.

    Returns:
    None
    """
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        cat_visits = 0
        intruding_cats = 0
        total_time_in_house = 0
        visit_lengths = []

        for line in lines:
            if line.strip() == 'END(log file)':
                break

            parts = line.strip().split(',')
            
            # Check if the parts list has the expected number of elements
            if len(parts) == 3:
                cat_type, entry_time, exit_time = parts[0], int(parts[1]), int(parts[2])

                if cat_type == 'OURS':
                    cat_visits += 1
                    total_time_in_house += exit_time - entry_time
                    visit_lengths.append(exit_time - entry_time)
                elif cat_type == 'THEIRS':
                    intruding_cats += 1
            else:
                print(f"{line}")

        if cat_visits == 0:
            print('No valid data available for the correct cat.')
            sys.exit(1)

        if len(visit_lengths) > 0:
            average_visit_length = sum(visit_lengths) // len(visit_lengths)
            longest_visit = max(visit_lengths)
            shortest_visit = min(visit_lengths)
        else:
            average_visit_length = longest_visit = shortest_visit = 0

        print(f"{'Log File Analysis'}\n{'='*18}\n")
        print(f"Cat Visits: {cat_visits}")
        print(f"Other Cats: {intruding_cats}\n")
        print(f"Total Time in House: {total_time_in_house // 60} Hours, {total_time_in_house % 60} Minutes \n")
        print(f"Average Visit Length: {average_visit_length} Minutes")
        print(f"Longest Visit:        {longest_visit} Minutes")
        print(f"Shortest Visit:       {shortest_visit} Minutes")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze_log(file_path)
