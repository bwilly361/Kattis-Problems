def license_to_launch():
    n = int(input())
    junk_pieces_day = list(map(int, input().split()))
    
    junk_days_sorted = sorted(junk_pieces_day)
    smallest_num = junk_days_sorted[0]
    smallest_num_index = junk_pieces_day.index(smallest_num)

    print(smallest_num_index)

if __name__ == '__main__':
    license_to_launch()