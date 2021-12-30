class BeaconMap:
    n_overlaps = 12
    def __init__(self, scannertext) -> None:
        self.scanners = []
        for st in scannertext:
            scan = Scanner(st)
            self.scanners.append(scan)

class Scanner:
    scan_range = 1000
    def __init__(self, scans) -> None:
        self.beacons = []
        for s in scans:
            self.add_beacon(s)
        self.orientation = [1,1,1]

    def add_beacon(self, s):
        x = int(s[0])
        y = int(s[1])
        z = int(s[2])
        self.beacons.append([x, y, z])

def main():
    
    scanners = []

    relative_path = 'src/tasks/advent_of_code_21/day19_input.txt'
    with open(relative_path, 'r') as f:
        scan = []
        for line in f:
            if 'scan' in line:
                scan_id = [int (s) for s in line.split() if s.isdigit()]
                scan.append(scan_id[0])
            elif line.strip():
                scan.append(line.strip())
            else:
                scanners.append(scan)
                scan = []
    #print(f'{scanners}')

    bmap = BeaconMap(scanners)


if __name__ == '__main__':
    main()