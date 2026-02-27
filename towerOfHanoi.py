def towerOfHenoi(n, source, destination, auxiliary):
    if n == 1:
        print(f'Move disc 1 from {source} to {destination}')
        return 
    towerOfHenoi(n-1, source, auxiliary, destination)
    print(f'Move disc {n} from {source} to {destination}')
    towerOfHenoi(n-1, auxiliary, destination, source)
    
towerOfHenoi(3, 'A', 'C', 'B')